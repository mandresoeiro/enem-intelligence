# 📘 O que deve aparecer na documentação (MkDocs)

## 📦 Uso do Python-Decouple

O projeto utiliza **python-decouple** para gerenciar variáveis de
ambiente com segurança e padronização entre DEV e PROD.

### 🔥 Benefícios principais

-   Conversão automática de tipos (`bool`, `int`, `list`)\
-   Valores padrão seguros via `default=`\
-   Leitura direta do `.env`\
-   Código desacoplado da infraestrutura\
-   Facilita mudanças entre ambientes (DEV → PROD)

------------------------------------------------------------------------

## 🧰 Exemplo prático no `base.py`

``` python
from decouple import config, Csv

SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS",
    default="127.0.0.1,localhost",
    cast=Csv()
)
```

🔎 **O cast `Csv()` transforma automaticamente a string do .env em
lista:**

    "127.0.0.1,localhost"
    → ["127.0.0.1", "localhost"]

------------------------------------------------------------------------

## 🧠 Referência visual mental

    ┌────────────────────────────────────┐
    │ .env                               │
    │ ├── DJANGO_SECRET_KEY              │
    │ ├── DJANGO_DEBUG=True              │
    │ └── DJANGO_ALLOWED_HOSTS           │
    │                                    │
    │ base.py                            │
    │ → usa decouple.config()            │
    │ → converte tipos automaticamente   │
    │ → aplica fallback seguro           │
    └────────────────────────────────────┘

------------------------------------------------------------------------

## ✅ Checklist final da migração

-   [x] `python-decouple` instalado\
-   [x] `.env` compatível e documentado\
-   [x] `base.py` atualizado e limpo\
-   [x] Tipos convertidos automaticamente (`bool`, `list`, `int`)\
-   [x] Documentação MkDocs revisada

------------------------------------------------------------------------

## 🚀 Próxima Etapa

Posso gerar e enviar o arquivo completo já atualizado:

### **`core/settings/prod.py`** (versão profissional)

Incluindo: - PostgreSQL com decouple\
- Configurações de segurança (HTTPS, CSRF, Cookies)\
- Allowed Hosts / Trusted Origins\
- Flags de produção

É só pedir!
