#!/bin/bash

# ==========================================================
# 🚀 Script de Setup - ENEM Intelligence
# ==========================================================
# Este script automatiza a configuração inicial do projeto
# ==========================================================

set -e

echo "🎓 ENEM Intelligence - Setup Automático"
echo "========================================"
echo ""

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar se está na raiz do projeto
if [ ! -f "DEPLOYMENT.md" ]; then
    echo "❌ Execute este script da raiz do projeto!"
    exit 1
fi

# 1. Backend Setup
echo -e "${BLUE}📦 Configurando Backend...${NC}"
cd backend

if ! command -v poetry &> /dev/null; then
    echo -e "${YELLOW}⚠️  Poetry não encontrado. Instale com: curl -sSL https://install.python-poetry.org | python3 -${NC}"
    exit 1
fi

poetry install
echo -e "${GREEN}✓ Dependências do backend instaladas${NC}"

# Criar diretório de dados se não existir
mkdir -p data
echo -e "${GREEN}✓ Diretório de dados criado${NC}"

# Executar migrações
poetry run python manage.py migrate
echo -e "${GREEN}✓ Migrações executadas${NC}"

# Criar superusuário (opcional)
echo ""
echo -e "${YELLOW}Deseja criar um superusuário para o admin? (s/n)${NC}"
read -r response
if [[ "$response" =~ ^([sS][iI][mM]|[sS])$ ]]; then
    poetry run python manage.py createsuperuser
fi

cd ..

# 2. Frontend Setup
echo ""
echo -e "${BLUE}📦 Configurando Frontend...${NC}"
cd frontend

if ! command -v npm &> /dev/null; then
    echo -e "${YELLOW}❌ npm não encontrado. Instale o Node.js primeiro.${NC}"
    exit 1
fi

npm install
echo -e "${GREEN}✓ Dependências do frontend instaladas${NC}"

cd ..

# 3. Verificar microdados
echo ""
echo -e "${BLUE}📊 Verificando Microdados...${NC}"

if ls backend/data/MICRODADOS_ENEM_*.csv 1> /dev/null 2>&1; then
    echo -e "${GREEN}✓ Arquivos de microdados encontrados:${NC}"
    ls -lh backend/data/MICRODADOS_ENEM_*.csv
    echo ""
    echo -e "${YELLOW}Deseja importar os dados agora? (s/n)${NC}"
    read -r response
    if [[ "$response" =~ ^([sS][iI][mM]|[sS])$ ]]; then
        cd backend
        for file in data/MICRODADOS_ENEM_*.csv; do
            echo -e "${BLUE}Importando $file...${NC}"
            poetry run python manage.py importar_microdados_enem --csv="$file"
        done
        cd ..
    fi
else
    echo -e "${YELLOW}⚠️  Nenhum arquivo de microdados encontrado em backend/data/${NC}"
    echo "   Baixe os arquivos de: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados"
    echo "   E coloque em: backend/data/MICRODADOS_ENEM_2024.csv"
fi

# 4. Conclusão
echo ""
echo -e "${GREEN}✅ Setup concluído!${NC}"
echo ""
echo "Para iniciar os servidores:"
echo ""
echo -e "${BLUE}Terminal 1 - Backend:${NC}"
echo "  cd backend && poetry run python manage.py runserver"
echo ""
echo -e "${BLUE}Terminal 2 - Frontend:${NC}"
echo "  cd frontend && npm run dev"
echo ""
echo "Depois acesse: http://localhost:3000"
echo ""
