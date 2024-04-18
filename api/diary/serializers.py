from rest_framework import serializers

from src.diary.models import *


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class PhysicalIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalIndicators
        fields = '__all__'

class PhysicalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalActivity
        fields = '__all__'
        read_only_fields = ['record']