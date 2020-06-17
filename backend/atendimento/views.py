from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from backend.atendimento.models import Especialidade
from backend.atendimento.serializers import EspecialidadeSerializer


class EspecialidadeViewSet(ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    search_fields = ('nome',)
    filter_backends = [SearchFilter, OrderingFilter]
    serializer_class = EspecialidadeSerializer
    permission_classes = (IsAuthenticated,)
