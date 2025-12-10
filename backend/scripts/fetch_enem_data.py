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
import argparse
import sys

# ----------------------------------------------------------
# 📁 Diretórios
# ----------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------
# 🌐 URL base dos microdados
# ----------------------------------------------------------
INEP_BASE = (
    "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem"
)
DOWNLOAD_BASE = "https://download.inep.gov.br/microdados"


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


def build_direct_download_url(year: int) -> str:
    """Constroi URL direta de download para um ano específico.
    Ex.: 2022 -> https://download.inep.gov.br/microdados/microdados_enem_2022.zip
    """
    return f"{DOWNLOAD_BASE}/microdados_enem_{year}.zip"


# ----------------------------------------------------------
# 💾 Função: baixar e extrair microdados
# ----------------------------------------------------------
def download_and_extract(
    url, year, out_dir: Path | None = None, sample_rows: int | None = None
):
    print(f"📥 Baixando microdados ENEM {year}...")
    resp = requests.get(url, stream=True)
    if resp.status_code != 200:
        raise Exception(f"❌ Erro ao baixar: {resp.status_code}")

    target_dir = out_dir or DATA_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    zip_path = target_dir / f"microdados_enem_{year}.zip"
    zip_path.write_bytes(resp.content)
    print(f"✅ Arquivo salvo em: {zip_path}")

    print("📦 Extraindo arquivos...")
    extract_dir = target_dir / f"enem_{year}"
    with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
        z.extractall(extract_dir)

    print(f"✅ Extração concluída em {extract_dir}")

    # Amostra opcional para desenvolvimento: cria um CSV reduzido (1% ou N linhas)
    if sample_rows and sample_rows > 0:
        try:
            import pandas as pd

            dados_dir = next(
                (p for p in extract_dir.glob("**/DADOS") if p.is_dir()), None
            )
            if not dados_dir:
                print("⚠️ Pasta DADOS não encontrada para geração de amostra.")
                return
            # procura principal microdados CSV
            csv_files = list(dados_dir.glob("MICRODADOS_ENEM_*.csv"))
            if not csv_files:
                print("⚠️ Arquivo MICRODADOS_ENEM_*.csv não encontrado para amostra.")
                return
            src_csv = csv_files[0]
            print(f"🔎 Gerando amostra de {sample_rows} linhas de {src_csv.name}...")
            df = pd.read_csv(src_csv, sep=";", encoding="latin1", nrows=sample_rows)
            sample_path = extract_dir / f"amostra_{year}.csv"
            df.to_csv(sample_path, index=False)
            print(f"✅ Amostra salva em: {sample_path}")
        except Exception as e:
            print(f"⚠️ Falha ao gerar amostra: {e}")


# ----------------------------------------------------------
# 🚀 Execução principal
# ----------------------------------------------------------
if __name__ == "__main__":
    print(f"\n=== ENEM Data Downloader [{datetime.date.today()}] ===\n")

    parser = argparse.ArgumentParser(
        description="Baixa e extrai microdados do ENEM para um ano específico ou o mais recente."
    )
    parser.add_argument(
        "--year", type=int, help="Ano alvo (ex.: 2022). Se omitido, usa o mais recente."
    )
    parser.add_argument(
        "--out",
        type=str,
        default=str(DATA_DIR),
        help="Diretório de saída (default: backend/data/raw)",
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=0,
        help="Gera amostra com N linhas do CSV principal (opcional)",
    )
    args = parser.parse_args()

    try:
        if args.year:
            year = args.year
            url = build_direct_download_url(year)
            print(f"🔗 URL direta: {url}")
        else:
            url, year = get_latest_enem_link()

        download_and_extract(
            url,
            year,
            Path(args.out),
            args.sample if args.sample and args.sample > 0 else None,
        )
        print("\n🎉 Download e extração concluídos com sucesso!")
    except Exception as e:
        print(f"\n⚠️ Erro: {e}")
        sys.exit(1)
