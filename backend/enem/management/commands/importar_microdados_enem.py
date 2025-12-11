import re
import pandas as pd
from django.core.management.base import BaseCommand

from enem.models import Aluno, EstatisticaEstado


class Command(BaseCommand):
    help = "Importa microdados ENEM (2023, 2024 ou outros anos) para alunos e estatísticas por estado"

    def add_arguments(self, parser):
        parser.add_argument(
            "--csv",
            type=str,
            required=True,
            help="Caminho do arquivo CSV dos microdados ENEM",
        )
        parser.add_argument(
            "--ano",
            type=int,
            default=None,
            help="Ano dos dados (extraído automaticamente do nome do arquivo se não fornecido)",
        )

    def handle(self, *args, **options):
        path = options["csv"]
        ano = options["ano"]
        
        # Tenta extrair o ano do nome do arquivo se não foi fornecido
        if not ano:
            match = re.search(r"20\d{2}", path)
            if match:
                ano = int(match.group())
            else:
                ano = 2024  # Default
        
        self.stdout.write(f"🔎 Lendo microdados do ENEM {ano}: {path}")
        df = pd.read_csv(path, sep=";", encoding="latin1", low_memory=False)

        # Importa notas ENEM para alunos já cadastrados
        alunos_cadastrados = {a.cpf: a for a in Aluno.objects.all()}
        count_importados = 0
        for _, row in df.iterrows():
            cpf = str(row.get("NU_CPF", "")).zfill(11)
            aluno = alunos_cadastrados.get(cpf)
            if aluno:
                aluno.nota_enem_linguagens = row.get("NU_NOTA_LC", 0)
                aluno.nota_enem_matematica = row.get("NU_NOTA_MT", 0)
                aluno.nota_enem_ciencias = row.get("NU_NOTA_CN", 0)
                aluno.nota_enem_humanas = row.get("NU_NOTA_CH", 0)
                aluno.save()
                count_importados += 1
        self.stdout.write(
            f"✅ Notas ENEM {ano} importadas para {count_importados} alunos cadastrados."
        )

        # Calcula médias por estado
        areas = [
            ("NU_NOTA_MT", "matematica"),
            ("NU_NOTA_LC", "linguagens"),
            ("NU_NOTA_CN", "ciencias"),
            ("NU_NOTA_CH", "humanas"),
        ]
        for estado, grupo in df.groupby("SG_UF_PROVA"):
            for col, area in areas:
                media = grupo[col].mean()
                EstatisticaEstado.objects.update_or_create(
                    ano=ano, estado=estado, area=area, defaults={"media_nota": media}
                )
        self.stdout.write(f"✅ Médias por estado do ENEM {ano} calculadas e salvas.")
