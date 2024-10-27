# Usa una imagen de Python como base
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copia requirements.txt e instala las dependencias
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copia el resto de los archivos de tu proyecto al contenedor
COPY . .

# Comando por defecto para ejecutar el archivo principal
CMD ["python", "main.py"]
