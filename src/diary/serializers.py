from rest_framework import serializers

from src.diary.models import HealthDiaryRecord

from .choices import (
    BreathingRhythmChoices,
    DyspneaTypeChoices,
    FatigueTypeChoices,
    HeartPainTypeChoices,
)


class HealthDiaryRecordSerializer(serializers.ModelSerializer):
    
    """Health diary record model serializer"""
    
    class Meta:
        model = HealthDiaryRecord
        fields = '__all__'

        
class BodyTemperatureSerializer(serializers.Serializer):
    
    """Body temperature serializer"""
    
    body_temperature = serializers.FloatField(write_only=True)
    creation_date = serializers.DateField(write_only=True)


class ArterialPressureSerializer(serializers.Serializer):
    
    """Arterial pressure serializer"""

    systolic_pressure = serializers.FloatField(write_only=True)
    diastolic_pressure = serializers.FloatField(write_only=True)
    creation_date = serializers.DateField(write_only=True)


class PulseRateSerializer(serializers.Serializer):

    """Pulse rate serializer"""

    pulse_rate = serializers.FloatField(write_only=True)
    pulse_on_exertion = serializers.CharField(write_only=True)
    creation_date = serializers.DateField(write_only=True)


class BloodSaturationSerializer(serializers.Serializer):

    """Blood saturation serializer"""

    blood_saturation = serializers.FloatField(write_only=True)
    creation_date = serializers.DateField(write_only=True)


class RespiratoryRateSerializer(serializers.Serializer):
    
    """Respiratory rate serializer"""

    respiratory_rate = serializers.FloatField(write_only=True)
    breathing_rhythm = serializers.ChoiceField(choices=BreathingRhythmChoices, write_only=True)
    creation_date = serializers.DateField(write_only=True)


class RespiratoryConditionSerializer(serializers.Serializer):

    """Respiratory condition serializer"""
    
    moist_rales = serializers.BooleanField(write_only=True)
    peripheral_edema = serializers.BooleanField(write_only=True)
    creation_date = serializers.DateField(write_only=True)
    

class DyspneaSerializer(serializers.Serializer):

    """Dyspnea serializer"""

    dyspnea = serializers.BooleanField(write_only=True)
    dyspnea_type = serializers.ChoiceField(choices=DyspneaTypeChoices, write_only=True)
    creation_date = serializers.DateField(write_only=True)
    
    
class FatiueSerializer(serializers.Serializer):

    """Fatigue serializer"""

    fatigue = serializers.BooleanField(write_only=True)
    fatigue_type = serializers.ChoiceField(choices=FatigueTypeChoices, write_only=True)
    creation_date = serializers.DateField(write_only=True)


class HeartPainSerializer(serializers.Serializer):
    
    """Heart pain serializer"""

    heart_pain = serializers.BooleanField(write_only=True)
    heart_pain_type = serializers.ChoiceField(choices=HeartPainTypeChoices, write_only=True)
    creation_date = serializers.DateField(write_only=True)


class PhysicalActivitySerializer(serializers.Serializer):
    
    """Physical activity serializer"""
    
    walking_speed = serializers.FloatField(write_only=True)
    walking_duration = serializers.FloatField(write_only=True)
    distance_covered = serializers.FloatField(write_only=True)
    step_count = serializers.FloatField(write_only=True)
    borg_scale = serializers.IntegerField(write_only=True)
    creation_date = serializers.DateField(write_only=True)
