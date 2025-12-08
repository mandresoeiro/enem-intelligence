# 🌍 Configuração de Ambientes --- ENEM Data Portal

> Documento oficial de configuração de ambientes (DEV e PROD) do projeto
> **ENEM Data Portal**.\
> Aqui estão descritos todos os arquivos relacionados ao ambiente:
> `.env`, `.env.example`, e `.gitignore`.

------------------------------------------------------------------------

## 🧩 Estrutura de Arquivos

    backend/
    ├── .env
    ├── .env.example
    ├── .gitignore
    └── core/
        └── settings/
            ├── base.py
            ├── dev.py
            └── prod.py

------------------------------------------------------------------------

## ⚙️ Arquivo `.env` (ativo no desenvolvimento)

> Este é o arquivo usado **localmente** durante o desenvolvimento.\
> As variáveis de produção ficam **comentadas** para referência futura.

``` bash
# ==========================================
# 🔧 ENEM Data Portal - Ambiente DEV
# ==========================================

# Django - Desenvolvimento
DJANGO_SECRET_KEY=dev-secret-key-123456789
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_TRUSTED_ORIGINS=http://127.0.0.1:8000
DJANGO_DEBUG=True

# Banco de dados local (SQLite padrão)
# Para usar PostgreSQL local, descomente abaixo:
# POSTGRES_DB=enemdb
# POSTGRES_USER=enemuser
# POSTGRES_PASSWORD=supersecret
# POSTGRES_HOST=localhost
# POSTGRES_PORT=5432


# ==========================================
# 🏗️ Ambiente de Produção (comentado)
# ==========================================

# DJANGO_SECRET_KEY=change-this-in-prod
# DJANGO_ALLOWED_HOSTS=api.enem-data.gov.br,www.enem-data.gov.br
# DJANGO_TRUSTED_ORIGINS=https://api.enem-data.gov.br,https://enem-data.gov.br
# DJANGO_DEBUG=False

# POSTGRES_DB=enemdb
# POSTGRES_USER=enemuser
# POSTGRES_PASSWORD=replace_me_securely
# POSTGRES_HOST=db
# POSTGRES_PORT=5432
```

## 📘 Arquivo `.env.example` (modelo para o time)

``` bash
# ==========================================
# 🌎 ENEM Data Portal - Exemplo de .env
# ==========================================

# Django
DJANGO_SECRET_KEY=change-me
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_TRUSTED_ORIGINS=http://127.0.0.1:8000
DJANGO_DEBUG=True

# Banco de dados
POSTGRES_DB=enemdb
POSTGRES_USER=enemuser
POSTGRES_PASSWORD=supersecret
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

## 🚫 Arquivo `.gitignore`

``` bash
# Ambiente e segredos
.env
.env.*

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.sqlite3
*.log

# Ambientes virtuais
.venv/
env/
venv/

# Django
db.sqlite3
media/
static/

# IDEs e Sistema
.vscode/
.idea/
.DS_Store

# MkDocs
/site/
```

## ✅ Checklist de Ambiente

  Item                      Status   Descrição
  ------------------------- -------- ----------------------------------
  .env criado               ☐        Arquivo ativo com configs de dev
  .env.example versionado   ☐        Modelo para o time
  .gitignore atualizado     ☐        Protege segredos
  python-dotenv instalado   ☐        Carrega variáveis no Django
  settings modularizados    ☐        base/dev/prod separados

------------------------------------------------------------------------

## 💡 Dica Profissional

Teste se o Django está lendo corretamente o .env:

``` bash
poetry run python manage.py shell
```

Dentro do shell Python:

``` python
from django.conf import settings
print(settings.ALLOWED_HOSTS)
```

Saída esperada:

    ['127.0.0.1', 'localhost']

------------------------------------------------------------------------

## 📘 Referência Rápida --- Variáveis Disponíveis

  ------------------------------------------------------------------------------
  Variável                 Descrição                  Exemplo
  ------------------------ -------------------------- --------------------------
  DJANGO_SECRET_KEY        Chave secreta da aplicação dev-secret-key-123456789

  DJANGO_ALLOWED_HOSTS     Hosts permitidos           127.0.0.1,localhost

  DJANGO_TRUSTED_ORIGINS   Domínios confiáveis        http://127.0.0.1:8000

  DJANGO_DEBUG             Ativa/Desativa modo debug  True

  POSTGRES_DB              Nome do banco PostgreSQL   enemdb

  POSTGRES_USER            Usuário do banco           enemuser

  POSTGRES_PASSWORD        Senha do banco             supersecret

  POSTGRES_HOST            Host do banco              localhost

  POSTGRES_PORT            Porta do banco             5432
  ------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Referência visual mental

    ┌────────────────────────────────────────────┐
    │ backend/                                   │
    │ ├── .env              ← usado localmente   │
    │ ├── .env.example      ← modelo no Git      │
    │ ├── .gitignore        ← protege segredos   │
    │ └── core/settings/                         │
    │     ├── base.py                            │
    │     ├── dev.py                             │
    │     └── prod.py                            │
    └────────────────────────────────────────────┘

------------------------------------------------------------------------

## 🏁 Conclusão

-   Ambiente DEV configurado e funcional\
-   Produção já documentada e comentada\
-   Projeto pronto para Docker, CI/CD e Deploy seguro

📘 **Próxima leitura sugerida:**\
ETAPA 1 --- Criação do App enem e primeiros Models (Aluno, Curso,
Inscricao, Estatistica)
