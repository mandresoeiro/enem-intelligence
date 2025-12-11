#!/bin/bash

# Script para importar microdados do ENEM de múltiplos anos

echo "📊 Iniciando importação de microdados do ENEM..."

cd backend

# Importar dados de 2023
if [ -f "data/MICRODADOS_ENEM_2023.csv" ] || [ -f "data/RESULTADOS_2023.csv" ]; then
    echo "📥 Importando dados de 2023..."
    
    if [ -f "data/RESULTADOS_2023.csv" ]; then
        python manage.py importar_microdados_enem --csv data/RESULTADOS_2023.csv --ano 2023
    elif [ -f "data/MICRODADOS_ENEM_2023.csv" ]; then
        python manage.py importar_microdados_enem --csv data/MICRODADOS_ENEM_2023.csv --ano 2023
    fi
else
    echo "⚠️  Nenhum arquivo de 2023 encontrado"
fi

# Importar dados de 2024
if [ -f "data/MICRODADOS_ENEM_2024.csv" ] || [ -f "data/RESULTADOS_2024.csv" ]; then
    echo "📥 Importando dados de 2024..."
    
    if [ -f "data/RESULTADOS_2024.csv" ]; then
        python manage.py importar_microdados_enem --csv data/RESULTADOS_2024.csv --ano 2024
    elif [ -f "data/MICRODADOS_ENEM_2024.csv" ]; then
        python manage.py importar_microdados_enem --csv data/MICRODADOS_ENEM_2024.csv --ano 2024
    fi
else
    echo "⚠️  Nenhum arquivo de 2024 encontrado"
fi

echo ""
echo "✅ Importação concluída!"
echo ""
echo "📊 Para ver as estatísticas importadas, execute:"
echo "   python manage.py shell"
echo "   >>> from enem.models import EstatisticaEstado"
echo "   >>> EstatisticaEstado.objects.values('ano').distinct()"
