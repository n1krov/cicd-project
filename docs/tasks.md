# Lista de Tareas de Implementación

## Fase 1: Infraestructura de Documentación y Gestión
- [x] Crear el tablero en Trello con las columnas To-Do, Haciendo y Terminado.
- [x] Obtener las credenciales de la API de Trello y cargarlas como secretos en GitHub.
- [ ] Crear la estructura de archivos Markdown de SDD en la carpeta docs/.

## Fase 2: Entorno Local y Código Base
- [ ] Implementar la página web base `src/index.html`.
- [ ] Configurar el entorno de pruebas BDD (`features/hola_mundo.feature` y `steps.py`).
- [ ] Crear el `Dockerfile` y el `Makefile` para la ejecución local encapsulada.
- [ ] Ejecutar la prueba localmente con `make test` y verificar el "Fallo Rápido".

## Fase 3: Automatización del Servidor de IC y Feedback
- [ ] Crear el workflow de GitHub Actions (`ci-cd.yml`).
- [ ] Implementar la integración con la API de Trello para mover tarjetas desde el pipeline.
- [ ] Configurar las alertas por correo electrónico en caso de fallos.
- [ ] [cite_start]Habilitar y validar el despliegue automático en GitHub Pages[cite: 8].