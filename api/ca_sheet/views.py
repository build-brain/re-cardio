from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from src.ca_sheet.models import *
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

    @swagger_auto_schema(method='post', request_body=MyocardialNecrosisBiochemicalMarkerSerializer)    
    @action(methods=['post'], detail=True)
    def add_mnbm(self, request, pk=None):
        second_stage = self.get_object()
        serializer = MyocardialNecrosisBiochemicalMarkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(second_stage=second_stage)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(method='delete', request_body=None)
    @action(methods=['delete'], detail=True)
    def delete_mnbm(self, request, pk=None):
        second_stage = self.get_object()  # Assuming get_object() returns the second_stage object
        
        mnbm_id = request.data.get('mnbm_id')
        
        try:
            mbnm = MyocardialNecrosisBiochemicalMarker.objects.get(pk=mnbm_id, second_stage=second_stage)
            mbnm.delete()
            return Response({"message": "MNBM deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except MyocardialNecrosisBiochemicalMarker.DoesNotExist:
            return Response({"error": "MBNM not found."}, status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(method='post', request_body=AdditionalTestResultSerializer)    
    @action(methods=['post'], detail=True)
    def add_test_result(self, request, pk=None):
        second_stage = self.get_object()
        serializer = AdditionalTestResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(second_stage=second_stage)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(method='delete', request_body=None)
    @action(methods=['delete'], detail=True)
    def delete_test_result(self, request, pk=None):
        second_stage = self.get_object()  # Assuming get_object() returns the second_stage object
        
        test_result_id = request.data.get('test_result_id')
        
        try:
            mbnm = AdditionalTestResult.objects.get(pk=test_result_id, second_stage=second_stage)
            mbnm.delete()
            return Response({"message": "Test result deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except AdditionalTestResult.DoesNotExist:
            return Response({"error": "Test result not found."}, status=status.HTTP_404_NOT_FOUND)


class ThirdStageDataViewSet(viewsets.ModelViewSet):
    queryset = ThirdStageData.objects.all()
    serializer_class = ThirdStageDataSerializer
    
    
class ClinicalDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = ClinicalDiagnosis.objects.all()
    serializer_class = ClinicalDiagnosisSerializer


    
