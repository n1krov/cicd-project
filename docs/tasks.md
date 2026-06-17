# Lista de Tareas de Implementación

## Fase 1: Infraestructura de Documentación y Gestión
- [x] Crear el tablero en Trello con las columnas To-Do, Haciendo y Terminado.
- [x] Obtener las credenciales de la API de Trello y cargarlas como secretos en GitHub.
- [x] Crear la estructura de archivos Markdown de SDD en la carpeta docs/.

## Fase 2: Entorno Local y Código Base (Evolución con Pytest)
- [x] Implementar la página web base `src/index.html`.
- [x] Configurar el entorno de pruebas BDD (`features/hola_mundo.feature` y `steps.py`).
- [x] Implementar el módulo lógico `src/validador.py` y su test unitario con `pytest`.
- [x] Modificar el `Dockerfile` y el `Makefile` para la ejecución unificada de ambas suites de pruebas.
- [x] Validar la secuencia de pruebas localmente con `make test` (Fallo Rápido).

## Fase 3: Automatización del Servidor de IC y Feedback
- [x] Actualizar el workflow de GitHub Actions (`ci-cd.yml`) para soportar la ejecución unificada de `pytest` + `behave`.
- [x] Asegurar la persistencia de la integración con la API de Trello mediante cURL.
- [x] Configurar las alertas por correo electrónico en caso de fallos (`if: failure()`).
- [x] Configurar y validar el despliegue automático en GitHub Pages solo ante éxito en `master`.