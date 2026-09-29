# Integración opcional: contexto para un agente OpenClaw

Usá esta guía si ya tenés OpenClaw configurado. Para empezar sin instalación, alcanza con los [pedidos para copiar y pegar](system-prompt-patterns.md).

OpenClaw utiliza un espacio de trabajo con archivos de contexto e instrucciones. Su documentación distingue el contexto del usuario (`USER.md`) de la identidad y el tono del agente (`SOUL.md`). Los archivos y sus límites de carga se explican en la [guía oficial del espacio de trabajo](https://docs.openclaw.ai/concepts/agent-workspace).

## Propuesta de organización

Conservá los diez documentos como fuente aprobada en una carpeta privada. En la configuración del agente, indicá qué archivos necesita para su tarea y dónde están. Si querés resumir información estable en `USER.md`, seguí el formato documentado para tu versión y mantené la referencia a la fuente.

No reemplaces `SOUL.md` con el perfil del cliente: describe al agente y cumple otra función. Antes de editar archivos de configuración existentes, revisá su contenido y preservá las instrucciones que correspondan.

## Ejemplo de instrucción para adaptar

```text
Para proponer el orden de trabajo de la semana, leé los archivos aprobados de responsabilidades,
proyectos, objetivos y límites en la carpeta de contexto autorizada.
Si no podés acceder a alguno, indicá cuál falta; no supongas su contenido.
Prepará una propuesta con próximos pasos y bloqueos. No modifiques la agenda ni envíes mensajes.
```

Es una propuesta de uso, no una configuración lista para ejecutar. La ruta, las herramientas de lectura y los permisos deben ajustarse a la instalación. No presupongas una conexión MCP disponible sin verificarla.

## Validación

Probá con una carpeta ficticia: confirmá que el agente pueda leer los archivos autorizados, que identifique su fecha y que no acceda al contexto de otros clientes. Cambiá un dato y comprobá que lo vuelva a consultar cuando corresponda.

Una copia resumida o pegada en instrucciones necesita mantenimiento separado. Que el original cambie no asegura que una sesión ya iniciada use el nuevo contenido.

**Documentación consultada:** 2026-09-29.
