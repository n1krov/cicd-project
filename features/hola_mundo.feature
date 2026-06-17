# language: es
Característica: Validación del Saludo Principal

  Escenario: Validar el texto del saludo en la página principal
    Dado que el runner de pruebas tiene acceso al archivo de fuentes
    Cuando se examina el contenido del archivo "src/index.html"
    Entonces el documento debe contener una etiqueta estructurada con el texto exacto "Hola Mundo"
