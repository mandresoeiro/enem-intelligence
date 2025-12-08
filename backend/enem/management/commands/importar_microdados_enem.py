import pandas as pd
from django.core.management.base import BaseCommand

from enem.models import Aluno, EstatisticaEstado


class Command(BaseCommand):
    help = "Importa microdados ENEM 2024 para alunos e estatísticas por estado"

    def add_arguments(self, parser):
        parser.add_argument(
            "--csv",
            type=str,
            required=True,
            help="Caminho do arquivo CSV dos microdados ENEM 2024",
        )

    def handle(self, *args, **options):
        path = options["csv"]
        self.stdout.write(f"🔎 Lendo microdados: {path}")
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
            f"✅ Notas ENEM importadas para {count_importados} alunos cadastrados."
        )

        # Calcula médias por estado
        areas = [
            ("NU_NOTA_MT", "matematica"),
            ("NU_NOTA_LC", "linguagens"),
            ("NU_NOTA_CN", "ciencias"),
            ("NU_NOTA_CH", "humanas"),
        ]
        ano = 2024
        for estado, grupo in df.groupby("SG_UF_PROVA"):
            for col, area in areas:
                media = grupo[col].mean()
                EstatisticaEstado.objects.update_or_create(
                    ano=ano, estado=estado, area=area, defaults={"media_nota": media}
                )
        self.stdout.write(f"✅ Médias por estado calculadas e salvas.")
