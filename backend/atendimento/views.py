from datetime import datetime

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from backend.atendimento.models import Agenda, Especialidade, Medico
from backend.atendimento.serializers import (AgendaSerializer,
                                             EspecialidadeSerializer,
                                             MedicoSerializer)


class EspecialidadeViewSet(ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    search_fields = ('nome',)
    filter_backends = (SearchFilter, OrderingFilter)
    serializer_class = EspecialidadeSerializer
    permission_classes = (IsAuthenticated,)


class MedicoViewSet(ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    search_fields = ('nome',)
    serializer_class = MedicoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)

    def get_queryset(self):
        queryset = self.queryset

        especialidade = self.request.query_params.getlist('especialidade')
        if especialidade:
            return queryset.filter(especialidade__id__in=especialidade)
        return queryset


class AgendaViewSet(ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)

    def get_queryset(self):
        queryset = self.queryset
        hoje = datetime.now()

        medicos = self.request.query_params.getlist('medico')
        if medicos:
            queryset = queryset.filter(medico__id__in=medicos)

        especialidades = self.request.query_params.getlist('especialidade')
        if especialidades:
            queryset = queryset.filter(medico__especialidade__id__in=especialidades)

        data_inicio = self.request.query_params.get('data_inicio')
        data_final = self.request.query_params.get('data_final')
        if data_inicio and data_final:
            queryset = queryset.filter(dia__range=(data_inicio, data_final))
        else:
            queryset = queryset.filter(dia__gte=hoje.strftime('%Y-%m-%d'))

        queryset = queryset.order_by('dia')

        return queryset
