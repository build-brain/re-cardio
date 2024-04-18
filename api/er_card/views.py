from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from src.er_card.models import ElectronicRehabilitationCard
from .serializers import *


class ElectronicRehabilitationCardViewSet(viewsets.ModelViewSet):
    queryset = ElectronicRehabilitationCard.objects.all()
    serializer_class = ElectronicRehabilitationCardSerializer


class AdmissionDataViewSet(viewsets.ModelViewSet):
    queryset = AdmissionData.objects.all().\
        select_related('patient')\
            .select_related('preliminary_diagnosis')\
                .prefetch_related('attachments')
    serializer_class = AdmissionDataSerializer

    @swagger_auto_schema(method='post', request_body=AttachedFileSerializer)    
    @action(methods=['post'], detail=True)
    def attach_file(self, request, pk=None):
        admission_data = self.get_object()
        serializer = AttachedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(admission_data=admission_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(method='delete', request_body=None)
    @action(methods=['delete'], detail=True)
    def delete_file(self, request, pk=None):
        admission_data = self.get_object()  # Assuming get_object() returns the admission_data object
        
        file_id = request.data.get('file_id')
        
        try:
            attached_file = AttachedFile.objects.get(pk=file_id, admission_data=admission_data)
            attached_file.delete()
            return Response({"message": "File deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except AttachedFile.DoesNotExist:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
    

class InternationalClassificationOfDiseasesViewSet(viewsets.ModelViewSet):
    queryset = InternationalClassificationOfDiseases.objects.all()
    serializer_class = InternationalClassificationOfDiseasesSerializer
    pagination_class = None