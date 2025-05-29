FROM python:3.11-slim

WORKDIR /app

# Copia o requirements e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto
COPY . .

# Expondo a porta da API
EXPOSE 8000

# Iniciando o servidor FastAPI
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
