#!/bin/bash

# ==========================================================
# 🚀 Script de Setup Completo com Download de Microdados
# ==========================================================
# Este script faz tudo: clone, setup e download dos dados
# ==========================================================

set -e

echo "🎓 ENEM Intelligence - Setup Completo com Download"
echo "=================================================="
echo ""
echo "⚠️  Este script vai baixar ~3-5 GB de dados do INEP"
echo "   Certifique-se de ter uma boa conexão de internet!"
echo ""
read -p "Deseja continuar? (s/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[SsYy]$ ]]; then
    echo "❌ Cancelado pelo usuário"
    exit 1
fi

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo -e "${BLUE}📦 Passo 1/5: Verificando repositório...${NC}"

if [ ! -f "setup.sh" ]; then
    echo "❌ Este script deve ser executado da raiz do projeto!"
    echo "   Execute assim:"
    echo "   git clone https://github.com/mandresoeiro/enem-intelligence.git"
    echo "   cd enem-intelligence"
    echo "   ./setup_completo.sh"
    exit 1
fi

echo -e "${GREEN}✓ Repositório OK${NC}"

echo ""
echo -e "${BLUE}📦 Passo 2/5: Instalando dependências...${NC}"
./setup.sh

echo ""
echo -e "${BLUE}📦 Passo 3/5: Criando diretórios de dados...${NC}"
mkdir -p backend/data/raw
echo -e "${GREEN}✓ Diretórios criados${NC}"

echo ""
echo -e "${BLUE}📥 Passo 4/5: Baixando microdados do INEP (isso pode demorar)...${NC}"
cd backend/data

# Verificar se já existe
if [ -f "microdados_enem_2024.zip" ]; then
    echo -e "${YELLOW}⚠️  Arquivo já existe. Deseja baixar novamente? (s/n)${NC}"
    read -p "" -n 1 -r
    echo
    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        rm microdados_enem_2024.zip
    else
        echo "Pulando download..."
    fi
fi

if [ ! -f "microdados_enem_2024.zip" ]; then
    echo "Baixando de: https://download.inep.gov.br/microdados/microdados_enem_2024.zip"
    wget -c https://download.inep.gov.br/microdados/microdados_enem_2024.zip || {
        echo -e "${YELLOW}⚠️  wget não disponível, tentando com curl...${NC}"
        curl -C - -O https://download.inep.gov.br/microdados/microdados_enem_2024.zip
    }
fi

echo -e "${GREEN}✓ Download concluído${NC}"

echo ""
echo -e "${BLUE}📦 Passo 5/5: Descompactando arquivos...${NC}"
unzip -o microdados_enem_2024.zip -d raw/
echo -e "${GREEN}✓ Arquivos descompactados${NC}"

cd ../..

echo ""
echo -e "${GREEN}✅ Setup completo finalizado!${NC}"
echo ""
echo "📊 Próximos passos:"
echo ""
echo "1. Importar dados (opcional, para busca por CPF):"
echo -e "   ${BLUE}cd backend${NC}"
echo -e "   ${BLUE}poetry run python manage.py importar_microdados_enem --csv=data/raw/enem_2024/DADOS/MICRODADOS_ENEM_2024.csv${NC}"
echo ""
echo "2. Iniciar servidores:"
echo -e "   ${BLUE}Terminal 1:${NC} cd backend && poetry run python manage.py runserver"
echo -e "   ${BLUE}Terminal 2:${NC} cd frontend && npm run dev"
echo ""
echo "3. Acessar: http://localhost:3000"
echo ""
echo -e "${GREEN}🎉 Tudo pronto para usar!${NC}"
