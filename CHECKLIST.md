# 📋 CHECKLIST RÁPIDO - Configurar no Trabalho

## 1️⃣ No GitHub (em qualquer lugar)
✅ Código está no repositório: `https://github.com/mandresoeiro/enem-intelligence`
✅ Arquivos grandes (microdados) **NÃO** estão no GitHub (ignorados)

## 2️⃣ Preparar os Microdados (em casa)

**Opção A - Cloud (Recomendado):**
```bash
# 1. Compactar os microdados
cd ~/dev/myprojects/Enem-Intelligence/backend/data
tar -czf microdados.tar.gz MICRODADOS_ENEM_*.csv

# 2. Upload no Google Drive/OneDrive/Dropbox
# Link de exemplo: https://drive.google.com/...
```

**Opção B - USB:**
- Copie `backend/data/MICRODADOS_ENEM_*.csv` para pen drive

**Opção C - Banco de Dados:**
```bash
cd backend
poetry run python manage.py dumpdata enem > dados_backup.json
# Envie dados_backup.json via cloud/email
```

## 3️⃣ No Trabalho - Setup

```bash
# 1. Clonar
git clone https://github.com/mandresoeiro/enem-intelligence.git
cd enem-intelligence

# 2. Instalar tudo automaticamente
./setup.sh

# 3. Baixar/transferir microdados
# - Se cloud: baixe e coloque em backend/data/
# - Se USB: copie para backend/data/
# - Se backup DB: poetry run python manage.py loaddata dados_backup.json

# 4. Rodar
# Terminal 1:
cd backend && poetry run python manage.py runserver

# Terminal 2:
cd frontend && npm run dev
```

Acesse: http://localhost:3000

## 🎯 RESUMO das Respostas

### ❓ GitHub vai ficar pesado?
**Não!** Os arquivos CSV não vão para o GitHub (.gitignore configurado)
- Repositório Git: ~10 MB
- Microdados (local): 3-5 GB

### ❓ Como acessar no trabalho?
1. Clone o repositório (rápido)
2. Execute `./setup.sh` (automatiza tudo)
3. Transfira os microdados separadamente (cloud/USB)

### ❓ E quem fez ENEM 2023?
**Funciona automaticamente!**
- Coloque `MICRODADOS_ENEM_2023.csv` em `backend/data/`
- O sistema busca em: 2024 → 2023 → 2022
- Importação: `poetry run python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2023.csv`

## 📦 Tamanhos

| Item | Tamanho | Onde |
|------|---------|------|
| Código (Git) | ~10 MB | GitHub ✅ |
| node_modules | ~500 MB | Local (auto) |
| Microdados 2024 | ~3 GB | Cloud/USB ⚠️ |
| Microdados 2023 | ~3 GB | Cloud/USB ⚠️ |
| DB exportado | ~100 MB | Cloud/Email ✅ |

## ⚡ Comandos Úteis

```bash
# Ver o que não está no Git
git status --ignored

# Verificar tamanho do repositório
du -sh .git

# Limpar arquivos não rastreados
git clean -xdf backend/data/raw/
```

## 🔗 Links Importantes

- **Repositório**: https://github.com/mandresoeiro/enem-intelligence
- **Microdados INEP**: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados
- **Documentação Completa**: Ver DEPLOYMENT.md
