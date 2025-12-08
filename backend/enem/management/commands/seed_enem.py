# ==========================================================
# 🌱 Comando: seed_enem
# ==========================================================
# Gera dados falsos (seed) para o banco do ENEM Data Portal.
# - Cria alunos com notas realistas
# - Cria cursos e estatísticas
# - Cria inscrições aluno ↔ curso
# ==========================================================

from django.core.management.base import BaseCommand
from faker import Faker
from enem.models import Aluno, Curso, Inscricao, Estatistica
import random


# ==========================================================
# 🧠 Classe Principal — Comando Customizado do Django
# ==========================================================
# Este comando pode ser executado com:
#   poetry run python manage.py seed_enem
# Ele é ideal para popular o banco com dados de teste.
# ==========================================================
class Command(BaseCommand):
    help = "Popula o banco com dados falsos de Alunos, Cursos e Estatísticas"

    # ======================================================
    # 🏁 Método principal executado quando o comando roda
    # ======================================================
    def handle(self, *args, **options):
        fake = Faker("pt_BR")  # 🇧🇷 Gera nomes e CPFs no formato brasileiro

        self.stdout.write(self.style.SUCCESS("🌱 Iniciando geração de dados..."))

        # ==================================================
        # 🎯 Etapa 1 — Criar Cursos
        # ==================================================
        cursos = []
        areas = ["Engenharias", "Saúde", "Humanas", "Exatas", "Tecnologia", "Educação"]

        for _ in range(10):  # cria 10 cursos diferentes
            curso = Curso.objects.create(
                nome=fake.job(),  # exemplo: "Engenheiro Civil", "Professor de Física"
                area=random.choice(areas),
                media_geral=round(random.uniform(500, 900), 2),  # média simulada
            )
            cursos.append(curso)

        # ==================================================
        # 🎓 Etapa 2 — Criar Alunos
        # ==================================================
        alunos = []
        for _ in range(100):  # cria 100 alunos
            aluno = Aluno.objects.create(
                nome=fake.name(),  # nome aleatório
                cpf=fake.cpf(),  # CPF válido (formato brasileiro)
                uf=fake.estado_sigla(),  # ex: SP, RJ, MG
                nota_linguagens=round(random.uniform(400, 900), 2),
                nota_matematica=round(random.uniform(400, 900), 2),
                nota_ciencias=round(random.uniform(400, 900), 2),
                nota_humanas=round(random.uniform(400, 900), 2),
            )
            alunos.append(aluno)

        # ==================================================
        # 🧾 Etapa 3 — Criar Inscrições (Aluno ↔ Curso)
        # ==================================================
        # Cada aluno se inscreve em um curso aleatório.
        # ==================================================
        for aluno in alunos:
            Inscricao.objects.create(
                aluno=aluno,
                curso=random.choice(cursos),
            )

        # ==================================================
        # 📊 Etapa 4 — Criar Estatísticas por Curso/Ano
        # ==================================================
        # Gera 5 anos de estatísticas (2020–2024) para cada curso.
        # ==================================================
        for curso in cursos:
            for ano in range(2020, 2025):
                Estatistica.objects.create(
                    curso=curso,
                    ano=ano,
                    media_notas=round(random.uniform(500, 900), 2),
                    total_inscritos=random.randint(50, 300),
                )

        # ==================================================
        # ✅ Finalização
        # ==================================================
        # Exibe uma mensagem de sucesso no terminal.
        # ==================================================
        self.stdout.write(self.style.SUCCESS("✅ Banco populado com sucesso!"))


'''💡 Explicação dos blocos principais
Bloco	Função
Faker("pt_BR")	Gera nomes, CPFs e estados brasileiros corretamente formatados
Curso.objects.create(...)	Cria cursos com média geral simulada
Aluno.objects.create(...)	Cria alunos com notas ENEM realistas
Inscricao.objects.create(...)	Relaciona cada aluno a um curso
Estatistica.objects.create(...)	Gera dados anuais de desempenho
self.stdout.write(...)	Mostra mensagens no terminal com cores
# (sucesso, aviso, erro)'''
