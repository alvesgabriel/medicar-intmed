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


class ConsultaInline(admin.TabularInline):
    model = models.Consulta
    exclude = ('usuario', 'dia')


@admin.register(models.Agenda)
class AgendaAdmin(admin.ModelAdmin):
    fields = (('dia', 'medico'),)
    list_display = ('id', 'dia', 'medico')
    inlines = (ConsultaInline,)
