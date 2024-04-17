import mimetypes
from django.utils.translation import gettext_lazy as _


from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from rest_framework import serializers

from src.er_card.models import *


class InternationalClassificationOfDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalClassificationOfDiseases
        fields = '__all__'


class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = ['id', 'title', 'attachment']


class AdmissionDataSerializer(serializers.ModelSerializer):
    attachments = AttachedFileSerializer(many=True, read_only=True)
    class Meta:
        model = AdmissionData
        fields = '__all__'


class ElectronicRehabilitationCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectronicRehabilitationCard
        fields = '__all__'
        read_only_fields = ['admission_data',]

