from rest_framework import serializers
from .models import Aluno, Curso, Inscricao, Estatistica

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = "__all__"


class EstatisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatistica
        fields = "__all__"
