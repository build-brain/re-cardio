from rest_framework import viewsets

from ca_sheet.models import *
from .serializers import *

class MedicationGroupViewSet(viewsets.ModelViewSet):
    queryset = MedicationGroup.objects.all()
    serializer_class = MedicationGroupSerializer
    

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class ConditionAssessmentSheetViewSet(viewsets.ModelViewSet):
    queryset = ConditionAssessmentSheet.objects.all()
    serializer_class = ConditionAssessmentSheetSerializer


class FirstStageDataViewSet(viewsets.ModelViewSet):
    queryset = FirstStageData.objects.all()
    serializer_class = FirstStageDataSerializer


class SecondStageDataViewSet(viewsets.ModelViewSet):
    queryset = SecondStageData.objects.all()
    serializer_class = SecondStageDataSerializer


class MyocardialNecrosisBiochemicalMarkerViewSet(viewsets.ModelViewSet):
    queryset = MyocardialNecrosisBiochemicalMarker.objects.all()
    serializer_class = MyocardialNecrosisBiochemicalMarkerSerializer


class AdditionalTestResultViewSet(viewsets.ModelViewSet):
    queryset = AdditionalTestResult.objects.all()
    serializer_class = AdditionalTestResultSerializer


class ThirdStageDataViewSet(viewsets.ModelViewSet):
    queryset = ThirdStageData.objects.all()
    serializer_class = ThirdStageDataSerializer
    
