# Alcance verificado y fuentes

Revisión: 2026-09-29. Esta página fundamenta la instalación; no garantiza funciones que una cuenta, plan, política o versión no habilite.

## Codex

El mecanismo documentado de instrucciones globales usa el directorio de Codex y da prioridad a `AGENTS.override.md` sobre `AGENTS.md`. Hay un límite de lectura configurable; se debe comprobar que la cadena completa entre en él. El instalador usa un bloque con los diez documentos y no edita la memoria generada. Fuentes: [instrucciones con AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) y [memorias y almacenamiento local](https://learn.chatgpt.com/docs/customization/memories).

## Claude Code

Las instrucciones de usuario permiten proporcionar contexto entre proyectos del mismo entorno. El kit incorpora el texto íntegro en `CLAUDE.md`, preservando las instrucciones ajenas al kit. No depende de que un recordatorio haga que el modelo abra otro archivo. La carga real se verifica en una sesión nueva; no se asume propagación a otros equipos. Fuente: [cómo Claude Code recuerda el contexto](https://code.claude.com/docs/en/memory).

## ChatGPT

Las instrucciones personalizadas sirven para preferencias entre chats; los proyectos comparten archivos e instrucciones dentro de su ámbito. Estas fuentes no documentan una instalación local que publique automáticamente diez documentos íntegros como memoria de toda la cuenta. Por eso el flujo verifica la capacidad de la cuenta y reporta la limitación si sólo puede configurar un proyecto. Fuentes: [personalización](https://learn.chatgpt.com/docs/personalize) y [proyectos y chats](https://learn.chatgpt.com/docs/projects).

## Claude chat

Las instrucciones de perfil tienen alcance de cuenta; las de proyecto tienen alcance de proyecto. La memoria es una síntesis, con ámbitos diferenciados, y no prueba que se hayan conservado archivos completos. El flujo sólo declara cobertura global completa después de comprobar almacenamiento íntegro y alcance del mecanismo disponible. Fuentes: [personalización](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) y [búsqueda y memoria](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).

## Qué verificar cuando cambien las herramientas

Revisá estas fuentes y la cuenta real antes de cambiar las recetas. Conservá los diez originales; no reemplaces silenciosamente el requisito de contenido íntegro por un resumen. Disponibilidad, recuperación y obediencia son propiedades distintas: tener los documentos no garantiza que todas las respuestas usen todos sus datos.
