from rest_framework import serializers

from backend.atendimento.models import Agenda, Especialidade, Medico


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('id', 'nome')


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ('id', 'nome', 'crm', 'email', 'telefone', 'especialidade')


class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer(read_only=True)

    class Meta:
        model = Agenda
        fields = ('id', 'dia', 'horarios', 'medico')
