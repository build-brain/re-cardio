from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from src.ca_sheet.models import *


class ComplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complication
        fields = '__all__'


class GraceScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraceScale
        fields = '__all__'


class ClinicalDiagnosisSerializer(serializers.ModelSerializer):
    complications_group_1 = ComplicationSerializer(many=True)
    complications_group_2 = ComplicationSerializer(many=True)
    complications_group_3 = ComplicationSerializer(many=True)
    grace = GraceScaleSerializer()

    class Meta:
        model = ClinicalDiagnosis
        fields = '__all__'


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
        fields = ['id', 'title', 'mnbm_date', 'file']


class AdditionalTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalTestResult
        fields = ['id', 'second_stage', 'title', 'file']
        read_only_fields = ['created_at', 'updated_at']


class ThirdStageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdStageData
        fields = '__all__'


class ConditionAssessmentSheetSerializer(serializers.ModelSerializer):
    first_stage = FirstStageDataSerializer()
    second_stage = SecondStageDataSerializer()
    third_stage = ThirdStageDataSerializer()
    clinical_diagnosis = ClinicalDiagnosisSerializer()

    class Meta:
        model = ConditionAssessmentSheet
        fields = '__all__'

