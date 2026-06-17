# Requerimientos: Validación de Entorno CI/CD con Hola Mundo

## Contexto y Objetivo
El objetivo es construir un entorno de integración y entrega continua (CI/CD) completamente automatizado para validar una aplicación web mínima. La aplicación cuenta con un frontend estático ("Hola Mundo") y un módulo lógico de validación, sirviendo como vehículo para demostrar la robustez de la infraestructura, el testing automatizado en pirámide (unitario + aceptación) y los mecanismos de feedback.

## Funcionalidades Incluidas (Scope In)
- Página web estática que despliega el texto "Hola Mundo".
- Módulo de lógica interna para la validación de consistencia de textos.
- Suite de pruebas automatizadas en dos niveles: Unitario (micro) y Aceptación (macro).
- Sincronización automática con un tablero de Trello basado en el estado de la build.
- Mecanismo de feedback por correo electrónico en caso de fallos.
- Despliegue automatizado a producción.

## Fuera de Alcance (Scope Out)
- Lógica de backend compleja o bases de datos relacionales.
- Estilos CSS avanzados o frameworks de frontend (React, Vue, etc.).

## Criterios de Aceptación (Formato Given/When/Then)
- **Caso 1: Validación del Saludo Principal (Prueba de Aceptación / BDD)**
  - **Given:** El sistema de archivos o el runner de IC tiene acceso al archivo de fuentes.
  - **When:** Se examina el contenido del archivo `src/index.html`.
  - **Then:** El documento debe contener una etiqueta estructurada con el texto exacto "Hola Mundo".

- **Caso 2: Validación Unitaria de Consistencia de Texto (Prueba Unitaria)**
  - **Función:** `validar_texto_saludo(texto)` en `src/validador.py`.
  - **Regla 1:** Si el texto es exactamente "Hola Mundo", debe retornar `True`.
  - **Regla 2:** Si el texto está vacío o supera los 50 caracteres, debe retornar `False`.