from rest_framework import viewsets

from er_card.models import ElectronicRehabilitationCard
from .serializers import *


class ElectronicRehabilitationCardViewSet(viewsets.ModelViewSet):
    queryset = ElectronicRehabilitationCard.objects.all()
    serializer_class = ElectronicRehabilitationCardSerializer