from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.response import Response

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
    
    queryset = ElectronicRehabilitationCard.objects.all().select_related('patient')
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

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ObjectDoesNotExist:
            error_message = "No admission data, GRACE requires admission_data"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        