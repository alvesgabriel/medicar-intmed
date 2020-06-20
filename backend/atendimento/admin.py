from django.contrib import admin

from backend.atendimento import models


@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_filter = ('nome',)


@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm')
    list_filter = ('nome', 'crm')


@admin.register(models.Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'dia', 'medico')
