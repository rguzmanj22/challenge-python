# Imagen de Python oficial
FROM python:3

# Directorio sobre el cual va a trabajar
WORKDIR /app

# Copiar archivo de requerimientos al directorio de trabajo
COPY requirements.txt /app

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar código fuente a directorio de trabajo
COPY . /app

# Ejecutar script
CMD [ "python", "main.py" ]