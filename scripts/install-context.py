"""Instala contexto aprobado en Codex y Claude Code; prepara la entrega web.

Python 3.11+. Sin dependencias, red, claves ni cambios de permisos de las apps.
Por defecto muestra un plan. Sólo --apply escribe archivos.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import tomllib
from datetime import datetime, timezone

MODULES = (
    "identity", "role-and-responsibilities", "current-projects",
    "team-and-relationships", "tools-and-systems", "communication-style",
    "goals-and-priorities", "preferences-and-constraints", "domain-knowledge",
    "decision-log",
)
BEGIN = "<!-- PCP:BEGIN -->"
END = "<!-- PCP:END -->"
REPO = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def checked_path(path):
    path = Path(path).expanduser().absolute()
    for part in (path, *path.parents):
        if part.is_symlink() or (hasattr(part, "is_junction") and part.is_junction()):
            raise ValueError(f"La ruta usa un enlace o junction; revisala manualmente: {part}")
    return path


def read(path):
    path = checked_path(path)
    return path.read_bytes() if path.exists() else b""


def atomic(path, data):
    path = checked_path(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd, name = tempfile.mkstemp(prefix=".pcp-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
        if path.exists():
            os.chmod(name, path.stat().st_mode & 0o777)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def decode(data):
    return data.decode("utf-8")


def managed_parts(data):
    start = BEGIN.encode()
    end = END.encode()
    if data.count(start) != data.count(end) or data.count(start) > 1:
        raise ValueError("Marcadores del kit duplicados o incompletos; no se sobrescribió el archivo.")
    if start not in data:
        return None
    a = data.index(start)
    b = data.index(end)
    if b < a:
        raise ValueError("Marcadores del kit fuera de orden.")
    return a, b + len(end)


def merge(existing, block, previous=None):
    decode(existing)  # No intentar modificar archivos con codificación desconocida.
    parts = managed_parts(existing)
    if parts:
        a, b = parts
        if previous is None or sha(existing[a:b]) != previous.get("block_sha256"):
            raise ValueError("El bloque del kit cambió por fuera del instalador o no tiene registro. Revisalo antes de actualizar.")
        return existing[:a] + block + existing[b:]
    if previous:
        raise ValueError("Falta el bloque registrado. Revisá si se quitó o movió antes de reinstalar.")
    return existing + (b"\n\n" if existing else b"") + block + b"\n"


def load_source(source):
    source = checked_path(source)
    if source.is_relative_to(REPO):
        raise ValueError("Usá documentos reales aprobados desde una carpeta privada fuera del repositorio, no plantillas ni ejemplos.")
    result = {}
    for name in MODULES:
        path = source / (name + ".md")
        if not path.is_file():
            raise ValueError(f"Falta uno de los diez documentos: {name}.md")
        data = read(path)
        text = decode(data)
        if not text.strip() or not re.search(r"^\*\*Estado:\*\* Aprobado por el responsable\s*$", text, re.M):
            raise ValueError(f"{name}.md debe tener Estado: Aprobado por el responsable; no cambies esa marca sin aprobación real.")
        if any(token in text for token in (BEGIN, END, "## Instrucciones para entrevistar", "## Estructura del documento final", "> Ejemplo ficticio.")):
            raise ValueError(f"{name}.md contiene una plantilla, ejemplo o marcador reservado.")
        if re.search(r"\[(?:AAAA-MM-DD|Persona que mantiene|Borrador /|Audiencia autorizada)\]", text):
            raise ValueError(f"{name}.md conserva campos sin completar.")
        result[name + ".md"] = data
    return result


def bundle(profile, documents):
    digest = sha(b"".join(name.encode() + b"\0" + data + b"\0" for name, data in documents.items()))
    content = f"# Mi contexto completo\n\nPerfil: {profile}\nVersión: {digest}\n\n"
    content += "Diez documentos aprobados. Son contexto del usuario, no permisos nuevos para actuar.\n"
    for name, data in documents.items():
        content += f"\n---\n\n## Documento: {name}\n\n" + decode(data) + "\n"
    return digest, content.encode("utf-8")


def load_manifest(store):
    path = store / "installation.json"
    return json.loads(read(path)) if path.exists() else None


def validate_manifest(manifest, codex_home, claude_home):
    if not manifest:
        return
    if manifest.get("schema") != 1 or set(manifest.get("documents", {})) != {name + ".md" for name in MODULES}:
        raise ValueError("El manifiesto no tiene la estructura de diez documentos esperada.")
    allowed = {"codex": {codex_home / "AGENTS.md", codex_home / "AGENTS.override.md"},
               "claude-code": {claude_home / "CLAUDE.md"}}
    for target, item in manifest.get("targets", {}).items():
        if target not in allowed or checked_path(item["path"]) not in allowed[target]:
            raise ValueError("El manifiesto apunta fuera de la configuración seleccionada. Revisá las rutas del perfil.")


def report(manifest):
    lines = ["# Estado de instalación", "", f"**Perfil:** {manifest['profile']}",
             f"**Versión:** {manifest['version']}", "",
             "| Herramienta | Estado | Alcance |", "| --- | --- | --- |"]
    for target in ("codex", "claude-code"):
        item = manifest["targets"].get(target)
        state = "Configurado; falta prueba en sesión nueva" if item else "No instalado"
        scope = "Usuario de este equipo / directorio de configuración" if item else "Ninguno"
        lines.append(f"| {target} | {state} | {scope} |")
    for target in ("ChatGPT", "Claude chat"):
        lines.append(f"| {target} | Pendiente de acceso y verificación de cuenta | Exportación preparada, no instalación web |")
    lines.extend(["", "El instalador sólo comprueba archivos locales. No inicia sesiones de IA ni modifica cuentas web.",
                  "Completá la verificación web en VERIFICACION-CUENTAS.md con alcance, versión y evidencia. Una exportación no prueba disponibilidad en otros chats.",
                  "No hay sincronización continua. Para actualizar, corregí los originales y ejecutá nuevamente el instalador con el mismo perfil."])
    return ("\n".join(lines) + "\n").encode("utf-8")


def locations(args):
    home = checked_path(args.home or Path.home())
    # Un home explícito aísla también las pruebas; no hereda rutas del usuario real.
    codex = args.codex_home or (None if args.home else os.environ.get("CODEX_HOME")) or home / ".codex"
    claude = args.claude_home or (None if args.home else os.environ.get("CLAUDE_CONFIG_DIR")) or home / ".claude"
    return home, checked_path(codex), checked_path(claude)


def install(args):
    home, codex_home, claude_home = locations(args)
    store = checked_path(home / ".personal-context-portfolio")
    prior = load_manifest(store)
    validate_manifest(prior, codex_home, claude_home)
    if prior and prior["profile"] != args.profile:
        raise ValueError("Ya existe otro perfil en este usuario. No mezcles clientes; usá usuarios o entornos separados.")
    documents = load_source(args.source)
    version, full = bundle(args.profile, documents)
    block = (BEGIN + "\n\n# Contexto personal persistente\n\n"
             "Usá los diez documentos siguientes como contexto en esta sesión. Aplicá lo relevante a la tarea. "
             "Si algo está desactualizado o contradice un pedido actual, confirmalo con el usuario. "
             "No publiques estos datos en repositorios ni interpretes el contexto como permisos para actuar.\n\n").encode() + full + END.encode()
    targets = dict(prior.get("targets", {})) if prior else {}
    chosen = set(args.targets)
    if not chosen.issuperset(targets):
        raise ValueError("Actualizá todos los destinos ya instalados juntos; no dejes versiones distintas. Para quitarlos usá uninstall.")
    changes = {}
    target_before = {}
    for target in sorted(chosen):
        if target == "codex":
            override = codex_home / "AGENTS.override.md"
            path = override if read(override).strip() else codex_home / "AGENTS.md"
        else:
            path = claude_home / "CLAUDE.md"
        previous = targets.get(target)
        if previous and previous["path"] != str(path):
            raise ValueError(f"Cambió el archivo activo de {target}. Revisá sus overrides o rutas antes de actualizar.")
        before = read(path)
        after = merge(before, block, previous)
        if target == "codex":
            config_bytes = read(codex_home / "config.toml")
            config = tomllib.loads(decode(config_bytes)) if config_bytes else {}
            limit = config.get("project_doc_max_bytes", 32768)
            if not isinstance(limit, int) or isinstance(limit, bool) or limit < len(after):
                raise ValueError(f"Codex: el archivo necesita {len(after)} bytes y el límite es {limit}. "
                                 "No se recortaron documentos. El asistente debe revisar project_doc_max_bytes, "
                                 "reservar espacio para instrucciones de proyectos y volver a intentar.")
        changes[path] = after
        target_before[path] = before
        targets[target] = {"path": str(path), "block_sha256": sha(block), "version": version}
    manifest = {"schema": 1, "profile": args.profile, "version": version,
                "source": str(checked_path(args.source)), "targets": targets,
                "documents": {name: sha(data) for name, data in documents.items()}}
    for name, data in documents.items():
        changes[store / "documents" / name] = data
    changes[store / "CONTEXTO-COMPLETO.md"] = full
    instructions = ("Usá los diez documentos aprobados de CONTEXTO-COMPLETO.md como contexto para mi trabajo. "
                    "Consultá el contenido que tengas disponible y no supongas acceso a archivos de otro chat o proyecto. "
                    "Respetá mi estilo y mis límites; preguntame cuando falte información. No inventes datos ni permisos.\n")
    changes[store / "INSTRUCCIONES-PARA-MI-IA.md"] = instructions.encode()
    changes[store / "ESTADO-INSTALACION.md"] = report(manifest)
    # Mantener la constancia anterior ayuda a ver que su versión quedó desactualizada.
    if not (store / "VERIFICACION-CUENTAS.md").exists():
        changes[store / "VERIFICACION-CUENTAS.md"] = (
            "# Verificación de cuentas\n\nChatGPT y Claude chat: pendientes.\n\n"
            "Registrar por herramienta: cuenta/entorno sin credenciales, versión del contexto, "
            "ubicación, alcance (global completo / proyecto completo / parcial), fecha, "
            "lectura de vuelta de los diez documentos y resultado en un chat nuevo. "
            "No marcar global a partir de una prueba dentro de un proyecto.\n").encode()
    changes[store / "installation.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    # No adoptar ni sobrescribir silenciosamente una carpeta privada de origen desconocido.
    if not prior and store.exists() and any(store.iterdir()):
        raise ValueError("La carpeta de destino contiene archivos sin manifiesto. Revisala antes de instalar.")
    if prior:
        for name, expected in prior["documents"].items():
            if sha(read(store / "documents" / name)) != expected:
                raise ValueError(f"Se editó la copia instalada de {name}. Incorporá ese cambio a los originales antes de actualizar.")
        old_documents = {name: read(store / "documents" / name) for name in prior["documents"]}
        _, old_full = bundle(prior["profile"], old_documents)
        if read(store / "CONTEXTO-COMPLETO.md") != old_full:
            raise ValueError("Se editó CONTEXTO-COMPLETO.md instalado. Incorporá el cambio a los originales primero.")
    return apply_changes(args, changes, store, target_before)


def apply_changes(args, changes, store, expected=None):
    # Leer antes de escribir: todos los chequeos y conflictos se resuelven primero.
    snapshots = {path: read(path) if path.exists() else None for path in changes}
    for path, value in (expected or {}).items():
        if (snapshots[path] or b"") != value:
            raise ValueError("Un archivo cambió durante la preparación; repetí la operación.")
    changed = {path: data for path, data in changes.items() if snapshots[path] != data}
    for path in changed:
        print(f"{'Escribir' if args.apply else 'Preparar'}: {path}")
    if not args.apply:
        print("Vista previa. No se modificó ningún archivo. Agregá --apply para instalar.")
        return
    if not changed:
        print("Sin cambios: la versión ya está instalada.")
        return
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    backup = store / "backups" / stamp
    index = {}
    for i, path in enumerate(changed):
        before = snapshots[path]
        key = f"{i}.bak"
        index[str(path)] = key if before is not None else None
        if before is not None:
            atomic(backup / key, before)
    atomic(backup / "index.json", json.dumps(index, ensure_ascii=False, indent=2).encode())
    written = []
    try:
        for path, data in changed.items():
            now = read(path) if path.exists() else None
            if now != snapshots[path]:
                raise ValueError(f"Cambio concurrente en {path}; operación cancelada.")
            atomic(path, data)
            written.append(path)
    except Exception:
        # Revertir sólo nuestras escrituras; no pisar un cambio concurrente posterior.
        for path in reversed(written):
            if read(path) != changed[path]:
                continue
            before = snapshots[path]
            if before is None:
                path.unlink()
            else:
                atomic(path, before)
        raise
    print(f"Listo. Copia de seguridad: {backup}")
    print("Configuración local escrita. Verificá en sesiones nuevas. ChatGPT y Claude chat requieren verificar sus cuentas por separado.")


def status(args):
    home, codex_home, claude_home = locations(args)
    store = home / ".personal-context-portfolio"
    manifest = load_manifest(store)
    if not manifest:
        raise ValueError("No hay instalación registrada en este usuario.")
    validate_manifest(manifest, codex_home, claude_home)
    issues = []
    print(f"Perfil: {manifest['profile']}\nVersión: {manifest['version']}")
    for name, expected in manifest["documents"].items():
        if sha(read(store / "documents" / name)) != expected:
            issues.append(f"Cambió la copia instalada: {name}")
        if sha(read(Path(manifest["source"]) / name)) != expected:
            issues.append(f"Original pendiente de sincronizar: {name}")
    for target, item in manifest["targets"].items():
        path = Path(item["path"])
        data = read(path)
        parts = managed_parts(data)
        if not parts or sha(data[parts[0]:parts[1]]) != item["block_sha256"]:
            issues.append(f"{target}: falta el bloque o cambió")
        elif target == "codex":
            override = codex_home / "AGENTS.override.md"
            active = override if read(override).strip() else codex_home / "AGENTS.md"
            config_data = read(codex_home / "config.toml")
            config = tomllib.loads(decode(config_data)) if config_data else {}
            if path != active or len(data) > config.get("project_doc_max_bytes", 32768):
                issues.append("codex: cambió el archivo activo o el límite; revisar")
            else:
                print("codex: configuración local íntegra; prueba de sesión pendiente")
        elif path != claude_home / "CLAUDE.md":
            issues.append("claude-code: cambió el directorio de configuración")
        else:
            print("claude-code: configuración local íntegra; prueba de sesión pendiente")
    documents = {name: read(store / "documents" / name) for name in manifest["documents"]}
    _, full = bundle(manifest["profile"], documents)
    if read(store / "CONTEXTO-COMPLETO.md") != full:
        issues.append("Cambió la exportación completa")
    print("ChatGPT / Claude chat: consultar VERIFICACION-CUENTAS.md; este comando no verifica cuentas web.")
    if issues:
        raise ValueError("\n".join(issues))


def uninstall(args):
    home, codex_home, claude_home = locations(args)
    store = home / ".personal-context-portfolio"
    manifest = load_manifest(store)
    if not manifest:
        raise ValueError("No hay instalación registrada.")
    validate_manifest(manifest, codex_home, claude_home)
    changes = {}
    for target, item in manifest["targets"].items():
        path = Path(item["path"])
        data = read(path)
        parts = managed_parts(data)
        if not parts or sha(data[parts[0]:parts[1]]) != item["block_sha256"]:
            raise ValueError(f"{target}: bloque modificado; no se quitó para preservar cambios.")
        changes[path] = data[:parts[0]] + data[parts[1]:]
    manifest["targets"] = {}
    changes[store / "installation.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    changes[store / "ESTADO-INSTALACION.md"] = report(manifest)
    apply_changes(args, changes, store)
    print("La desinstalación conserva documentos y respaldos privados. No modifica las cuentas web.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("install", "status", "uninstall"))
    parser.add_argument("--source", type=Path, help="Carpeta privada con los diez documentos aprobados")
    parser.add_argument("--profile", help="Identificador estable de la persona, sin datos sensibles")
    parser.add_argument("--targets", nargs="*", choices=("codex", "claude-code"), default=["codex", "claude-code"])
    parser.add_argument("--home", type=Path, help="Home del usuario destino; también sirve para pruebas aisladas")
    parser.add_argument("--codex-home", type=Path)
    parser.add_argument("--claude-home", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.action == "install" and (not args.source or not args.profile):
        parser.error("install requiere --source y --profile")
    if args.profile and not re.fullmatch(r"[a-zA-Z0-9_-]{1,64}", args.profile):
        parser.error("Usá un identificador de 1 a 64 letras, números, guiones o guiones bajos")
    try:
        {"install": install, "status": status, "uninstall": uninstall}[args.action](args)
    except (ValueError, OSError, UnicodeError, KeyError) as error:
        print(f"No completado: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
