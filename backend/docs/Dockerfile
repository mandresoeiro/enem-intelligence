# ==========================================================
# 📘 ENEM Data Portal — MkDocs (Documentação Técnica)
# ==========================================================

# Imagem base
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /docs

# Instala MkDocs + Tema Material
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir mkdocs mkdocs-material

# Copia apenas os arquivos de configuração e conteúdo
COPY mkdocs.yml ./
COPY docs/ ./docs/
COPY environment.md ./
COPY projeto-discriminado/ ./projeto-discriminado/

# Expõe a porta padrão do MkDocs
EXPOSE 8001

# Comando padrão para iniciar o servidor MkDocs
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8001"]
