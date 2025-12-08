# ==========================================================
# 🌍 ENEM Data Portal — Configurações Base (com Python-Decouple)
# ==========================================================
# Este arquivo serve como base comum para DEV e PROD.
# - Em dev, será herdado por core/settings/dev.py (SQLite + DEBUG=True)
# - Em prod, herdado por core/settings/prod.py (PostgreSQL + DEBUG=False)
# ==========================================================

from pathlib import Path
from decouple import config, Csv

# ==========================================================
# 📁 Diretório Base do Projeto
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ==========================================================
# 🔐 Variáveis de Ambiente via python-decouple
# ==========================================================
# - Lê direto do .env
# - Converte tipos automaticamente (bool, list, int, etc)
# - Evita que o .env seja interpretado manualmente
# ==========================================================
SECRET_KEY = config("DJANGO_SECRET_KEY", default="dev-key-unsafe")

# ⚙️ Ambiente padrão: desenvolvimento
DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)

# 🌍 Hosts permitidos (em dev, libera tudo)
ALLOWED_HOSTS = ["*"]  # ✅ aceita qualquer host local
# ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="*", cast=Csv())

# ==========================================================
# 🧱 Aplicações Django + DRF + Locais
# ==========================================================
INSTALLED_APPS = [
    # ⚙️ Core Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 🔌 Terceiros
    "rest_framework",
    "corsheaders",

    # 🧩 Apps Locais
    "enem",
]

# ==========================================================
# 🧭 Middlewares
# ==========================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# ==========================================================
# 🧩 Templates
# ==========================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==========================================================
# 🗄️ Banco de Dados (SQLite por padrão)
# ==========================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==========================================================
# 🔓 CORS
# ==========================================================
CORS_ALLOW_ALL_ORIGINS = True

# ==========================================================
# 🚀 Aplicação WSGI
# ==========================================================
WSGI_APPLICATION = "core.wsgi.application"

# ==========================================================
# 🔐 Validação de Senhas
# ==========================================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==========================================================
# 🌎 Localização
# ==========================================================
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ==========================================================
# 🧱 Arquivos Estáticos
# ==========================================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

# ==========================================================
# 🆔 Campo Padrão
# ==========================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================================================
# ✅ Fim do base.py
# ==========================================================



# ==========================================================
# 🚀 BLOCO DE PRODUÇÃO — core/settings/prod.py
# ==========================================================
# Esse bloco pode ser separado em outro arquivo (recomendado),
# mas está incluído aqui como referência imediata.
# ==========================================================

"""
from .base import *
from decouple import config, Csv

# ==========================================================
# 🚀 ENEM Data Portal — Configurações de Produção (PROD)
# ==========================================================
# Este arquivo é carregado quando DJANGO_SETTINGS_MODULE=core.settings.prod
# Ele herda tudo de base.py e sobrescreve com configurações seguras.
# ==========================================================

DEBUG = False  # 🚫 Nunca use True em produção

# 🌍 Hosts e origens confiáveis
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="localhost", cast=Csv())
CSRF_TRUSTED_ORIGINS = config(
    "DJANGO_TRUSTED_ORIGINS",
    default="https://api.enem-data.gov.br,https://enem-data.com",
    cast=Csv(),
)

# 🗄️ Banco de Dados — PostgreSQL (Produção)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="enemdb"),
        "USER": config("POSTGRES_USER", default="enemuser"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="securepass"),
        "HOST": config("POSTGRES_HOST", default="localhost"),
        "PORT": config("POSTGRES_PORT", default="5432"),
    }
}

# 🔒 Segurança
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = config("DJANGO_SECURE_SSL_REDIRECT", default=True, cast=bool)

# 🪶 Logging Básico
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

# ⚠️ Bloqueia uso indevido de PROD localmente
import sys
if "runserver" in sys.argv:
    raise RuntimeError("❌ Você está tentando rodar o servidor local com settings de PRODUÇÃO!")
"""


# 💡 Explicação
# Parte	Função
# base.py	Configuração comum (carregada por dev.py e prod.py)
# ALLOWED_HOSTS = ["*"]	Mantém o dev livre e funcional
# Bloco prod.py comentado	Mantém referência visual e pode ser facilmente extraído depois
# Proteção “runserver”	Evita acidentalmente rodar o modo produção no local

# 🧠 Referência visual mental
# ┌──────────────────────────────┐
# │ core/settings/base.py        │
# │  ├── DEBUG=True (dev)        │
# │  ├── ALLOWED_HOSTS=["*"]     │
# │  └── SQLite local            │
# │                              │
# │ core/settings/prod.py        │
# │  ├── DEBUG=False             │
# │  ├── PostgreSQL              │
# │  ├── Segurança HTTPS         │
# │  └── Bloqueio local runserver│
# └──────────────────────────────┘
