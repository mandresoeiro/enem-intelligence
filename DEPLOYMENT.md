# 🚀 Guia de Deploy - ENEM Intelligence

## 📋 Pré-requisitos no Novo Ambiente

- Python 3.12+
- Poetry
- Node.js 18+
- Git

## 🔧 Setup Inicial (no trabalho)

### 1. Clonar o Repositório
```bash
git clone https://github.com/mandresoeiro/enem-intelligence.git
cd enem-intelligence
```

### 2. Configurar Backend
```bash
cd backend
poetry install
poetry run python manage.py migrate
```

### 3. Configurar Frontend
```bash
cd ../frontend
npm install
```

### 4. Baixar os Microdados do ENEM

**⚠️ IMPORTANTE**: Os arquivos de microdados são grandes demais para o GitHub.

#### Opção 1: Baixar Direto no Trabalho
1. Acesse: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados
2. Baixe o arquivo do ano desejado (2023 ou 2024)
3. Coloque em `backend/data/MICRODADOS_ENEM_2024.csv`

#### Opção 2: Transferir via Cloud
1. Suba o arquivo no Google Drive/OneDrive/Dropbox
2. Baixe no trabalho
3. Coloque em `backend/data/`

#### Opção 3: Transferir via USB
1. Copie o arquivo em um pen drive
2. Leve para o trabalho
3. Coloque em `backend/data/`

### 5. Executar os Servidores

Terminal 1 - Backend:
```bash
cd backend
poetry run python manage.py runserver
```

Terminal 2 - Frontend:
```bash
cd frontend
npm run dev
```

Acesse: http://localhost:3000

## 📊 Trabalhando com Múltiplos Anos (2023, 2024, etc.)

O sistema está preparado para trabalhar com múltiplos anos. Veja como:

### Estrutura de Arquivos Sugerida:
```
backend/data/
├── MICRODADOS_ENEM_2023.csv
├── MICRODADOS_ENEM_2024.csv
└── README.md
```

### Importar Dados de Anos Diferentes:

**Para 2024:**
```bash
poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2024.csv
```

**Para 2023:**
```bash
poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2023.csv
```

## 🔄 Sincronização de Dados entre Ambientes

### Opção 1: Exportar/Importar Banco de Dados

**Exportar (em casa):**
```bash
cd backend
poetry run python manage.py dumpdata enem > dados_enem.json
```

**Importar (no trabalho):**
```bash
cd backend
poetry run python manage.py loaddata dados_enem.json
```

### Opção 2: Usar Backup do SQLite

**Backup (em casa):**
```bash
cp backend/db.sqlite3 backup_db.sqlite3
# Envie este arquivo via cloud/USB
```

**Restaurar (no trabalho):**
```bash
cp backup_db.sqlite3 backend/db.sqlite3
```

## 📦 Tamanho dos Arquivos

| Arquivo | Tamanho Aproximado | Onde Guardar |
|---------|-------------------|--------------|
| Repositório Git | ~10 MB | GitHub |
| node_modules | ~500 MB | Local (não versionar) |
| Microdados ENEM | 3-5 GB | Cloud/USB (não versionar) |
| Banco de Dados | ~100 MB | Backup via cloud/USB |

## ⚡ Dicas de Performance

1. **Primeira Importação**: Pode demorar 10-30 minutos dependendo do tamanho do arquivo
2. **Busca por CPF**: Rápida após a primeira carga (pandas cacheia os dados)
3. **Otimização**: Considere usar apenas uma amostra dos microdados para testes

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` no backend com:
```env
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 📝 Checklist de Deploy

- [ ] Clonar repositório
- [ ] Instalar dependências (poetry + npm)
- [ ] Executar migrações
- [ ] Baixar/transferir microdados
- [ ] Importar dados (se necessário)
- [ ] Criar usuário admin: `poetry run python manage.py createsuperuser`
- [ ] Testar aplicação

## 🆘 Problemas Comuns

### Erro: "Port already in use"
```bash
# Matar processo na porta 8000
lsof -ti:8000 | xargs kill -9

# Matar processo na porta 3000
lsof -ti:3000 | xargs kill -9
```

### Erro: "Module not found"
```bash
# Backend
cd backend && poetry install

# Frontend
cd frontend && npm install
```

### Erro: "Database locked"
```bash
# Feche todos os terminais que estão usando o banco
# Reinicie o servidor
```
