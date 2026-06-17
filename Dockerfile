FROM python:3.11-slim

WORKDIR /app

# Instalar behave
RUN pip install --no-cache-dir behave

# Copiar archivos del proyecto
COPY src/ ./src/
COPY features/ ./features/

# Comando predeterminado para ejecutar las pruebas behave
CMD ["behave"]
