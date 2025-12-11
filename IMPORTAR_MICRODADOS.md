# Importação de Microdados ENEM (2023 e 2024)

Este guia explica como importar dados do ENEM de múltiplos anos para o sistema.

## 📋 Pré-requisitos

- Microdados do ENEM baixados em:
  - `D:\micro-dados\microdados_enem_2023\`
  - `D:\micro-dados\microdados_enem_2024\`

## 🚀 Processo de Importação

### Passo 1: Copiar os arquivos para o projeto

Execute o script de cópia:

```bash
./copiar_microdados.sh
```

Isso copiará os arquivos de `D:\micro-dados\` para `backend/data/`.

### Passo 2: Importar para o banco de dados

#### Opção A: Importar todos os anos automaticamente

```bash
./importar_todos_microdados.sh
```

#### Opção B: Importar ano específico

```bash
cd backend

# Importar 2023
python manage.py importar_microdados_enem --csv data/MICRODADOS_ENEM_2023.csv --ano 2023

# Importar 2024
python manage.py importar_microdados_enem --csv data/MICRODADOS_ENEM_2024.csv --ano 2024
```

## 📊 Verificar dados importados

```bash
cd backend
python manage.py shell
```

No shell Python:

```python
from enem.models import EstatisticaEstado

# Ver anos disponíveis
EstatisticaEstado.objects.values('ano').distinct()

# Ver estatísticas de um ano específico
EstatisticaEstado.objects.filter(ano=2023)
EstatisticaEstado.objects.filter(ano=2024)

# Ver média de matemática por estado em 2024
EstatisticaEstado.objects.filter(ano=2024, area='matematica').values('estado', 'media_nota')
```

## 📁 Estrutura de arquivos esperada

```
backend/data/
├── MICRODADOS_ENEM_2023.csv (ou RESULTADOS_2023.csv)
├── MICRODADOS_ENEM_2024.csv (ou RESULTADOS_2024.csv)
├── PARTICIPANTES_2023.csv (opcional)
├── PARTICIPANTES_2024.csv (opcional)
├── ITENS_PROVA_2023.csv (opcional)
└── ITENS_PROVA_2024.csv (opcional)
```

## ⚙️ Usando Docker

Se estiver usando Docker:

```bash
# Copiar arquivos primeiro
./copiar_microdados.sh

# Importar via Docker
docker-compose exec backend python manage.py importar_microdados_enem --csv data/MICRODADOS_ENEM_2023.csv --ano 2023
docker-compose exec backend python manage.py importar_microdados_enem --csv data/MICRODADOS_ENEM_2024.csv --ano 2024
```

## 🔍 Notas

- O sistema detecta automaticamente o ano pelo nome do arquivo
- Os arquivos CSV grandes (1-2GB) podem demorar alguns minutos para processar
- Certifique-se de ter espaço suficiente em disco
- O `.gitignore` já está configurado para não versionar arquivos `.csv`

## 🆘 Problemas comuns

### Arquivo não encontrado
Verifique se os arquivos estão em `/mnt/d/micro-dados/` no WSL

### Erro de memória
Para arquivos muito grandes, considere processar em chunks ou usar um servidor com mais RAM

### Encoding incorreto
Os microdados do INEP usam `latin1` encoding, já configurado no comando
