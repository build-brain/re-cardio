from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema

from .models import (
    ElectronicRehabilitationCard,
    AdmissionData,
    InternationalClassificationOfDiseases,
    AdmissionAttachment,
    ERCardAttachment,
    ConditionAssessmentSheet,
    Complication,
)
from .serializers import (
    ElectronicRehabilitationCardSerializer,
    AdmissionDataSerializer,
    InternationalClassificationOfDiseasesSerializer,
    AdmissionAttachmentSerializer,
    ERCardAttachmentSerializer,
    ConditionAssessmentSheetSerializer,
    ComplicationSerializer,
)


class ElectronicRehabilitationCardViewSet(viewsets.ModelViewSet):

    """Electronic rehabilitation card model view set"""
    
    queryset = ElectronicRehabilitationCard.objects.all()
    serializer_class = ElectronicRehabilitationCardSerializer


class AdmissionDataViewSet(viewsets.ModelViewSet):

    """Admission data model view set"""

    queryset = AdmissionData.objects.all()
    serializer_class = AdmissionDataSerializer


class InternationalClassificationOfDiseasesViewSet(viewsets.ModelViewSet):

    """International classification of diseases model view set"""

    queryset = InternationalClassificationOfDiseases.objects.all()
    serializer_class = InternationalClassificationOfDiseasesSerializer
    

class AdmissionAttachmentViewSet(viewsets.ModelViewSet):

    """Admission attachment model view set"""

    queryset = AdmissionAttachment.objects.all()
    serializer_class = AdmissionAttachmentSerializer
    

class ERCardAttachmentViewSet(viewsets.ModelViewSet):

    """ER card attachment model view set"""
    
    queryset = ERCardAttachment.objects.all()
    serializer_class = ERCardAttachmentSerializer
    

class ComplicationViewSet(viewsets.ModelViewSet):
    
    """Complication model view set"""
    
    queryset = Complication.objects.all()
    serializer_class = ComplicationSerializer


class ConditionAssessmentSheetViewSet(viewsets.ModelViewSet):

    """Condition assessment sheet model view set"""

    queryset = ConditionAssessmentSheet.objects.all()
    serializer_class = ConditionAssessmentSheetSerializer
        