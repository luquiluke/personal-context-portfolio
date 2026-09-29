# Detalle de esta adaptación

**Fecha:** 2026-09-29
**Origen:** [nlwhittemore/personal-context-portfolio](https://github.com/nlwhittemore/personal-context-portfolio)
**Edición:** español rioplatense, con voseo; sin marca comercial.

## Qué se conserva

La idea de una carpeta de contexto portable, los diez módulos, la entrevista con revisión del usuario y las rutas originales. La historia de Git permite consultar los textos originales y comparar futuras actualizaciones.

## Qué cambia

- Se traduce y adapta todo el contenido orientado al usuario: presentación, inicio, diez plantillas, protocolo, guías y treinta archivos de ejemplo.
- Se incorporan servicios, clientes, propuestas, capacidad, cobros, proveedores y operaciones cotidianas.
- Se reemplazan los casos tecnológicos y corporativos por tres casos ficticios: profesional independiente, pyme de servicios y comercio.
- Se agrega una ruta inicial de tres documentos y una guía para consultores.
- Se eliminan las referencias a una aplicación web que el original no enlazaba ni incluía.
- Se agregan estado, fecha, responsable y audiencia para distinguir borradores de contexto aprobado.
- Se aclara que adjuntar archivos no los sincroniza y que el contexto no concede permisos para operar cuentas o enviar mensajes.
- Se agrega un mensaje de inicio para apuntar ChatGPT o Claude al repositorio y un [archivo único de configuración guiada](INICIAR-CON-IA.md) con entrevista, plantillas y entrega. Puede compartirse por enlace, adjunto o texto pegado.
- Se incorpora instalación persistente para ChatGPT, Claude, Claude Code y Codex, con los diez documentos completos y actualizaciones a pedido. El script instala instrucciones globales locales; las cuentas web se configuran con las herramientas autorizadas disponibles y se reportan sus límites reales.
- El instalador preserva instrucciones existentes, respalda cambios, comprueba tamaño, identifica conflictos y permite desinstalar sus bloques. No modifica la memoria generada interna de las herramientas ni declara cobertura universal a partir de una carga en un proyecto.

## Mantener la guía de inicio para IA

`INICIAR-CON-IA.md` reúne las [instrucciones de configuración](interview-protocol/repo-setup.md), el protocolo de entrevista, las diez plantillas y [la instalación](INSTALACION.md). Después de editar esas fuentes, ejecutá `python scripts/build-ai-starter.py` desde la raíz del repositorio. Con `--check` podés comprobar que la versión compartible coincida con las fuentes.

El instalador usa Python 3.11 o posterior sin dependencias. Lo ejecuta el asistente en el equipo del cliente cuando dispone de acceso y runtime; la entrevista web no necesita Python. Las pruebas se ejecutan con `python -m unittest discover -s tests -v` en carpetas temporales, sin modificar el perfil real ni cuentas web.

## Correspondencia de ejemplos

| Carpeta original conservada | Caso de esta edición |
| --- | --- |
| `examples/knowledge-worker/` | Lucía: arquitecta independiente |
| `examples/executive/` | Martín: dueño de una pyme de mantenimiento |
| `examples/entrepreneur/` | Paula: dueña de una ferretería |

Son adaptaciones de las situaciones, no traducciones literales de las personas originales. Ningún caso representa a un cliente real. Los nombres técnicos de archivos y productos se conservan cuando ayudan a reutilizar el material.

## Licencia de origen

El README original declara MIT. Se mantiene la atribución y esa declaración, sin inventar un titular de derechos ni un texto de licencia ausente del origen.
