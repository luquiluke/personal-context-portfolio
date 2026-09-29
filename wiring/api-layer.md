# Integración opcional: diseñar una API de contexto

Una API es una interfaz para que una aplicación consulte información de otro sistema. Esta opción tiene sentido cuando estás construyendo una aplicación propia que necesita contexto de varios usuarios o clientes. Para usar el kit en un chat no hace falta.

Esta es una propuesta de diseño, no una API implementada en el repositorio.

## Versión mínima

Guardá por documento: identificador de cliente, nombre permitido, contenido, versión, fecha de actualización y estado de aprobación. Publicá sólo las versiones aprobadas para la audiencia correspondiente.

Estas rutas son ilustrativas:

```text
GET /api/context/identity
GET /api/context/current-projects
GET /api/context/communication-style
```

El servidor debe obtener el cliente autorizado a partir de la sesión o credencial validada. No alcanza con aceptar un identificador de cliente enviado por quien hace la consulta.

## Comportamiento esperado

- Autenticar cada solicitud y comprobar permisos sobre cada documento.
- Usar una lista de nombres permitidos; no convertir un parámetro libre en una ruta de archivos.
- Devolver el texto Markdown con su versión y fecha para poder identificar el contexto usado.
- Evitar registrar contenido sensible en los registros técnicos del servicio.
- Aislar almacenamiento, caché y acceso entre clientes.
- Mantener historial para recuperar una versión anterior.

## Cambios propuestos por la IA

Empezá con lectura. Si más adelante necesitás escritura, guardá los cambios como propuestas pendientes de revisión. Usá control de versiones para detectar si otro usuario modificó el documento desde que se leyó; no sobrescribas silenciosamente la versión nueva.

## Validación para una implementación futura

Comprobá solicitudes sin credenciales, acceso cruzado entre dos clientes de prueba, nombres de archivo no permitidos, documentos no aprobados y versiones desactualizadas. Si usás una base de datos con políticas por fila, configurá y verificá esas políticas explícitamente; no asumas que el aislamiento aparece por guardar un identificador de usuario.

Elegí framework, alojamiento y autenticación según el producto y el soporte disponible. Este kit no necesita una base de datos para cumplir su función inicial.
