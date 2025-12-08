#!/bin/bash

# ==========================================================
# 📦 Script para Preparar Dados para Transferência
# ==========================================================

set -e

echo "📦 Preparando dados do ENEM para transferência..."
echo ""

cd backend/data

# Verificar se existem dados
if [ ! -d "raw" ] && [ ! -f "MICRODADOS_ENEM_2024.csv" ]; then
    echo "❌ Nenhum dado encontrado em backend/data/"
    echo "   Baixe os microdados primeiro."
    exit 1
fi

# Criar arquivo compactado
echo "🗜️  Compactando arquivos..."
tar -czf ../../enem_data_backup.tar.gz .

cd ../..

# Informações
SIZE=$(ls -lh enem_data_backup.tar.gz | awk '{print $5}')
echo ""
echo "✅ Dados compactados com sucesso!"
echo "📁 Arquivo: enem_data_backup.tar.gz"
echo "📊 Tamanho: $SIZE"
echo ""
echo "📤 Próximos passos:"
echo "1. Faça upload deste arquivo no Google Drive/OneDrive"
echo "2. No trabalho, baixe o arquivo"
echo "3. Execute: tar -xzf enem_data_backup.tar.gz -C backend/data/"
echo ""
