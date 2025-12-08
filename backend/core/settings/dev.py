# ==========================================================
# 💻 ENEM Data Portal — Configurações de Desenvolvimento (DEV)
# ==========================================================
"""
Herda de base.py e ajusta o ambiente local.
Objetivo: experiência de desenvolvimento simples e segura.
"""

from .base import *

# ----------------------------------------------------------
# ⚙️ Gerais
# ----------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Ajuda a evitar warnings de CSRF quando testando localmente
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# ----------------------------------------------------------
# 🗄️ Banco de Dados (SQLite Local)
# ----------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ----------------------------------------------------------
# 🌐 CORS
# ----------------------------------------------------------
CORS_ALLOW_ALL_ORIGINS = True
# Caso prefira restringir para o Next.js local
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]

# ----------------------------------------------------------
# ✅ Fim do dev.py
# ----------------------------------------------------------
