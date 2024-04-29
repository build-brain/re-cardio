from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from rest_framework import serializers

from src.er_card.models import er_card 
from src.er_card.models import diagnosis
from src.er_card.models import first_stage
from src.er_card.models import second_stage
from src.er_card.models import third_stage


class InternationalClassificationOfDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = er_card.InternationalClassificationOfDiseases
        fields = '__all__'


class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = er_card.AttachedFile
        fields = ['id', 'title', 'attachment']
    

class ElectronicRehabilitationCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = er_card.ElectronicRehabilitationCard
        fields = '__all__'


class AdmissionDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = er_card.AdmissionData
        fields = '__all__'


class ComplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = diagnosis.Complication
        fields = '__all__'


class GraceScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = diagnosis.GraceScale
        fields = '__all__'


class ClinicalDiagnosisSerializer(serializers.ModelSerializer):
    complications_group_1 = ComplicationSerializer(many=True)
    complications_group_2 = ComplicationSerializer(many=True)
    complications_group_3 = ComplicationSerializer(many=True)
    grace = GraceScaleSerializer()

    class Meta:
        model = diagnosis.ClinicalDiagnosis
        fields = '__all__'


class MedicationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = first_stage.MedicationGroup
        fields = '__all__'


class MedicationSerializer(serializers.ModelSerializer):
    group = MedicationGroupSerializer()

    class Meta:
        model = first_stage.Medication
        fields = '__all__'


class ConditionAssessmentSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = er_card.ConditionAssessmentSheet
        fields = '__all__'


class FirstStageDataSerializer(serializers.ModelSerializer):
    medication_group = MedicationGroupSerializer()
    medication_name = MedicationSerializer()

    class Meta:
        model = first_stage.FirstStageData
        fields = '__all__'


class SecondStageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = second_stage.SecondStageData
        fields = '__all__'


class MyocardialNecrosisBiochemicalMarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = second_stage.MyocardialNecrosisBiochemicalMarker
        fields = ['id', 'title', 'mnbm_date', 'file']


class AdditionalTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = second_stage.AdditionalTestResult
        fields = ['id', 'second_stage', 'title', 'file']
        read_only_fields = ['created_at', 'updated_at']


class ThirdStageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = third_stage.ThirdStageData
        fields = '__all__'


class ConditionAssessmentSheetSerializer(serializers.ModelSerializer):
    first_stage = FirstStageDataSerializer()
    second_stage = SecondStageDataSerializer()
    third_stage = ThirdStageDataSerializer()
    clinical_diagnosis = ClinicalDiagnosisSerializer()

    class Meta:
        model = er_card.ConditionAssessmentSheet
        fields = '__all__'

