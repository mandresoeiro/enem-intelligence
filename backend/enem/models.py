from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)
    uf = models.CharField(max_length=2)
    # Notas do ENEM 2024 (importadas dos microdados)
    nota_enem_linguagens = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    nota_enem_matematica = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    nota_enem_ciencias = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    nota_enem_humanas = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.nome


class Simulado(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField()
    tipo = models.CharField(max_length=50)  # Ex: “Simulado 1”, “Teste Diagnóstico”
    nota_linguagens = models.DecimalField(max_digits=5, decimal_places=2)
    nota_matematica = models.DecimalField(max_digits=5, decimal_places=2)
    nota_ciencias = models.DecimalField(max_digits=5, decimal_places=2)
    nota_humanas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.aluno.nome} - {self.tipo} ({self.data})"


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    media_geral = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} → {self.curso.nome}"


# Estatísticas agregadas por estado
class EstatisticaEstado(models.Model):
    ano = models.IntegerField()
    estado = models.CharField(max_length=2)  # Ex: 'SP', 'RJ'
    area = models.CharField(max_length=20)  # Ex: 'matematica', 'linguagens', etc
    media_nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.estado} - {self.area} - {self.ano}"
