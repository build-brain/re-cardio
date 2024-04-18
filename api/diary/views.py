from django.db import IntegrityError
from django.utils.translation import gettext_lazy as _
    
from rest_framework import viewsets, status
from rest_framework.response import Response

from src.er_card.models import ElectronicRehabilitationCard
from src.diary.models import *

from .serializers import *
from .filters import *


class RecordViewSet(viewsets.ModelViewSet):
    queryset = HealthDiaryRecord.objects.all().select_related('physical_indicators', 'physical_activity')
    serializer_class = RecordSerializer


class PhysicalIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = PhysicalIndicators.objects.all()
    serializer_class = PhysicalIndicatorsSerializer
    filterset_class = PhysicalIndicatorsFilter
    
    def perform_create(self, serializer):
        if self.request.user.user_type == "PATIENT":
            patient = self.request.user
            try:
                er_card = ElectronicRehabilitationCard.objects.get(patient=patient, is_active=True)
                record, created = HealthDiaryRecord.objects.get_or_create(creation_date=date.today(), er_card=er_card)
                serializer.save(record=record)
            except IntegrityError:
                raise serializers.ValidationError({"error": "Record already exists"})
            except ElectronicRehabilitationCard.DoesNotExist:
                raise serializers.ValidationError({"error": "Patient does not have Electronic Rehabilitation Card."})
        else:
            raise serializers.ValidationError({"error": "User is not a patient."})
        
        
class PhysicalActivityViewSet(viewsets.ModelViewSet):
    queryset = PhysicalActivity.objects.all()
    serializer_class = PhysicalActivitySerializer
    filterset_class = PhysicalActivityFilter
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.user_type != "PATIENT":
            raise serializers.ValidationError({"error": _("User is not a patient.")})

        try:
            er_card = user.er_cards.get(is_active=True)
            record, created = HealthDiaryRecord.objects.get_or_create(
                creation_date=date.today(),
                er_card=er_card
            )
            serializer.save(record=record)
        except ElectronicRehabilitationCard.DoesNotExist:
            raise serializers.ValidationError({"error": _("Patient does not have Electronic Rehabilitation Card.")})
        except IntegrityError:
            raise serializers.ValidationError({"error": _("Record already exists")})

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)