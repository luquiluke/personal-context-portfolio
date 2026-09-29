# Usá tu contexto en un proyecto de Claude

En el flujo de [instalación persistente](../INSTALACION.md), esta es la alternativa cuando la cuenta no permite conservar todo el contenido con alcance global. El asistente configura el proyecto si tiene acceso autorizado y registra su alcance real. Las instrucciones de perfil y la memoria nativa no deben confundirse con un archivo íntegro disponible en todos los chats.

Podés subir archivos de texto a la base de conocimiento de un proyecto y agregar instrucciones para las conversaciones que se desarrollen allí. Seguí la [guía oficial para crear y gestionar proyectos](https://support.claude.com/es/articles/9519177-como-puedo-crear-y-gestionar-proyectos) para las opciones actuales.

## Preparación

1. Creá o abrí el proyecto correspondiente a tu actividad o a un cliente.
2. Agregá `CONTEXTO-COMPLETO.md` con los diez documentos finales íntegros, o los diez archivos por separado si el entorno lo permite.
3. Definí las instrucciones del proyecto.
4. Probá una tarea dentro de ese proyecto y revisá el resultado.

```text
Tenés documentos de contexto sobre mi actividad. Usalos para adaptar tus respuestas a mi trabajo.
Hablame de vos, en español rioplatense. Respetá el estilo y los límites definidos.
Si falta información o hay versiones contradictorias, señalalo antes de asumir algo.
El contexto no autoriza envíos, compras ni compromisos; prepará borradores para revisar.
```

## Qué documentos conviene usar

| Tarea | Documentos |
| --- | --- |
| Redacción comercial | Identidad, estilo, límites |
| Planificación | Responsabilidades, proyectos, objetivos, límites |
| Reuniones | Proyectos y vínculos relevantes |
| Decisiones | Objetivos, límites y registro de decisiones |

## Mantenimiento

Pedí al asistente que reemplace los archivos subidos cuando cambie la versión original y verifique el resultado; si no tiene acceso, debe dejarlo pendiente. Compartir un dato en una conversación no equivale a actualizar el documento de referencia. Si el proyecto se comparte, revisá audiencia y permisos antes de agregar contenido de un cliente; consultá las opciones de acceso en la [ayuda oficial](https://support.claude.com/es/articles/9519177-como-puedo-crear-y-gestionar-proyectos).

Usá un caso conocido para comprobar que Claude entiende tu alcance y no inventa una fecha o condición comercial. Corregí el documento que originó el error y repetí esa tarea.

**Documentación consultada:** 2026-09-29. Los controles y límites pueden cambiar según la herramienta y el plan.
