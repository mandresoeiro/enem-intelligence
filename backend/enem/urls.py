from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AlunoViewSet,
    CursoViewSet,
    EstatisticaEstadoViewSet,
    InscricaoViewSet,
    SimuladoViewSet,
)

router = DefaultRouter()
router.register(r"alunos", AlunoViewSet)
router.register(r"cursos", CursoViewSet)
router.register(r"inscricoes", InscricaoViewSet)
router.register(r"simulados", SimuladoViewSet)
router.register(r"estatisticas-estado", EstatisticaEstadoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
