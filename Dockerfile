FROM python:3.12-slim

WORKDIR /app

# Actualiza el sistema y limpia la caché de apt en un solo paso para reducir el tamaño de la imagen
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto 8080
EXPOSE 8080

# Define el comando de entrada
ENTRYPOINT ["streamlit", "run", "🏠_Home.py", "--server.port=8080", "--server.address=0.0.0.0"]