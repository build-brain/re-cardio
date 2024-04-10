from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from api.management.serializers import AdmissionDataSerializer
from er_card.models import ElectronicRehabilitationCard


class ElectronicRehabilitationCardSerializer(serializers.ModelSerializer):
    admission_data = AdmissionDataSerializer()

    class Meta:
        model = ElectronicRehabilitationCard
        fields = '__all__'