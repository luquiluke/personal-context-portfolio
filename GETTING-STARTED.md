# Empezá por acá

## Opción recomendada: pedile a la IA que lo arme con vos

1. Abrí una conversación nueva en ChatGPT, Claude, Claude Code o Codex.
2. Copiá y pegá el [mensaje de inicio del repositorio](README.md#dejá-que-la-ia-te-guíe).
3. Respondé las preguntas, de a una. La IA prepara cada documento y te lo muestra para que lo corrijas.
4. Aprobá los diez documentos. La IA configura automáticamente las herramientas a las que tenga acceso, conservando tus instrucciones previas.
5. Revisá el estado final: qué quedó instalado, dónde están disponibles los diez documentos y qué necesita un paso tuyo. Probalo en una sesión nueva.

El enlace apunta a [INICIAR-CON-IA.md](INICIAR-CON-IA.md): un único archivo con entrevista, diez plantillas y procedimiento de instalación. La IA no necesita usar los perfiles ficticios como información sobre vos. El instalador local se obtiene por separado desde el repositorio cuando hace falta; el asistente se ocupa de ese paso.

### Si la IA no puede abrir el enlace

Abrí [el archivo de inicio en GitHub](https://github.com/luquiluke/personal-context-portfolio/blob/main/INICIAR-CON-IA.md), usá **Download raw file** y adjuntalo al chat. Si no podés adjuntar archivos, abrí la vista **Raw**, copiá el texto y pegalo. Agregá:

> Este es el archivo de inicio del kit. Usalo para guiarme y armar mis documentos. Empezá por preguntarme a qué me dedico.

Si el chat limita el tamaño del mensaje, pegalo en partes numeradas y pedile que espere hasta que escribas «Ya envié la guía completa». No necesitás descargar todo el repositorio ni conectar tu cuenta de GitHub.

### Qué hace la IA y qué hacés vos

La IA organiza la entrevista, redacta, incorpora tus correcciones y prepara los diez archivos completos. Vos aportás los datos y aprobás los documentos. Después configura cada herramienta accesible y preserva lo que ya tenías. Si necesita un permiso del sistema o un paso en tu cuenta, te indica exactamente qué hacer.

En Codex y Claude Code, la instalación local deja el contexto en instrucciones globales para nuevas sesiones del mismo usuario y entorno, sujeto a sus límites. En ChatGPT y Claude chat, depende de lo que permita la cuenta: si sólo se pueden conservar los archivos dentro de un proyecto, la IA debe indicarlo como tal. **Eso no equivale a tener los diez documentos en cualquier chat.** El contenido íntegro se conserva; no se resume para simular cobertura universal.

Si empezaste en un chat sin acceso a tu computadora, la IA prepara un traspaso a Codex o Claude Code con tus archivos para completar la instalación local sin rehacer la entrevista. Si no usás asistentes locales, no necesitás instalarlos: se registra que esos destinos no se usan.

Recibís los diez originales, un archivo combinado, instrucciones de uso y un estado por herramienta. Podés decir «pausamos acá» para recibir el avance; no se marcarán como instalados los documentos que falten.

### Actualizaciones a pedido

Cuando cambie algo, escribí: **«Actualizá mi contexto en todas mis herramientas con estos cambios: […]»**. La IA revisa los cambios con vos, actualiza las instalaciones accesibles y señala las pendientes. No tenés que volver a responder toda la entrevista ni configurar una sincronización continua. El [procedimiento de instalación](INSTALACION.md) también explica cómo recuperar o quitar la configuración.

## Opción manual: trabajá plantilla por plantilla

Elegí una tarea en la que quieras recibir mejor ayuda: responder una consulta, preparar una propuesta o acomodar tu semana. Ese caso te va a servir para probar el resultado.

## 1. Prepará tu carpeta privada

Creá una carpeta llamada `mi-contexto` fuera de este repositorio público. Si acompañás a varios clientes, usá una carpeta independiente para cada uno y compartila sólo con las personas que corresponda. No mezcles sus respuestas.

No necesitás una cuenta de GitHub: podés abrir las plantillas desde los enlaces y copiar su contenido. Si preferís descargarlas juntas, usá **Code → Download ZIP** en el repositorio y descomprimí el archivo.

## 2. Completá los diez documentos

Podés empezar por estas plantillas y continuar con los demás módulos de la tabla del paso 4. La instalación completa necesita los diez documentos aprobados:

1. [Identidad y actividad](templates/identity.md).
2. [Estilo de comunicación](templates/communication-style.md).
3. [Preferencias y límites](templates/preferences-and-constraints.md).

Copiá una plantilla completa en una conversación con la IA que uses y agregá:

> Ayudame a completar esta plantilla. Hablame de vos, en español rioplatense. Haceme una pregunta por vez y usá ejemplos de mi actividad. No inventes respuestas: si falta un dato, dejalo como «Por confirmar». Mostrame el borrador para que lo corrija antes de darlo por terminado.

Respondé como hablarías con alguien que recién empieza a trabajar con vos. Usá alias para clientes y ejemplos sin datos sensibles. Podés saltear una pregunta o pausar cuando quieras.

Leé el borrador: corregí lo que no te represente, verificá los datos y aprobá la versión final. Guardá **sólo el documento resultante**, sin las preguntas de la plantilla, con el nombre indicado, por ejemplo `identity.md`. Un editor de texto común alcanza; verificá que no termine en `.md.txt`.

También podés completar la estructura a mano. No hace falta una entrevista con IA.

## 3. Probalo con trabajo real

Adjuntá los archivos aprobados a un chat nuevo o pegá su contenido. Pedile:

> Usá mi contexto para redactar una respuesta a esta consulta: [pegá una consulta anonimizada]. Dejá como pendientes los precios, plazos o condiciones que no estén confirmados. Prepará un borrador para revisar.

Comprobá si suena como vos, entiende qué ofrecés y respeta tus límites. Si falla, corregí el archivo correspondiente y repetí la prueba. Esta prueba de uso no reemplaza verificar la instalación en sesiones nuevas.

## 4. Completá el resto según tu actividad

| Si necesitás… | Sumá… |
| --- | --- |
| Organizar tu carga de trabajo | [Responsabilidades](templates/role-and-responsibilities.md) y [proyectos](templates/current-projects.md) |
| Coordinar con otras personas | [Equipo y vínculos](templates/team-and-relationships.md) |
| Encontrar la fuente correcta de información | [Herramientas](templates/tools-and-systems.md) |
| Ordenar prioridades y evaluar alternativas | [Objetivos](templates/goals-and-priorities.md) y [decisiones](templates/decision-log.md) |
| Darle criterio del rubro a la IA | [Conocimiento del rubro](templates/domain-knowledge.md) |

Para una entrevista completa, copiá las [instrucciones del entrevistador](interview-protocol/agent-system-prompt.md) junto con las diez plantillas. Podés dividirla en varias sesiones; al terminar, pedí un resumen de avance para retomar. Este kit no incluye una aplicación web ni guarda automáticamente tu progreso.

## 5. Usalo donde ya trabajás

Pedile a la IA que siga la [guía de instalación](INSTALACION.md) con los diez archivos aprobados. La [guía de conexión](wiring/README.md) incluye las rutas de uso y opciones de integración.

## 6. Mantenelo al día

- **Cada semana:** actualizá estados, fechas y próximos pasos de trabajos activos.
- **Cada mes:** revisá prioridades, capacidad disponible y decisiones abiertas.
- **Cuando cambie algo:** actualizá servicios, personas, herramientas o condiciones comerciales.

En cada documento anotá responsable, fecha, estado y quién puede verlo. Usá `AAAA-MM-DD` para evitar confusiones de fecha, la moneda explícita (`ARS`, `USD`, etc.) para importes y la zona horaria cuando importe. Si un valor no está confirmado, no lo completes por intuición.

Una copia adjuntada o pegada no se actualiza sola. Pedí a la IA que aplique la nueva versión en todas tus herramientas y conserve el registro de los destinos pendientes. Los respaldos permiten revisar y recuperar cambios anteriores.
