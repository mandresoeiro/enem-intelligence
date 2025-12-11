#!/bin/bash

# Script para copiar microdados do ENEM de 2023 e 2024 do Windows para o projeto

echo "📦 Copiando microdados do ENEM..."

# Criar diretório se não existir
mkdir -p backend/data

# Copiar dados de 2024
echo "📊 Copiando dados de 2024..."
if [ -f "/mnt/d/micro-dados/microdados_enem_2024/DADOS/RESULTADOS_2024.csv" ]; then
    cp /mnt/d/micro-dados/microdados_enem_2024/DADOS/RESULTADOS_2024.csv backend/data/MICRODADOS_ENEM_2024.csv
    echo "✅ RESULTADOS_2024.csv copiado"
else
    echo "⚠️  Arquivo RESULTADOS_2024.csv não encontrado"
fi

if [ -f "/mnt/d/micro-dados/microdados_enem_2024/DADOS/PARTICIPANTES_2024.csv" ]; then
    cp /mnt/d/micro-dados/microdados_enem_2024/DADOS/PARTICIPANTES_2024.csv backend/data/
    echo "✅ PARTICIPANTES_2024.csv copiado"
fi

if [ -f "/mnt/d/micro-dados/microdados_enem_2024/DADOS/ITENS_PROVA_2024.csv" ]; then
    cp /mnt/d/micro-dados/microdados_enem_2024/DADOS/ITENS_PROVA_2024.csv backend/data/
    echo "✅ ITENS_PROVA_2024.csv copiado"
fi

# Copiar dados de 2023
echo "📊 Copiando dados de 2023..."
if [ -d "/mnt/d/micro-dados/microdados_enem_2023/DADOS" ]; then
    cp /mnt/d/micro-dados/microdados_enem_2023/DADOS/*.csv backend/data/ 2>/dev/null
    echo "✅ Dados de 2023 copiados"
else
    echo "⚠️  Diretório de dados 2023 não encontrado"
fi

# Listar arquivos copiados
echo ""
echo "📁 Arquivos na pasta backend/data:"
ls -lh backend/data/*.csv 2>/dev/null || echo "Nenhum arquivo CSV encontrado"

echo ""
echo "✅ Cópia concluída!"
