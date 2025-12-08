# 🎓 ENEM Intelligence

Sistema completo para análise de desempenho do ENEM com dashboard profissional, gerenciamento de alunos e integração com microdados oficiais.

## ✨ Funcionalidades

- 📊 **Dashboard Interativo** com estatísticas em tempo real
- 👨‍🎓 **Gerenciamento de Alunos** com formulários completos
- 🔍 **Busca Automática de Notas** nos microdados do ENEM por CPF
- 📈 **Estatísticas por Estado** com comparações de desempenho
- 📝 **Simulados e Avaliações** para acompanhamento
- 🎯 **Interface Profissional** com sidebar responsiva

## 🚀 Quick Start

### Pré-requisitos
- Python 3.12+
- Poetry
- Node.js 18+
- Git

### Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/mandresoeiro/enem-intelligence.git
cd enem-intelligence

# 2. Execute o script de setup
./setup.sh

# 3. Inicie os servidores
# Terminal 1
cd backend && poetry run python manage.py runserver

# Terminal 2
cd frontend && npm run dev
```

Acesse: **http://localhost:3000**

## 📊 Trabalhando com Microdados

### ⚠️ IMPORTANTE: Arquivos NÃO estão no GitHub

Os arquivos de microdados do ENEM são **muito grandes** (3-5 GB) e **NÃO estão** versionados no Git.

### Como Obter os Microdados

1. **Baixar do Site Oficial:**
   - Acesse: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados
   - Baixe os anos desejados (2024, 2023, etc.)

2. **Colocar no Projeto:**
   ```bash
   # Coloque os arquivos em:
   backend/data/MICRODADOS_ENEM_2024.csv
   backend/data/MICRODADOS_ENEM_2023.csv
   ```

3. **Importar os Dados:**
   ```bash
   cd backend
   poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2024.csv
   ```

### Transferência entre Ambientes (Casa ↔️ Trabalho)

#### Opção 1: Cloud Storage (Recomendado)
- Upload no Google Drive/OneDrive/Dropbox
- Baixe no outro ambiente
- Coloque em `backend/data/`

#### Opção 2: Pen Drive/HD Externo
- Copie os arquivos CSV
- Transfira fisicamente

#### Opção 3: Banco de Dados Exportado
```bash
# Exportar (origem)
cd backend
poetry run python manage.py dumpdata enem > dados_enem.json

# Importar (destino)
poetry run python manage.py loaddata dados_enem.json
```

## 🏗️ Estrutura do Projeto

```
enem-intelligence/
├── backend/                 # Django REST API
│   ├── core/               # Configurações
│   ├── enem/               # App principal
│   │   ├── models.py       # Modelos de dados
│   │   ├── views.py        # API endpoints
│   │   ├── utils.py        # Busca nos microdados
│   │   └── management/     # Comandos personalizados
│   └── data/               # Microdados (não versionado)
│       └── README.md
├── frontend/               # Next.js Application
│   ├── app/               # Páginas
│   │   ├── alunos/        # Gerenciamento de alunos
│   │   └── page.tsx       # Dashboard
│   └── components/        # Componentes React
│       ├── Sidebar.jsx    # Menu lateral
│       └── Layout.jsx     # Layout principal
├── DEPLOYMENT.md          # Guia completo de deploy
├── setup.sh              # Script de instalação
└── README.md             # Este arquivo
```

## 🔧 Comandos Úteis

### Backend

```bash
# Criar migrações
poetry run python manage.py makemigrations

# Aplicar migrações
poetry run python manage.py migrate

# Criar superusuário
poetry run python manage.py createsuperuser

# Criar aluno de teste
poetry run python manage.py criar_aluno_fake

# Importar microdados
poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2024.csv

# Shell Django
poetry run python manage.py shell
```

### Frontend

```bash
# Desenvolvimento
npm run dev

# Build de produção
npm run build

# Lint
npm run lint
```

## 📡 API Endpoints

### Alunos
- `GET /api/enem/alunos/` - Listar todos
- `POST /api/enem/alunos/` - Criar novo
- `POST /api/enem/alunos/buscar_notas_cpf/` - Buscar notas por CPF
- `GET /api/enem/alunos/{id}/` - Detalhes
- `DELETE /api/enem/alunos/{id}/` - Excluir

### Outros Recursos
- `/api/enem/simulados/` - Simulados
- `/api/enem/cursos/` - Cursos
- `/api/enem/estatisticas-estado/` - Estatísticas por estado

## 🎨 Tecnologias

**Backend:**
- Django 6.0
- Django REST Framework
- Poetry
- Pandas (processamento de dados)
- SQLite (desenvolvimento)

**Frontend:**
- Next.js 16
- React 19
- SCSS Modules
- Axios

## 📝 Suporte para Múltiplos Anos

O sistema suporta dados de **múltiplos anos** do ENEM:

```bash
# Importar 2024
poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2024.csv

# Importar 2023
poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2023.csv
```

A busca automática por CPF procura nos anos: **2024 → 2023 → 2022**

## 🐛 Problemas Comuns

Ver [DEPLOYMENT.md](DEPLOYMENT.md) para soluções detalhadas.

## 📄 Licença

MIT License - veja LICENSE para detalhes

## 👨‍💻 Autor

**Márcio Soeiro**
- GitHub: [@mandresoeiro](https://github.com/mandresoeiro)

---

⭐ Se este projeto foi útil, considere dar uma estrela!
