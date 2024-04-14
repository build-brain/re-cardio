from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from src.ca_sheet.models import *


class MedicationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationGroup
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    group = MedicationGroupSerializer()

    class Meta:
        model = Medication
        fields = '__all__'

class ConditionAssessmentSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionAssessmentSheet
        fields = '__all__'

class FirstStageDataSerializer(serializers.ModelSerializer):
    medication_group = MedicationGroupSerializer()
    medication_name = MedicationSerializer()

    class Meta:
        model = FirstStageData
        fields = '__all__'

class SecondStageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondStageData
        fields = '__all__'

class MyocardialNecrosisBiochemicalMarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyocardialNecrosisBiochemicalMarker
        fields = '__all__'

class AdditionalTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalTestResult
        fields = '__all__'

class ThirdStageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdStageData
        fields = '__all__'

