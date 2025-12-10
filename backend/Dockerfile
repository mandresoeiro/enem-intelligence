# ==========================================================
# 🐍 Backend — Django + DRF + Poetry
# ==========================================================
FROM python:3.12-slim

# Variáveis de ambiente básicas
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential libpq-dev curl

# Instala o Poetry
RUN pip install poetry

# Copia arquivos do Poetry e instala dependências
COPY pyproject.toml poetry.lock* ./
# Garante que o lock esteja atualizado com o pyproject (inclui novas deps como pandas)
RUN poetry lock --no-interaction && poetry install --no-root --no-interaction

# Copia o restante do backend
COPY . .

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando padrão
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
