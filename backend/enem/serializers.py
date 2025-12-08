from rest_framework import serializers

from .models import Aluno, Curso, EstatisticaEstado, Inscricao, Simulado


class SimuladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulado
        fields = "__all__"


class EstatisticaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatisticaEstado
        fields = "__all__"


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
