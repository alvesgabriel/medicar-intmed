from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from backend.atendimento.models import Especialidade, Medico
from backend.atendimento.serializers import (EspecialidadeSerializer,
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
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('especialidade',)
