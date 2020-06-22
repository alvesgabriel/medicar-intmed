from datetime import datetime

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from backend.atendimento.models import Agenda, Consulta, Especialidade, Medico
from backend.atendimento.serializers import (AgendaSerializer,
                                             ConsultaSerializer,
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


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (OrderingFilter,)
    allowed_methods = ('GET', 'POST', 'DELETE')

    def get_queryset(self):
        return Consulta.objects.filter(usuario=self.request.user)

    def create(self, request, *args, **kwargs):
        consulta = Consulta.objects.get(agenda_id=request.data.get('agenda_id'), horario=request.data.get('horario'))
        consulta.usuario = self.request.user
        consulta.save(*args, **kwargs)
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        agora = datetime.now().strftime('%Y-%m-%d %H:%M')
        consulta = Consulta.objects.filter(pk=self.kwargs.get('pk'), usuario=self.request.user, dia__gte=agora).first()
        if consulta is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        consulta.usuario = None
        consulta.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
