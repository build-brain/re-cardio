from rest_framework import serializers

from src.diary.models import *


class PhysicalIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalIndicators
        fields = '__all__'

class PhysicalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalActivity
        fields = '__all__'
        read_only_fields = ['record']

class RecordSerializer(serializers.ModelSerializer):
    physical_indicators = PhysicalIndicatorsSerializer(read_only=True)
    physical_activity = PhysicalActivitySerializer(read_only=True)
    class Meta:
        model = HealthDiaryRecord
        fields = '__all__'
        read_only_fields = ['physical_indicators', 'physical_activity']