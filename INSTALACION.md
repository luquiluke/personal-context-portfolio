# Instalación de contexto persistente en tus cuatro herramientas

**Decisión de esta edición:** conservar los diez documentos completos, configurar una vez por herramienta y actualizar cuando lo pidas. El asistente hace las operaciones a las que tenga acceso; vos aportás y aprobás tu contexto.

## Qué significa «en todas partes»

El kit busca la cobertura más amplia posible en ChatGPT, Claude, Claude Code y Codex. No hay una instalación única que convierta automáticamente archivos locales en memoria íntegra de todas las cuentas web. Por eso la entrega incluye un estado por herramienta y distingue **contexto completo instalado**, **disponible sólo en un proyecto**, **parcial** y **pendiente**.

| Herramienta | Método del kit | Alcance que se puede verificar |
| --- | --- | --- |
| Codex | Incorporar los diez documentos al archivo global activo de instrucciones | Sesiones nuevas que usen ese usuario y directorio de configuración; sujeto al límite de lectura y a instrucciones de cada proyecto |
| Claude Code | Incorporar los diez documentos a las instrucciones del usuario | Sesiones nuevas en ese equipo y configuración, sujetas a sus políticas y mecanismos de carga |
| ChatGPT | Intentar configuración de cuenta con el contenido íntegro donde esté soportado; mantener copia completa en un proyecto privado | Alcance real de la cuenta; una copia en un proyecto sólo cubre ese proyecto |
| Claude chat | Intentar instrucciones de perfil con el contenido íntegro cuando lo admita; mantener copia completa en un proyecto privado | Alcance real del perfil; conocimiento de proyecto no equivale a memoria global |

La memoria automática puede resumir o seleccionar información. No la usamos como prueba de conservación íntegra de diez documentos. Tampoco consideramos que un enlace o una ruta local en instrucciones globales dé acceso a su contenido. Las sesiones temporales, los entornos remotos y las políticas de una organización pueden tener otros límites. Consultá las [fuentes de alcance](wiring/capabilities.md).

## Instrucciones para el asistente instalador

### 1. Preparar la fuente aprobada

Completá los diez módulos. Un módulo que no corresponda puede decir «No aplica», con aprobación de la persona; no lo inventes ni lo omitas silenciosamente. Guardá cada archivo con sus metadatos y la línea `**Estado:** Aprobado por el responsable` sólo después de esa aprobación. No instales plantillas, entrevistas ni ejemplos ficticios.

Elegí una carpeta privada fuera del repositorio público como fuente. Usá un identificador estable para esa persona, sin datos sensibles. Un usuario de sistema sólo debe tener un perfil global activo; no mezcles clientes de una consultora en el mismo perfil global.

Preguntá qué herramientas usa y detectá el equipo o entorno cuando tengas acceso. Los cuatro destinos están soportados por el flujo; no instales aplicaciones que la persona no utiliza. Si empieza en un chat sin acceso al equipo, terminá la entrevista y prepará la entrega completa antes de pedirle abrir un asistente con acceso local. Que ChatGPT o Claude puedan generar archivos en su entorno de ejecución no significa que puedan escribir en la computadora del usuario.

### 2. Instalar automáticamente en Codex y Claude Code

Si tenés acceso real al equipo de la persona, leé y ejecutá [scripts/install-context.py](scripts/install-context.py). Usá Python 3.11 o posterior disponible en ese entorno. No ejecutes el instalador en un contenedor de análisis y lo describas como una instalación en la computadora del cliente. Si falta el runtime, usá las herramientas de archivos del asistente siguiendo las mismas reglas de preservación y verificación, o indicá el requisito pendiente.

Ejemplo para el asistente técnico; reemplazá la ruta por la carpeta privada real:

```text
python scripts/install-context.py install --source RUTA_PRIVADA --profile mi-contexto
python scripts/install-context.py install --source RUTA_PRIVADA --profile mi-contexto --apply
python scripts/install-context.py status
```

El primer comando muestra qué cambiará. Si el usuario ya pidió instalar, continuá con `--apply` dentro de los permisos disponibles; no conviertas la vista previa en una confirmación adicional. Respetá cualquier aprobación que exija el entorno. Nunca cambies políticas de seguridad para evitarla.

Por defecto se configuran ambos asistentes locales. `--targets codex` o `--targets claude-code` permite elegir uno. `--targets` sin valores prepara únicamente la carpeta y exportaciones. `--home` permite indicar explícitamente el usuario destino o un entorno de prueba; `--codex-home` y `--claude-home` permiten rutas particulares. No escribas en otro usuario por suposición.

El instalador:

- Conserva completos los diez originales y crea `CONTEXTO-COMPLETO.md` sin resumirlos.
- Usa `CODEX_HOME` y `CLAUDE_CONFIG_DIR` si están definidos; de lo contrario, las ubicaciones habituales del usuario. Si hay un override global activo de Codex, lo detecta.
- Agrega un bloque identificado a las instrucciones existentes. Mantiene el resto, hace respaldos y evita duplicar el bloque al repetir la operación.
- Rechaza plantillas, perfiles diferentes, cambios concurrentes y modificaciones externas en sus bloques o copias de contexto.
- Comprueba el tamaño para Codex. Si no entra, detiene la operación antes de escribir; nunca recorta módulos. Revisá el límite `project_doc_max_bytes` y el espacio necesario para instrucciones de proyectos. Si corresponde y está autorizado, ajustá sólo ese valor preservando el resto de la configuración y repetí la instalación. Una configuración de cuenta, perfil o comando puede modificar el límite efectivo: verificá la sesión real.
- No cambia archivos internos de memoria generada, credenciales, permisos de ejecución ni políticas de las aplicaciones.

