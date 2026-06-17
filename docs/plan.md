# Plan de Arquitectura Técnica y Stack

## Stack Tecnológico
- **IDE / Entorno:** Google Antigravity.
- [cite_start]**Control de Versiones:** GitHub (Estrategia de ramas: master, dev, feature/ [cite: 7, 15]).
- [cite_start]**Servidor de IC:** GitHub Actions (Orquestador principal del pipeline [cite: 7, 16]).
- [cite_start]**Entorno Local (Build Local):** Docker + Makefile (Consistencia de entorno ).
- [cite_start]**Pruebas Automatizadas:** Python con la librería `behave` (Gherkin/BDD para el Spec-Driven Dev [cite: 7, 18]).
- [cite_start]**Mecanismo de Feedback:** API de Trello (vía cURL) y Alertas por Correo Electrónico (SMTP [cite: 19]).
- [cite_start]**Entorno de Entrega:** GitHub Pages (Producción [cite: 8, 20]).

## Arquitectura del Pipeline de IC/CD
1. **Etapa de Validación Local:** Ejecución de `make test` dentro de un contenedor Docker aislado.
2. **Etapa de Integración (remota):** GitHub Actions dispara los tests al recibir código en `dev`.
3. **Etapa de Feedback:** Si la build falla, envía correo. Si pasa, actualiza Trello.
4. [cite_start]**Etapa de Entrega:** Si el código se consolida en `master`, se publica en GitHub Pages[cite: 8].