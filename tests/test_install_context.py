"""Pruebas aisladas: nunca escriben en el home real ni acceden a cuentas."""

import contextlib
import importlib.util
import io
import json
import os
import sys
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("installer", Path(__file__).resolve().parents[1] / "scripts/install-context.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.source = self.base / "source"
        self.source.mkdir()
        self.home = self.base / "home"
        for name in m.MODULES:
            (self.source / f"{name}.md").write_text(
                f"# {name}\n\n**Estado:** Aprobado por el responsable\n\nDato único: {name}-áéíóú.\n", encoding="utf-8")
        self.args = SimpleNamespace(source=self.source, home=self.home, profile="prueba",
                                    targets=["codex", "claude-code"], apply=True,
                                    codex_home=None, claude_home=None)
        self.codex = self.home / ".codex/AGENTS.md"
        self.claude = self.home / ".claude/CLAUDE.md"
        self.store = self.home / ".personal-context-portfolio"

    def run_silent(self, fn):
        with contextlib.redirect_stdout(io.StringIO()):
            return fn(self.args)

    def seed(self, path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def test_dry_run_writes_nothing(self):
        self.args.apply = False
        self.run_silent(m.install)
        self.assertFalse(self.home.exists())

    def test_all_ten_verbatim_and_existing_content_preserved(self):
        before = b"# Mis reglas\r\n\r\nNo editar.\r\n"
        self.seed(self.codex, before)
        self.seed(self.claude, before)
        self.run_silent(m.install)
        for target in (self.codex, self.claude):
            data = target.read_bytes()
            self.assertTrue(data.startswith(before))
            for path in self.source.glob("*.md"):
                self.assertIn(path.read_bytes(), data)
        self.run_silent(m.status)
        self.assertIn("Pendiente de acceso", (self.store / "ESTADO-INSTALACION.md").read_text(encoding="utf-8"))

    def test_rerun_is_idempotent(self):
        self.run_silent(m.install)
        before = self.codex.read_bytes()
        backup_count = len(list((self.store / "backups").iterdir()))
        self.run_silent(m.install)
        self.assertEqual(before, self.codex.read_bytes())
        self.assertEqual(backup_count, len(list((self.store / "backups").iterdir())))

    def test_update_keeps_unmanaged_edits_and_backs_up(self):
        self.run_silent(m.install)
        extra = b"\nRegla agregada por el usuario.\n"
        before = self.codex.read_bytes() + extra
        self.codex.write_bytes(before)
        p = self.source / "identity.md"
        p.write_text(p.read_text(encoding="utf-8") + "Nuevo dato aprobado.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "pendiente de sincronizar"):
            self.run_silent(m.status)
        self.run_silent(m.install)
        self.assertTrue(self.codex.read_bytes().endswith(extra))
        self.assertIn(b"Nuevo dato aprobado.", self.claude.read_bytes())
        self.assertTrue(any(p.read_bytes() == before for p in (self.store / "backups").rglob("*.bak")))
        self.run_silent(m.status)

    def test_override_and_custom_config_homes(self):
        self.args.codex_home = self.base / "codex-alt"
        self.args.claude_home = self.base / "claude-alt"
        target = self.args.codex_home / "AGENTS.override.md"
        self.seed(target, b"Override existente\n")
        self.run_silent(m.install)
        self.assertIn(m.BEGIN.encode(), target.read_bytes())
        self.assertFalse(self.codex.exists())
        self.assertTrue((self.args.claude_home / "CLAUDE.md").exists())
        self.run_silent(m.status)

    def test_new_override_detected(self):
        self.run_silent(m.install)
        self.seed(self.codex.with_name("AGENTS.override.md"), b"Nuevo override")
        with self.assertRaisesRegex(ValueError, "archivo activo"):
            self.run_silent(m.status)
        with self.assertRaisesRegex(ValueError, "archivo activo"):
            self.run_silent(m.install)

    def test_budget_rejects_before_any_write(self):
        self.seed(self.home / ".codex/config.toml", b"project_doc_max_bytes = 100\n")
        with self.assertRaisesRegex(ValueError, "No se recortaron"):
            self.run_silent(m.install)
        self.assertFalse(self.claude.exists())
        self.assertFalse(self.store.exists())

    def test_missing_or_unapproved_document(self):
        path = self.source / "identity.md"
        path.unlink()
        with self.assertRaisesRegex(ValueError, "Falta"):
            self.run_silent(m.install)
        path.write_text("# Borrador\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Aprobado"):
            self.run_silent(m.install)
        self.assertFalse(self.home.exists())

    def test_templates_examples_rejected(self):
        self.args.source = m.REPO / "examples/knowledge-worker"
        with self.assertRaisesRegex(ValueError, "fuera del repositorio"):
            self.run_silent(m.install)

    def test_distinct_profile_and_conflicting_managed_edits_rejected(self):
        self.run_silent(m.install)
        self.args.profile = "otro"
        with self.assertRaisesRegex(ValueError, "otro perfil"):
            self.run_silent(m.install)
        self.args.profile = "prueba"
        original = self.claude.read_bytes()
        self.codex.write_bytes(self.codex.read_bytes().replace(b"Contexto personal", b"Contexto editado"))
        with self.assertRaisesRegex(ValueError, "cambió por fuera"):
            self.run_silent(m.install)
        self.assertEqual(original, self.claude.read_bytes())

    def test_changed_installed_documents_block_update(self):
        self.run_silent(m.install)
        p = self.store / "documents/identity.md"
        p.write_bytes(p.read_bytes() + b"Cambio local")
        with self.assertRaisesRegex(ValueError, "copia instalada"):
            self.run_silent(m.install)

    def test_unknown_destination_and_malformed_markers_rejected(self):
        self.seed(self.codex, m.BEGIN.encode())
        with self.assertRaisesRegex(ValueError, "Marcadores"):
            self.run_silent(m.install)
        self.seed(self.codex, b"")
        self.seed(self.store / "notas.md", b"Datos existentes")
        with self.assertRaisesRegex(ValueError, "sin manifiesto"):
            self.run_silent(m.install)

    def test_uninstall_keeps_other_content_and_portfolio(self):
        before = b"Mis reglas previas\r\n"
        self.seed(self.codex, before)
        self.run_silent(m.install)
        self.run_silent(m.uninstall)
        self.assertTrue(self.codex.read_bytes().startswith(before))
        self.assertNotIn(m.BEGIN.encode(), self.codex.read_bytes())
        self.assertTrue((self.store / "CONTEXTO-COMPLETO.md").exists())
        self.assertEqual({}, json.loads((self.store / "installation.json").read_bytes())["targets"])
        self.run_silent(m.install)
        self.run_silent(m.status)

    def test_partial_update_is_rejected(self):
        self.run_silent(m.install)
        self.args.targets = ["codex"]
        with self.assertRaisesRegex(ValueError, "todos los destinos"):
            self.run_silent(m.install)

    def test_rollback_after_write_failure(self):
        before = b"Instrucciones originales"
        self.seed(self.codex, before)
        original = m.atomic
        def fail(path, data):
            if path == self.codex:
                raise OSError("Fallo simulado")
            return original(path, data)
        with patch.object(m, "atomic", side_effect=fail):
            with self.assertRaisesRegex(OSError, "simulado"):
                self.run_silent(m.install)
        self.assertEqual(before, self.codex.read_bytes())
        self.assertFalse(self.claude.exists())

    def test_home_override_ignores_host_environment(self):
        with patch.dict(os.environ, {"CODEX_HOME": str(self.base / "wrong"), "CLAUDE_CONFIG_DIR": str(self.base / "wrong2")}):
            self.run_silent(m.install)
        self.assertTrue(self.codex.exists())
        self.assertFalse((self.base / "wrong").exists())

    def test_cli_export_only_and_status(self):
        argv = ["install-context.py", "install", "--source", str(self.source),
                "--profile", "prueba", "--home", str(self.home), "--targets", "--apply"]
        with patch.object(sys, "argv", argv), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(0, m.main())
        self.assertTrue((self.store / "CONTEXTO-COMPLETO.md").exists())
        self.assertFalse(self.codex.exists())
        self.assertFalse(self.claude.exists())

    def test_tampered_manifest_cannot_redirect_uninstall(self):
        self.run_silent(m.install)
        unrelated = self.base / "unrelated.md"
        unrelated.write_bytes(self.codex.read_bytes())
        path = self.store / "installation.json"
        data = json.loads(path.read_bytes())
        data["targets"]["codex"]["path"] = str(unrelated)
        path.write_text(json.dumps(data), encoding="utf-8")
        before = unrelated.read_bytes()
        with self.assertRaisesRegex(ValueError, "fuera de la configuración"):
            self.run_silent(m.uninstall)
        self.assertEqual(before, unrelated.read_bytes())

    def test_symlink_guard_without_os_link_privilege(self):
        original = Path.is_symlink
        def pretend_link(path):
            return path == self.home / ".claude" or original(path)
        with patch.object(Path, "is_symlink", pretend_link):
            with self.assertRaisesRegex(ValueError, "enlace"):
                self.run_silent(m.install)
        self.assertFalse(self.codex.exists())

    def test_symlink_rejected(self):
        self.home.mkdir()
        other = self.base / "outside"
        other.mkdir()
        try:
            (self.home / ".claude").symlink_to(other, target_is_directory=True)
        except OSError:
            self.skipTest("El sistema no permite crear enlaces para esta prueba")
        with self.assertRaisesRegex(ValueError, "enlace"):
            self.run_silent(m.install)
        self.assertFalse(self.codex.exists())


if __name__ == "__main__":
    unittest.main()
