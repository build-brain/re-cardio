from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import (
    ElectronicRehabilitationCard,
    AdmissionData,
    InternationalClassificationOfDiseases,
    ERCardAttachment,
    AdmissionAttachment,
    ConditionAssessmentSheet,
    Complication
)


class InternationalClassificationOfDiseasesSerializer(serializers.ModelSerializer):

    """International classification of diseases model serializer"""

    class Meta:
        model = InternationalClassificationOfDiseases
        fields = '__all__'


class AdmissionAttachmentSerializer(serializers.ModelSerializer):

    """Admission attachment model serializer"""

    class Meta:
        model = AdmissionAttachment
        fields = '__all__'


class AdmissionDataSerializer(serializers.ModelSerializer):

    """Admission data model serializer"""

    preliminary_diagnosis = InternationalClassificationOfDiseasesSerializer(read_only=True)
    attachments = AdmissionAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = AdmissionData
        fields = '__all__'


class ERCardAttachmentSerializer(serializers.ModelSerializer):

    """ER card attachment model serializer"""

    class Meta:
        model = ERCardAttachment
        fields = '__all__'


class ElectronicRehabilitationCardSerializer(serializers.ModelSerializer):
    
    """Electronic rehabilitation card model serializer"""

    patient_avatar = serializers.ImageField(source="patient.avatar", read_only=True)
    patient_first_name = serializers.ReadOnlyField(source="patient.first_name")
    patient_last_name = serializers.ReadOnlyField(source="patient.last_name")
    patient_middle_name = serializers.ReadOnlyField(source="patient.middle_name")
    admission_data = AdmissionDataSerializer(read_only=True)
    attachments = ERCardAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = ElectronicRehabilitationCard
        fields = '__all__'


class ComplicationSerializer(serializers.ModelSerializer):

    """Complication model serializer"""

    class Meta:
        model = Complication
        fields = '__all__'


class ConditionAssessmentSheetSerializer(serializers.ModelSerializer):
    
    """Condition assessment sheet model serializer"""

    # complications = ComplicationSerializer(many=True)

    class Meta:
        model = ConditionAssessmentSheet
        fields = '__all__'