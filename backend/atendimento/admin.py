from django.contrib import admin

from backend.atendimento import models


@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_filter = ('nome',)


@admin.register(models.Medico)
class MedicoAdin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm')
    list_filter = ('nome', 'crm')
