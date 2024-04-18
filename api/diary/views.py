from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.response import Response

from src.management.models import Patient
from src.er_card.models import ElectronicRehabilitationCard
from src.diary.models import *
from .serializers import *


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class PhysicalIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = PhysicalIndicators.objects.all()
    serializer_class = PhysicalIndicatorsSerializer
    
    def perform_create(self, serializer):
        if self.request.user.user_type == "PATIENT":
            patient = self.request.user
            try:
                er_card = ElectronicRehabilitationCard.objects.get(patient=patient, is_active=True)
                record, created = Record.objects.get_or_create(creation_date=date.today(), er_card=er_card)
                serializer.save(record=record)
            except ElectronicRehabilitationCard.DoesNotExist:
                raise serializers.ValidationError({"error": "Patient does not have Electronic Rehabilitation Card."})
        else:
            raise serializers.ValidationError({"error": "User is not a patient."})
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response({"error": "Record already exists"}, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        
class PhysicalActivityViewSet(viewsets.ModelViewSet):
    queryset = PhysicalActivity.objects.all()
    serializer_class = PhysicalActivitySerializer
    
    def perform_create(self, serializer):
        if self.request.user.user_type == "PATIENT":
            patient = self.request.user
            try:
                er_card = ElectronicRehabilitationCard.objects.get(patient=patient, is_active=True)
                record, created = Record.objects.get_or_create(creation_date=date.today(), er_card=er_card)
                serializer.save(record=record)
            except ElectronicRehabilitationCard.DoesNotExist:
                raise serializers.ValidationError({"error": "Patient does not have Electronic Rehabilitation Card."})
        else:
            raise serializers.ValidationError({"error": "User is not a patient."})
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response({"error": "Record already exists"}, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    # def perform_create(self, serializer):
    #     # Проверяем, является ли пользователь пациентом
    #     if self.request.user.user_type == "PATIENT":
    #         patient = self.request.user
    #         # Получаем активную карту реабилитации пациента
    #         er_card = patient.er_cards.filter(is_active=True).last()
    #         # Получаем или создаем запись Record для текущего дня и карты реабилитации
    #         record, created = Record.objects.get_or_create(creation_date=date.today(), er_card=er_card)
    #         serializer.save(record=record)
    #     else:
    #         raise serializers.ValidationError({"error": "User type is not patient."})