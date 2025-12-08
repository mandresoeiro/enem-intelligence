# ⚡ Quick Start - Configurar no Trabalho

## 🏠 EM CASA (antes de ir pro trabalho)

```bash
cd ~/dev/myprojects/Enem-Intelligence
./preparar_dados.sh
```

Isso cria: `enem_data_backup.tar.gz` (~500 MB)

📤 **Upload no Google Drive/OneDrive**

---

## 🏢 NO TRABALHO

### 1. Clone + Setup (5 min)
```bash
git clone https://github.com/mandresoeiro/enem-intelligence.git
cd enem-intelligence
./setup.sh
```

### 2. Baixar + Restaurar Dados (10 min)
```bash
# Baixe enem_data_backup.tar.gz do cloud

# Extrair
tar -xzf ~/Downloads/enem_data_backup.tar.gz -C backend/data/

# Verificar
ls backend/data/
# Deve ver: raw/ e MICRODADOS_ENEM_*.csv
```

### 3. Rodar (1 min)
```bash
# Terminal 1
cd backend && poetry run python manage.py runserver

# Terminal 2  
cd frontend && npm run dev
```

**Acesse:** http://localhost:3000

---

## 🎯 Alternativa: SEM dados/raw

Se você **não precisa** das provas/gabaritos extras:

```bash
# 1. Clone + setup
git clone https://github.com/mandresoeiro/enem-intelligence.git
cd enem-intelligence
./setup.sh

# 2. Use apenas o sistema sem importar microdados
#    (cadastre alunos manualmente pelo formulário)

# 3. Rodar
cd backend && poetry run python manage.py runserver
cd frontend && npm run dev
```

Sistema funciona **perfeitamente** sem os microdados!
A busca automática por CPF simplesmente não encontrará dados.

---

## 📚 Documentação Completa

- **TRABALHO.md** ← Guia detalhado sobre data/raw
- **DEPLOYMENT.md** ← Deploy completo
- **CHECKLIST.md** ← Checklist passo a passo
- **README.md** ← Visão geral do projeto

---

## 💡 Dica Pro

Se no trabalho você tem internet boa:

```bash
# Baixar microdados direto (3 GB)
cd backend/data
wget https://download.inep.gov.br/microdados/microdados_enem_2024.zip
unzip microdados_enem_2024.zip
```

Pronto! ✨
