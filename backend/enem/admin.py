# ==========================================================
# 🧩 Admin do ENEM Data Portal
# ==========================================================
# Personaliza a visualização dos modelos no painel administrativo.
# ==========================================================

from django.contrib import admin
from .models import Aluno, Curso, Inscricao, Estatistica

# ==========================================================
# 🎓 Aluno
# ==========================================================
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf", "uf")
    search_fields = ("nome", "cpf")
    list_filter = ("uf",)
    ordering = ("nome",)


# ==========================================================
# 🎯 Curso
# ==========================================================
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "area", "media_geral")
    search_fields = ("nome", "area")
    ordering = ("nome",)


# ==========================================================
# 🧾 Inscrição
# ==========================================================
@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "curso", "data_inscricao")
    list_filter = ("curso",)
    search_fields = ("aluno__nome", "curso__nome")


# ==========================================================
# 📊 Estatística
# ==========================================================
@admin.register(Estatistica)
class EstatisticaAdmin(admin.ModelAdmin):
    list_display = ("id", "curso", "ano", "media_notas", "total_inscritos")
    list_filter = ("ano", "curso")
    ordering = ("-ano",)
