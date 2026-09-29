"""Reúne las instrucciones y plantillas en un archivo compartible con una IA.

Uso: python scripts/build-ai-starter.py [--check]
"""

from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
MODULES = (
    "identity",
    "role-and-responsibilities",
    "current-projects",
    "team-and-relationships",
    "tools-and-systems",
    "communication-style",
    "goals-and-priorities",
    "preferences-and-constraints",
    "domain-knowledge",
    "decision-log",
)


def nested_headings(text):
    """Baja los títulos de sección sin modificar los documentos de ejemplo."""
    in_fence = False
    lines = []
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and re.match(r"^#{1,4} ", line):
            line = "##" + line
        lines.append(line)
    return "\n".join(lines)


def build():
    intro = (ROOT / "interview-protocol/repo-setup.md").read_text(encoding="utf-8").strip()
    intro = intro.replace("(../INSTALACION.md)", "(INSTALACION.md)").replace("(../scripts/", "(scripts/")
    protocol = (ROOT / "interview-protocol/agent-system-prompt.md").read_text(encoding="utf-8")
    # La introducción del protocolo separado pide adjuntar plantillas: aquí ya están.
    protocol = protocol.split("\n---\n", 1)[1].strip().replace("../templates/", "templates/")
    parts = [
        intro,
        "---\n\n## Protocolo de entrevista\n\n" + nested_headings(protocol),
        "---\n\n## Las diez plantillas completas\n\nAplicá cada plantilla desde este archivo; no hace falta abrir enlaces adicionales.",
    ]
    for name in MODULES:
        template = (ROOT / "templates" / f"{name}.md").read_text(encoding="utf-8").strip()
        parts.append(f"---\n\n**Plantilla incluida: `{name}.md`**\n\n" + nested_headings(template))
    installation = (ROOT / "INSTALACION.md").read_text(encoding="utf-8").strip()
    parts.append("---\n\n## Procedimiento de instalación completo\n\n" + nested_headings(installation))
    parts.append("<!-- FIN DEL KIT DE INICIO -->")
    parts.append("Este archivo se genera con `python scripts/build-ai-starter.py` a partir de `interview-protocol/repo-setup.md`, el protocolo, las plantillas e `INSTALACION.md`. Editá esas fuentes para mantenerlo actualizado.")
    return "\n\n".join(parts) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Comprueba que el archivo generado coincida con las fuentes.")
    args = parser.parse_args()
    target = ROOT / "INICIAR-CON-IA.md"
    content = build()
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            raise SystemExit("INICIAR-CON-IA.md necesita regenerarse.")
        print("OK: guia completa y sincronizada con las diez plantillas.")
    else:
        target.write_text(content, encoding="utf-8")
        print("INICIAR-CON-IA.md generado.")
