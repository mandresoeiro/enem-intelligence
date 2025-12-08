# ==========================================================
# 🧩 Admin do ENEM Data Portal
# ==========================================================
# Personaliza a visualização dos modelos no painel administrativo.
# ==========================================================

from django.contrib import admin

from .models import Aluno, Curso, EstatisticaEstado, Inscricao, Simulado


# ==========================================================
# 🎓 Aluno
# ==========================================================
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "cpf",
        "uf",
        "nota_enem_matematica",
        "nota_enem_linguagens",
    )
    search_fields = ("nome", "cpf")
    list_filter = ("uf",)
    ordering = ("nome",)


# ==========================================================
# 📝 Simulado
# ==========================================================
@admin.register(Simulado)
class SimuladoAdmin(admin.ModelAdmin):
    list_display = ("id", "aluno", "tipo", "data", "nota_matematica", "nota_linguagens")
    list_filter = ("tipo", "data")
    search_fields = ("aluno__nome", "tipo")
    ordering = ("-data",)


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
# 📊 Estatística por Estado
# ==========================================================
@admin.register(EstatisticaEstado)
class EstatisticaEstadoAdmin(admin.ModelAdmin):
    list_display = ("id", "estado", "area", "ano", "media_nota")
    list_filter = ("ano", "estado", "area")
    ordering = ("-ano", "estado", "area")
