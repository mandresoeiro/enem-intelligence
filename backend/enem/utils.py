"""
Utilitários para buscar dados nos microdados do ENEM
"""

import os
import glob

import pandas as pd
from django.conf import settings


def buscar_notas_por_cpf(cpf, ano=None):
    """
    Busca as notas de um aluno nos microdados do ENEM pelo número de inscrição
    NOTA: A nomenclatura 'cpf' é mantida para compatibilidade, mas recebe NU_INSCRICAO
    Otimizado para ler arquivos grandes em chunks

    Args:
        cpf (str): Número de inscrição do aluno (NU_INSCRICAO)
        ano (int, optional): Ano específico para buscar (2024, 2023, etc.).
                            Se None, busca em todos os anos disponíveis.

    Returns:
        dict: Dicionário com as notas ou None se não encontrado
    """
    # Remove formatação e espaços
    inscricao = "".join(filter(str.isdigit, str(cpf)))

    # Define os anos para buscar
    anos = [ano] if ano else [2024, 2023, 2022]

    # Tenta localizar os arquivos de microdados
    for ano_busca in anos:
        # Caminhos diretos comuns
        possible_paths = [
            os.path.join(settings.BASE_DIR, "data", f"MICRODADOS_ENEM_{ano_busca}.csv"),
            os.path.join(settings.BASE_DIR, "..", "data", f"MICRODADOS_ENEM_{ano_busca}.csv"),
            f"/tmp/microdados_enem/MICRODADOS_ENEM_{ano_busca}.csv",
            os.path.expanduser(f"~/enem_data/MICRODADOS_ENEM_{ano_busca}.csv"),
            f"/tmp/MICRODADOS_ENEM_{ano_busca}.csv",
        ]

        # Busca automática em estruturas extraídas dos microdados oficiais (raw/DADOS)
        raw_search_patterns = [
            os.path.join(settings.BASE_DIR, "data", "raw", "**", "DADOS", f"MICRODADOS_ENEM_{ano_busca}.csv"),
            os.path.join(settings.BASE_DIR, "..", "data", "raw", "**", "DADOS", f"MICRODADOS_ENEM_{ano_busca}.csv"),
            f"/tmp/microdados_enem/**/DADOS/MICRODADOS_ENEM_{ano_busca}.csv",
        ]

        csv_path = None
        for path in possible_paths:
            if os.path.exists(path):
                csv_path = path
                break

        # Se não encontrou nos caminhos diretos, tenta via glob nas pastas raw
        if not csv_path:
            for pattern in raw_search_patterns:
                matches = glob.glob(pattern, recursive=True)
                if matches:
                    # seleciona o primeiro match
                    csv_path = matches[0]
                    break

        if not csv_path:
            continue

        try:
            print(f"Buscando inscrição {inscricao} no arquivo {csv_path}...")
            
            # Lê o arquivo em chunks para otimizar performance
            chunk_size = 100000  # 100k linhas por vez
            
            for chunk in pd.read_csv(csv_path, sep=";", encoding="latin1", 
                                    low_memory=False, chunksize=chunk_size):
                # Busca o número de inscrição no chunk atual
                chunk["NU_INSCRICAO"] = chunk["NU_INSCRICAO"].astype(str)
                aluno_data = chunk[chunk["NU_INSCRICAO"] == inscricao]

                if not aluno_data.empty:
                    # Retorna as notas
                    row = aluno_data.iloc[0]
                    print(f"Inscrição encontrada no ano {ano_busca}!")
                    return {
                        "ano": ano_busca,
                        "inscricao": inscricao,
                        "nota_enem_matematica": (
                            float(row.get("NU_NOTA_MT", 0))
                            if pd.notna(row.get("NU_NOTA_MT"))
                            else None
                        ),
                        "nota_enem_linguagens": (
                            float(row.get("NU_NOTA_LC", 0))
                            if pd.notna(row.get("NU_NOTA_LC"))
                            else None
                        ),
                        "nota_enem_ciencias": (
                            float(row.get("NU_NOTA_CN", 0))
                            if pd.notna(row.get("NU_NOTA_CN"))
                            else None
                        ),
                        "nota_enem_humanas": (
                            float(row.get("NU_NOTA_CH", 0))
                            if pd.notna(row.get("NU_NOTA_CH"))
                            else None
                        ),
                        "uf": row.get("SG_UF_PROVA", ""),
                    }
            
            print(f"Inscrição não encontrada no arquivo do ano {ano_busca}")
                    
        except Exception as e:
            print(f"Erro ao buscar notas no arquivo {csv_path}: {e}")
            continue

    # Se chegou aqui, não encontrou em nenhum ano
    print(f"Inscrição {inscricao} não encontrada em nenhum arquivo de microdados")
    return None
