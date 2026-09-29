# Integración opcional: compartir contexto mediante MCP

Esta guía es para quien configura herramientas de IA. Si sólo querés usar tus archivos, empezá por [copiar y pegar](system-prompt-patterns.md).

MCP es un protocolo para conectar aplicaciones con fuentes de datos y herramientas. Un servidor puede exponer archivos como recursos; el cliente determina cómo incorporarlos al contexto. No basta con que una aplicación diga que soporta MCP para asumir que puede usar cualquier recurso de la misma manera. Consultá la [especificación de recursos](https://modelcontextprotocol.io/specification/2025-06-18/server/resources).

## Diseño propuesto

1. Guardá una copia aprobada del contexto de cada cliente en su carpeta privada.
2. Definí una lista explícita de documentos que se pueden leer para cada tarea.
3. Elegí un servidor y un cliente que soporten el mecanismo elegido: recursos o herramientas de lectura.
4. Configurá autenticación y autorización para ese cliente o usuario, según el entorno.
5. Verificá que la aplicación reciba la versión esperada del archivo.

Los recursos pueden identificar, por ejemplo, identidad o proyectos activos. Sus identificadores y rutas dependen de tu implementación; este repositorio no ofrece un servidor ya desplegado.

## Recursos y herramientas no son lo mismo

El servidor de archivos de referencia ofrece herramientas para leer, pero también para escribir y mover archivos. Usarlo no implica tener un acceso de sólo lectura. Revisá su [documentación y herramientas disponibles](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md) y restringí efectivamente las operaciones que no necesites; un texto en el prompt no sustituye un control de acceso.

## Prueba antes de usar contexto real

Usá dos carpetas ficticias. Comprobá que una sesión autorizada para la primera no pueda consultar la segunda. Verificá que no pueda acceder a archivos fuera de la lista permitida ni modificar el contexto si el alcance acordado es lectura.

Actualizá un dato de prueba y volvé a pedir una lectura. El archivo nuevo sólo estará disponible cuando el servidor lo lea y el cliente lo solicite o actualice su copia. No supongas sincronización automática, ausencia de caché ni actualización retroactiva de conversaciones.

**Documentación consultada:** 2026-09-29. Implementación y configuración quedan a cargo del equipo técnico.
