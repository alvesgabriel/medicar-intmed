from django.core.validators import RegexValidator
from django.db import models

from backend.core.models import User


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.nome}'


class Medico(models.Model):
    crm = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)
    telefone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Número de telefone deve ter o formato: '+999999999'. Máximo 15 dígitos.")
    telefone = models.CharField(validators=[telefone_regex], max_length=17, blank=True, null=True)

    def __str__(self):
        return f'{self.id}: {self.nome}'


class Agenda(models.Model):
    dia = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)


class Consulta(models.Model):
    dia = models.DateTimeField()
    horario = models.TimeField()
    agenda = models.ForeignKey(Agenda, related_name='horarios', on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.dia is None:
            agenda = Agenda.objects.get(pk=self.agenda.id)
            self.dia = agenda.dia.strftime(f'%Y-%m-%d {self.horario}')
        super(Consulta, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.horario}'
