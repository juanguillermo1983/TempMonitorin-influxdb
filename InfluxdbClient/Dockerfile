# Dockerfile
FROM python:3.8-slim

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente al contenedor
#COPY . .

# Comando por defecto al ejecutar el contenedor
#CMD ["python", "app.py"]
