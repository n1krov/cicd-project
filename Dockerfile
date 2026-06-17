FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias de pruebas
RUN pip install --no-cache-dir behave pytest

# Copiar archivos del proyecto
COPY src/ ./src/
COPY features/ ./features/

# Comando predeterminado para ejecutar las pruebas behave
CMD ["behave"]
