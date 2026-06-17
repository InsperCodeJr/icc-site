FROM python:3.12-slim

WORKDIR /app

# Instala dependências do sistema para o Pillow
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Cria a pasta de arquivos de mídia
RUN mkdir -p /app/media

# Roda migrations, importa os membros e inicia o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py import_members && python manage.py download_photos && python manage.py runserver 0.0.0.0:8000"]