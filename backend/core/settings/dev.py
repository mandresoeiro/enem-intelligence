# ==========================================================
# 💻 ENEM Data Portal — Configurações de Desenvolvimento (DEV)
# ==========================================================
# Este arquivo herda todas as configurações de base.py
# e sobrescreve apenas o que é específico do ambiente local.
# ==========================================================

from .base import *

# ==========================================================
# ⚙️ Configurações Gerais
# ==========================================================
# - DEBUG=True libera o modo de depuração (erros detalhados)
# - ALLOWED_HOSTS=["*"] permite acesso de qualquer IP local
# ==========================================================
DEBUG = True
ALLOWED_HOSTS = ["*"]  # 🌍 Livre para localhost, 127.0.0.1, etc.

# ==========================================================
# 🗄️ Banco de Dados (SQLite Local)
# ==========================================================
# Simples e prático para desenvolvimento.
# Em produção será substituído por PostgreSQL no prod.py
# ==========================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==========================================================
# 🌐 CORS (Cross-Origin Resource Sharing)
# ==========================================================
# Permite que o frontend (Next.js) acesse a API livremente.
# Ideal para testes locais sem bloqueios.
# ==========================================================
CORS_ALLOW_ALL_ORIGINS = True

# ==========================================================
# 🧠 Dica Profissional:
# ==========================================================
# Caso você esteja usando outro frontend (ex: em porta diferente),
# pode restringir o acesso apenas a ele:
#
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]
# ==========================================================

# ✅ Fim do dev.py
# ==========================================================


#💡 Explicação
Seção	Função
# DEBUG=True	Ativa o modo de depuração local (mostra stacktraces detalhados).
# ALLOWED_HOSTS=["*"]	Permite qualquer origem local (sem bloqueio de host).
# DATABASES	Usa SQLite (zero configuração, ideal para dev).
# CORS_ALLOW_ALL_ORIGINS=True	Permite acesso do frontend (Next.js, porta 3000).
