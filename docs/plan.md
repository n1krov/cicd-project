# Plan de Arquitectura Técnica y Stack

## Stack Tecnológico
- **IDE / Entorno:** Google Antigravity.
- **Control de Versiones:** GitHub (Estrategia de branches: master, dev, feature/).
- **Servidor de IC:** GitHub Actions (Orquestador principal del pipeline).
- **Entorno Local (Build Local):** Docker +具 Makefile (Consistencia de entorno).
- **Pruebas Unitarias:** Python con el framework `pytest`.
- **Pruebas de Aceptación:** Python con la librería `behave` (Gherkin/BDD).
- **Mecanismo de Feedback:** API de Trello (vía cURL) y Alertas por Correo Electrónico.
- **Entorno de Entrega:** GitHub Pages (Producción).

## Arquitectura del Pipeline de IC/CD (Secuencia Estricta)
1. **Fase de Compilación Local:** Construcción de la imagen Docker aislada con las dependencias instaladas (`pytest` y `behave`).
2. **Barrera de Calidad 1 (Test Unitario):** Ejecución automatizada de `pytest`. Si falla, el pipeline aborta.
3. **Barrera de Calidad 2 (Test de Aceptación):** Ejecución automatizada de `behave`. Si falla, el pipeline aborta.
4. **Mecanismo de Feedback:** - En caso de ÉXITO: Se dispara el script cURL que mueve la tarjeta en Trello de "HACIENDO" a "TERMINAD".
   - En caso de FALLO: Se dispara la notificación automatizada por correo electrónico.
5. **Etapa de Entrega Continua (CD):** Si y solo si todas las etapas previas pasaron con éxito y se encuentra en la rama `master`, se publica automáticamente en GitHub Pages.