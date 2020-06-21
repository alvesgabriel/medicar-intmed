from datetime import datetime

from rest_framework import serializers

from backend.atendimento.models import Agenda, Consulta, Especialidade, Medico


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('id', 'nome')


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(read_only=True)

    class Meta:
        model = Medico
        fields = ('id', 'nome', 'crm', 'email', 'telefone', 'especialidade')


class HorarioList(serializers.ListSerializer):
    def to_representation(self, data):
        agora = datetime.now().strftime('15:00:00')
        return data.queryset.filter(horario__gte=agora)


class HorarioSerializer(serializers.ModelSerializer):
    horario = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Consulta
        fields = ('horario',)


class AgendaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer(read_only=True)
    horarios = serializers.SerializerMethodField('get_horarios')

    def get_horarios(self, agenda):
        agora = datetime.now().strftime('%Y-%m-%d %H:%M')
        queryset = Consulta.objects.filter(agenda__id=agenda.id, dia__gte=agora, usuario__isnull=True)
        serializer = HorarioSerializer(instance=queryset, many=True)
        data = [horario.get('horario') for horario in serializer.data]
        return data

    class Meta:
        model = Agenda
        fields = ('id', 'dia', 'horarios', 'medico')