Los archivos privados quedan bajo `~/.personal-context-portfolio/`, junto con respaldos, manifiesto, instrucciones para la IA y estado local. Es una carpeta local, no almacenamiento cifrado ni una conexión con cuentas web; conserva los controles de acceso del usuario de sistema.

### 3. Configurar ChatGPT y Claude chat con el acceso disponible

Hacé este procedimiento por separado en cada cuenta que la persona use:

1. **Comprobar acceso.** Si disponés de interfaz, conector o herramienta autorizada para administrar esa cuenta, inspeccioná las opciones reales. Si no, prepará los archivos y un único paso concreto para que el usuario continúe. No solicites contraseñas ni tokens por chat, ni uses endpoints privados no documentados.
2. **Preservar lo existente.** Leé y guardá una copia de instrucciones previas antes de cambiarlas. Conservá cualquier instrucción ajena al bloque del kit; no reemplaces todo el campo ni restablezcas la memoria de la cuenta.
3. **Intentar alcance global completo.** Usá el campo de instrucciones globales o de perfil si acepta el contenido completo junto con lo existente. Guardá y leé de vuelta el contenido; verificá los diez módulos y que no se haya truncado. Si la cuenta ofrece una fuente privada conectada accesible desde sus chats, puede ser otra ruta, pero verificá acceso autenticado y alcance en chats nuevos antes de declararla disponible. No hagas públicos los documentos para que una URL sea accesible.
4. **Si no admite el contenido íntegro, mantenerlo completo.** Creá o actualizá un proyecto privado «Mi contexto» con `CONTEXTO-COMPLETO.md` y las instrucciones de uso. Un archivo combinado evita depender de poder adjuntar diez archivos separados. No conviertas el portfolio en un resumen para simular que cumple el requisito. Registrá **proyecto completo; global pendiente/no soportado en esta configuración**. No declares instalado globalmente un simple recordatorio para abrir el proyecto.
5. **Memoria nativa.** Sólo incorporá información aprobada mediante controles disponibles si sirve como complemento. No la confundas con conservar archivos textuales ni prometas que su mecanismo de recuperación usará todos los datos. No borres recuerdos ajenos al kit.
6. **Comprobar y registrar.** Indicá cuenta o entorno sin credenciales, ubicación, versión, fecha, alcance y evidencia de lectura. Guardá esos resultados en `VERIFICACION-CUENTAS.md`; el instalador local deja esa verificación pendiente porque no tiene acceso a cuentas.

Si necesitás acciones manuales, agrupalas por herramienta y prepará previamente todo el texto. El cliente no tiene que elegir archivos, escribir comandos ni diseñar la configuración. Evitá repetir pasos ya completados.

### 4. Verificar en sesiones nuevas

La escritura correcta de archivos no prueba que una aplicación ya los esté usando. Abrí una sesión nueva con herramientas autorizadas o prepará un único pedido de prueba para el usuario:

> Sin usar esta conversación anterior, indicá qué versión de mi contexto tenés disponible. Nombrá los diez documentos y mencioná un dato concreto de cada uno. Señalá si alguno no está disponible. No inventes lo que falta.

Compará la respuesta con los originales. Para alcance global en chat, probá una conversación nueva fuera del proyecto y verificá también el alcance documentado del mecanismo. Una respuesta acertada aislada no garantiza todos los modos o futuras sesiones. Para asistentes locales, probá desde otra carpeta y revisá que las instrucciones globales estén activas. Si no podés abrir una sesión o leer de vuelta el estado, registrá **configurado; verificación pendiente**.

Entregá una tabla con las cuatro herramientas, estado, alcance, versión y acción pendiente. No cierres con «memoria universal instalada» cuando alguna fila sea parcial o pendiente. Los documentos completos siguen siendo el objetivo, no una promesa sobre plataformas fuera de tu control.

## Actualizar cuando la persona lo pida

Pedido sugerido:

> Actualizá mi contexto en todas mis herramientas con estos cambios: […]. Conservá los diez documentos completos y decime dónde quedó aplicada la nueva versión.

Revisá el cambio con la persona, actualizá los originales y repetí el instalador con el mismo perfil y todos los destinos locales ya instalados. Después reemplazá la versión en cada cuenta a la que tengas acceso. Un cambio local no modifica ChatGPT ni Claude chat: las verificaciones web de una versión anterior quedan desactualizadas hasta repetirlas.

Si no podés acceder a un destino, actualizá los demás y dejá esa fila como **actualización pendiente**, con el siguiente paso listo. No programes sincronización continua ni tareas en segundo plano.

## Desinstalar y recuperar

```text
python scripts/install-context.py uninstall
python scripts/install-context.py uninstall --apply
```

Se retiran sólo los bloques locales del kit, conservando otras instrucciones, documentos privados y respaldos. Si un bloque fue modificado por fuera, la desinstalación se detiene para que el asistente concilie los cambios. Las cuentas web se revisan por separado: quitá únicamente contenido del kit y preservá lo demás.

Cada respaldo tiene un `index.json` que relaciona la ruta original con su copia. Antes de recuperar una versión, comparala con la actual para no perder cambios posteriores. No copies archivos de configuración completos a ciegas.
