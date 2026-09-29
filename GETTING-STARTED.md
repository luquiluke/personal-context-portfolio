# Empezá por acá

## Opción recomendada: pedile a la IA que lo arme con vos

1. Abrí una conversación nueva en ChatGPT o Claude.
2. Copiá y pegá el [mensaje de inicio del repositorio](README.md#dejá-que-la-ia-te-guíe).
3. Respondé las preguntas, de a una. La IA prepara cada documento y te lo muestra para que lo corrijas.
4. Al terminar, recibís tus archivos de contexto, instrucciones listas para tu asistente y una guía breve para usarlos.

El enlace apunta a [INICIAR-CON-IA.md](INICIAR-CON-IA.md): un único archivo con el proceso completo y las diez plantillas. La IA no necesita recorrer todas las carpetas ni usar los perfiles ficticios como información sobre vos.

### Si la IA no puede abrir el enlace

Abrí [el archivo de inicio en GitHub](https://github.com/luquiluke/personal-context-portfolio/blob/main/INICIAR-CON-IA.md), usá **Download raw file** y adjuntalo al chat. Si no podés adjuntar archivos, abrí la vista **Raw**, copiá el texto y pegalo. Agregá:

> Este es el archivo de inicio del kit. Usalo para guiarme y armar mis documentos. Empezá por preguntarme a qué me dedico.

Si el chat limita el tamaño del mensaje, pegalo en partes numeradas y pedile que espere hasta que escribas «Ya envié la guía completa». No necesitás descargar todo el repositorio ni conectar tu cuenta de GitHub.

### Qué hace la IA y qué hacés vos

La IA organiza la entrevista, redacta, incorpora tus correcciones y prepara la entrega. Vos aportás los datos y aprobás los documentos. Si puede generar archivos, te los entrega para descargar; si no, te da bloques de texto identificados para guardar.

Para usar el resultado en un proyecto de ChatGPT o Claude, normalmente vas a crear el proyecto, agregar los archivos y pegar las instrucciones que te prepare. La IA te guía en esos pasos; sólo puede realizarlos por vos si dispone de herramientas y permisos adecuados. Entregar un enlace al repositorio no crea por sí solo un proyecto ni una memoria permanente.

Podés decir «hagamos una versión breve» para empezar con identidad, estilo y límites, o «pausamos acá» para recibir tus documentos y un resumen que te permita retomar.

## Opción manual: trabajá plantilla por plantilla

Elegí una tarea en la que quieras recibir mejor ayuda: responder una consulta, preparar una propuesta o acomodar tu semana. Ese caso te va a servir para probar el resultado.

## 1. Prepará tu carpeta privada

Creá una carpeta llamada `mi-contexto` fuera de este repositorio público. Si acompañás a varios clientes, usá una carpeta independiente para cada uno y compartila sólo con las personas que corresponda. No mezcles sus respuestas.

No necesitás una cuenta de GitHub: podés abrir las plantillas desde los enlaces y copiar su contenido. Si preferís descargarlas juntas, usá **Code → Download ZIP** en el repositorio y descomprimí el archivo.

## 2. Armá los primeros tres documentos

Empezá por estas plantillas, en este orden:

1. [Identidad y actividad](templates/identity.md).
2. [Estilo de comunicación](templates/communication-style.md).
3. [Preferencias y límites](templates/preferences-and-constraints.md).

Copiá una plantilla completa en una conversación con la IA que uses y agregá:

> Ayudame a completar esta plantilla. Hablame de vos, en español rioplatense. Haceme una pregunta por vez y usá ejemplos de mi actividad. No inventes respuestas: si falta un dato, dejalo como «Por confirmar». Mostrame el borrador para que lo corrija antes de darlo por terminado.

Respondé como hablarías con alguien que recién empieza a trabajar con vos. Usá alias para clientes y ejemplos sin datos sensibles. Podés saltear una pregunta o pausar cuando quieras.

Leé el borrador: corregí lo que no te represente, verificá los datos y aprobá la versión final. Guardá **sólo el documento resultante**, sin las preguntas de la plantilla, con el nombre indicado, por ejemplo `identity.md`. Un editor de texto común alcanza; verificá que no termine en `.md.txt`.

También podés completar la estructura a mano. No hace falta una entrevista con IA.

## 3. Probalo con trabajo real

Adjuntá los tres archivos aprobados a un chat nuevo o pegá su contenido. Pedile:

> Usá mi contexto para redactar una respuesta a esta consulta: [pegá una consulta anonimizada]. Dejá como pendientes los precios, plazos o condiciones que no estén confirmados. Prepará un borrador para revisar.

Comprobá si suena como vos, entiende qué ofrecés y respeta tus límites. Si falla, corregí el archivo correspondiente y repetí la prueba. La IA no necesita saber todo sobre vos para ayudarte con una tarea concreta.

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

La [guía de conexión](wiring/README.md) explica cómo usar los archivos en un chat, en un proyecto de ChatGPT o Claude, o en una integración propia. Copiar y pegar alcanza para empezar.

## 6. Mantenelo al día

- **Cada semana:** actualizá estados, fechas y próximos pasos de trabajos activos.
- **Cada mes:** revisá prioridades, capacidad disponible y decisiones abiertas.
- **Cuando cambie algo:** actualizá servicios, personas, herramientas o condiciones comerciales.

En cada documento anotá responsable, fecha, estado y quién puede verlo. Usá `AAAA-MM-DD` para evitar confusiones de fecha, la moneda explícita (`ARS`, `USD`, etc.) para importes y la zona horaria cuando importe. Si un valor no está confirmado, no lo completes por intuición.

Una copia adjuntada o pegada no se actualiza sola: reemplazala cuando cambie el original. Conservá la última versión aprobada para poder recuperar un cambio equivocado.
