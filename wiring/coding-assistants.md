# Instalación en Codex y Claude Code

El asistente puede configurar los diez documentos completos para las sesiones nuevas del usuario en este equipo. El [procedimiento de instalación](../INSTALACION.md) cubre detección de rutas, preservación de instrucciones, respaldos, límites de tamaño y verificación.

El cliente puede pedir:

> Instalá mi contexto aprobado en Codex y Claude Code. Hacé vos la configuración que puedas, conservá mis instrucciones existentes y verificá el resultado en una sesión nueva. Si algo requiere un permiso, indicame la acción concreta.

Los originales deben estar en una carpeta privada fuera del repositorio. El asistente usa [el instalador local](../scripts/install-context.py); no necesita que el cliente copie comandos. La instalación aplica al equipo y directorios configurados, no a cuentas web, otros equipos, máquinas remotas o sesiones que tengan deshabilitada la carga correspondiente.

Para actualizar, pedí «Actualizá mi contexto en todas mis herramientas». Para quitarlo, pedí «Retirá los bloques de este kit y conservá mis demás instrucciones». El estado local y las copias de seguridad quedan en `~/.personal-context-portfolio/`.

No se instala automáticamente el contexto al leer este repositorio: primero hay que completar y aprobar los diez documentos.
