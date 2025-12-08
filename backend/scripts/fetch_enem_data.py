# ==========================================================
# 🎓 ENEM Data Portal — Download Automático de Microdados
# ==========================================================
# Este script:
# 1. Verifica o link mais recente de microdados no site do INEP;
# 2. Faz o download do arquivo ZIP (2024, se disponível);
# 3. Extrai o conteúdo em /data/raw/ para processamento posterior.
# ==========================================================

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import zipfile
import io
import datetime

# ----------------------------------------------------------
# 📁 Diretórios
# ----------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------
# 🌐 URL base dos microdados
# ----------------------------------------------------------
INEP_BASE = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem"

# ----------------------------------------------------------
# 🔍 Função: localizar link mais recente de microdados
# ----------------------------------------------------------
def get_latest_enem_link():
    print("🔎 Buscando microdados disponíveis no site do INEP...")
    resp = requests.get(INEP_BASE)
    soup = BeautifulSoup(resp.text, "html.parser")

    # Procura links que contenham "microdados_enem"
    links = [
        a["href"]
        for a in soup.find_all("a", href=True)
        if "microdados_enem" in a["href"].lower() and a["href"].endswith(".zip")
    ]

    if not links:
        raise Exception("❌ Nenhum link de microdados encontrado.")

    # Ordena por ano
    links_sorted = sorted(links, reverse=True)
    latest_link = links_sorted[0]

    year = "".join(filter(str.isdigit, latest_link))
    print(f"✅ Último conjunto disponível: ENEM {year}")
    return latest_link, year

# ----------------------------------------------------------
# 💾 Função: baixar e extrair microdados
# ----------------------------------------------------------
def download_and_extract(url, year):
    print(f"📥 Baixando microdados ENEM {year}...")
    resp = requests.get(url, stream=True)
    if resp.status_code != 200:
        raise Exception(f"❌ Erro ao baixar: {resp.status_code}")

    zip_path = DATA_DIR / f"microdados_enem_{year}.zip"
    zip_path.write_bytes(resp.content)
    print(f"✅ Arquivo salvo em: {zip_path}")

    print("📦 Extraindo arquivos...")
    with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
        z.extractall(DATA_DIR / f"enem_{year}")

    print(f"✅ Extração concluída em {DATA_DIR / f'enem_{year}'}")

# ----------------------------------------------------------
# 🚀 Execução principal
# ----------------------------------------------------------
if __name__ == "__main__":
    print(f"\n=== ENEM Data Downloader [{datetime.date.today()}] ===\n")

    try:
        link, year = get_latest_enem_link()
        download_and_extract(link, year)
        print("\n🎉 Download e extração concluídos com sucesso!")
    except Exception as e:
        print(f"\n⚠️ Erro: {e}")
