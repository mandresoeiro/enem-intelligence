from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)
    uf = models.CharField(max_length=2)
    nota_linguagens = models.DecimalField(max_digits=5, decimal_places=2)
    nota_matematica = models.DecimalField(max_digits=5, decimal_places=2)
    nota_ciencias = models.DecimalField(max_digits=5, decimal_places=2)
    nota_humanas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    media_geral = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} → {self.curso.nome}"


class Estatistica(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ano = models.IntegerField()
    media_notas = models.DecimalField(max_digits=5, decimal_places=2)
    total_inscritos = models.IntegerField()

    def __str__(self):
        return f"{self.curso.nome} - {self.ano}"
