# 🏢 Guia: Como Usar no Trabalho

## 📥 Passo a Passo Completo

### 1. Clone o Repositório no Trabalho

```bash
git clone https://github.com/mandresoeiro/enem-intelligence.git
cd enem-intelligence
```

### 2. Execute o Setup Básico

```bash
./setup.sh
```

Isso vai:
- ✅ Instalar todas as dependências (poetry + npm)
- ✅ Executar migrações do banco
- ✅ Criar estrutura de pastas

### 3. Transferir os Dados (data/raw)

A pasta `data/raw/` contém os arquivos originais do INEP (provas, gabaritos, dicionários). Existem **3 opções** para transferir:

---

## 🎯 OPÇÃO 1: Compactar e Transferir via Cloud (RECOMENDADO)

### Em Casa:

```bash
cd ~/dev/myprojects/Enem-Intelligence/backend/data

# Compactar tudo
tar -czf enem_data_completo.tar.gz raw/ *.csv

# Verificar tamanho
ls -lh enem_data_completo.tar.gz
```

**Resultado:** ~500 MB a 1 GB compactado (bem menor que os 3-5 GB originais)

### Upload:
- **Google Drive**: Faça upload do `enem_data_completo.tar.gz`
- **OneDrive**: Faça upload do arquivo
- **Dropbox**: Faça upload do arquivo

### No Trabalho:

```bash
cd ~/enem-intelligence/backend/data

# Baixe o arquivo do cloud para aqui

# Descompactar
tar -xzf enem_data_completo.tar.gz

# Verificar
ls -la
# Deve ver: raw/ e MICRODADOS_ENEM_*.csv
```

---

## 🎯 OPÇÃO 2: USB/HD Externo

### Em Casa:

```bash
# Copiar para USB
cp -r ~/dev/myprojects/Enem-Intelligence/backend/data /media/seu-usb/enem_data/
```

### No Trabalho:

```bash
# Copiar do USB para o projeto
cp -r /media/seu-usb/enem_data/* ~/enem-intelligence/backend/data/
```

---

## 🎯 OPÇÃO 3: Baixar Direto no Trabalho (Mais Demorado)

Se preferir, pode baixar tudo novamente no trabalho:

```bash
cd ~/enem-intelligence/backend/data

# 1. Baixar microdados do INEP
wget https://download.inep.gov.br/microdados/microdados_enem_2024.zip

# 2. Descompactar
unzip microdados_enem_2024.zip -d raw/

# 3. Localizar os CSVs principais
find raw/ -name "*.csv" -type f
```

---

## 📂 Estrutura Esperada

Após transferir, sua pasta deve ficar assim:

```
backend/data/
├── raw/
│   └── enem_2024/
│       ├── DADOS/
│       │   ├── PARTICIPANTES_2024.csv
│       │   ├── RESULTADOS_2024.csv
│       │   └── ITENS_PROVA_2024.csv
│       ├── DICIONÁRIO/
│       ├── PROVAS E GABARITOS/
│       └── LEIA-ME E DOCUMENTOS TÉCNICOS/
├── MICRODADOS_ENEM_2024.csv  (se processado)
└── README.md
```

---

## 🚀 Verificar se Funcionou

```bash
# 1. Verificar arquivos
ls -lh backend/data/raw/

# 2. Tentar importar (teste)
cd backend
poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2024.csv

# 3. Iniciar servidor
poetry run python manage.py runserver
```

---

## 💡 Dica: Não Precisa de Tudo!

Se você **só quer testar** ou **não precisa das provas/gabaritos**, pode transferir **apenas** os CSVs:

```bash
# Apenas os arquivos necessários:
backend/data/
├── MICRODADOS_ENEM_2024.csv  ← Principal
└── README.md
```

Os arquivos em `raw/` são extras (provas, gabaritos, dicionários). O sistema funciona **sem eles** se você tiver os CSVs processados.

---

## ⚡ Tamanhos de Referência

| Item | Tamanho | Necessário? |
|------|---------|-------------|
| `MICRODADOS_ENEM_2024.csv` | ~3 GB | ✅ Sim |
| `raw/enem_2024/` (completo) | ~5 GB | ❌ Opcional |
| `raw/enem_2024/DADOS/` | ~3 GB | ✅ Se não tiver CSV |
| `raw/enem_2024/PROVAS/` | ~2 GB | ❌ Não essencial |
| Compactado `.tar.gz` | ~500 MB | 📦 Para transferir |

---

## 🔧 Resolver Problema: "CSV não encontrado"

Se aparecer erro ao buscar notas por CPF:

```bash
# Verifique se o CSV existe
ls -lh backend/data/MICRODADOS_ENEM_2024.csv

# Se não existir, mas você tem os dados raw:
cd backend/data/raw/enem_2024/DADOS/

# Copie o CSV principal
cp MICRODADOS_ENEM_2024.csv ../../
```

---

## 📝 Resumo Rápido

**Mais Simples (Apenas testes):**
1. Clone o repo
2. `./setup.sh`
3. Crie alunos manualmente (sem importar microdados)

**Completo (Com dados reais):**
1. Em casa: `tar -czf enem_data.tar.gz backend/data/`
2. Upload no Google Drive
3. No trabalho: baixe e descompacte
4. `./setup.sh`
5. Importe os dados

**Perguntas?** Veja `DEPLOYMENT.md` para mais detalhes!
