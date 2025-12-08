from django.core.management.base import BaseCommand

from enem.models import Aluno


class Command(BaseCommand):
    help = "Cria um aluno fake para testes"

    def handle(self, *args, **options):
        aluno, created = Aluno.objects.get_or_create(
            cpf="12345678901",
            defaults={
                "nome": "Aluno Teste",
                "uf": "SP",
                "nota_enem_linguagens": 650.0,
                "nota_enem_matematica": 700.0,
                "nota_enem_ciencias": 680.0,
                "nota_enem_humanas": 620.0,
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Aluno fake criado: {aluno.nome} (CPF: {aluno.cpf})"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Aluno já existe: {aluno.nome} (CPF: {aluno.cpf})")
            )
