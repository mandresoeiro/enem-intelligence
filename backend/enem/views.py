from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Aluno, Curso, EstatisticaEstado, Inscricao, Simulado
from .serializers import (
    AlunoSerializer,
    CursoSerializer,
    EstatisticaEstadoSerializer,
    InscricaoSerializer,
    SimuladoSerializer,
)
from .utils import buscar_notas_por_cpf


class SimuladoViewSet(viewsets.ModelViewSet):
    queryset = Simulado.objects.all()
    serializer_class = SimuladoSerializer


class EstatisticaEstadoViewSet(viewsets.ModelViewSet):
    queryset = EstatisticaEstado.objects.all()
    serializer_class = EstatisticaEstadoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=False, methods=["post"])
    def buscar_notas_cpf(self, request):
        """
        Busca as notas de um aluno nos microdados do ENEM pelo CPF
        POST /api/enem/alunos/buscar_notas_cpf/
        Body: {"cpf": "12345678901"}
        """
        cpf = request.data.get("cpf")
        if not cpf:
            return Response(
                {"erro": "CPF é obrigatório"}, status=status.HTTP_400_BAD_REQUEST
            )

        notas = buscar_notas_por_cpf(cpf)
        if notas:
            return Response(notas, status=status.HTTP_200_OK)
        else:
            return Response(
                {"mensagem": "Notas não encontradas para este CPF"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def perform_create(self, serializer):
        """
        Ao criar um aluno, tenta buscar automaticamente as notas nos microdados
        """
        cpf = serializer.validated_data.get("cpf")
        notas = buscar_notas_por_cpf(cpf)

        if notas:
            # Se encontrou notas, preenche automaticamente
            if not serializer.validated_data.get("nota_enem_matematica"):
                serializer.validated_data["nota_enem_matematica"] = notas.get(
                    "nota_enem_matematica"
                )
            if not serializer.validated_data.get("nota_enem_linguagens"):
                serializer.validated_data["nota_enem_linguagens"] = notas.get(
                    "nota_enem_linguagens"
                )
            if not serializer.validated_data.get("nota_enem_ciencias"):
                serializer.validated_data["nota_enem_ciencias"] = notas.get(
                    "nota_enem_ciencias"
                )
            if not serializer.validated_data.get("nota_enem_humanas"):
                serializer.validated_data["nota_enem_humanas"] = notas.get(
                    "nota_enem_humanas"
                )
            if not serializer.validated_data.get("uf") and notas.get("uf"):
                serializer.validated_data["uf"] = notas.get("uf")

        serializer.save()


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
