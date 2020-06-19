from django.core.validators import RegexValidator
from django.db import models


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
