# Use a imagem base do Python
FROM python:3.10

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install -r requirements.txt

# Copie todo o código-fonte para o contêiner
COPY . .

# Exponha a porta em que o servidor Django será executado
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
