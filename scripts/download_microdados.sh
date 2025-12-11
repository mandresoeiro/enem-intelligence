#!/bin/bash
# Script para baixar microdados ENEM em pasta temporária (não versionada)

TEMP_DIR="/tmp/microdados_enem"
DATA_DIR="$HOME/dev/myprojects/enem-intelligence/backend/data"

echo "📥 Baixando microdados do ENEM 2024..."
echo "⚠️  Arquivo grande (~3-5 GB) - pode demorar!"
echo ""

# Cria diretório temporário
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR"

# Baixa o arquivo
echo "🌐 Iniciando download..."
wget -c https://download.inep.gov.br/microdados/microdados_enem_2024.zip

# Descompacta
echo ""
echo "📦 Descompactando..."
unzip -q microdados_enem_2024.zip

# Encontra o CSV
CSV_FILE=$(find . -name "MICRODADOS_ENEM_2024.csv" -type f | head -1)

if [ -z "$CSV_FILE" ]; then
    echo "❌ Arquivo CSV não encontrado!"
    exit 1
fi

echo "✅ CSV encontrado: $CSV_FILE"
echo ""

# Opções de onde colocar
echo "📂 Escolha onde guardar o arquivo:"
echo "1) /tmp/microdados_enem/ (temporário - apaga ao reiniciar)"
echo "2) ~/enem_data/ (pasta na home - permanente, não versionada)"
echo "3) backend/data/raw/ (dentro do projeto, já no .gitignore)"
echo ""
read -p "Opção [1-3]: " OPCAO

case $OPCAO in
    1)
        DEST="$TEMP_DIR"
        cp "$CSV_FILE" "$DEST/MICRODADOS_ENEM_2024.csv"
        ;;
    2)
        DEST="$HOME/enem_data"
        mkdir -p "$DEST"
        cp "$CSV_FILE" "$DEST/MICRODADOS_ENEM_2024.csv"
        ;;
    3)
        DEST="$DATA_DIR/raw"
        mkdir -p "$DEST"
        cp "$CSV_FILE" "$DEST/MICRODADOS_ENEM_2024.csv"
        ;;
    *)
        echo "❌ Opção inválida!"
        exit 1
        ;;
esac

echo ""
echo "✅ CSV salvo em: $DEST/MICRODADOS_ENEM_2024.csv"
echo ""
echo "🔧 Atualizando configuração do backend..."

# Cria arquivo .env com o caminho
ENV_FILE="$DATA_DIR/../.env"
if ! grep -q "ENEM_DATA_PATH" "$ENV_FILE" 2>/dev/null; then
    echo "ENEM_DATA_PATH=$DEST" >> "$ENV_FILE"
    echo "✅ Caminho adicionado ao .env"
fi

echo ""
echo "📊 Tamanho do arquivo:"
du -h "$DEST/MICRODADOS_ENEM_2024.csv"
echo ""
echo "✅ Pronto! Reinicie o backend para usar os dados reais."
