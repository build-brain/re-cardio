from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import *


class HealthDiaryRecord(models.Model):

    """Health diary model"""
    
    creation_date = models.DateField(verbose_name=_("Creation Date"), auto_now_add=True, unique=True)
    er_card = models.ForeignKey(verbose_name=_("ER Card"), to="er_card.ElectronicRehabilitationCard", on_delete=models.CASCADE, related_name="records")
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("Health Diary Record")
        verbose_name_plural = _("Health Diary Records")
        

class PhysicalIndicators(models.Model):

    """Physical indicators model"""
    
    record = models.OneToOneField(verbose_name=_("Record"), to=HealthDiaryRecord, on_delete=models.CASCADE, related_name="physical_indicators", unique=True)
    general_condition = models.CharField(verbose_name=_("General Condition"), max_length=20, choices=GeneralConditionChoices.choices, null=True, blank=True)
    body_temperature = models.FloatField(verbose_name=_("Body Temperature (°C)"), null=True, blank=True)
    systolic_pressure = models.FloatField(verbose_name=_("Systolic Blood Pressure (mmHg)"), null=True, blank=True)
    diastolic_pressure = models.FloatField(verbose_name=_("Diastolic Blood Pressure (mmHg)"), null=True, blank=True)
    pulse_rate = models.FloatField(verbose_name=_("Radial artery pulse rate"), null=True, blank=True)
    pulse_on_exertion = models.CharField(verbose_name=_("Blood Pressure and Pulse on Exertion"), max_length=40, choices=PulseOnExertionChoices.choices, null=True, blank=True)
    blood_saturation = models.FloatField(verbose_name=_("Blood Oxygen Saturation (%)"), null=True, blank=True)
    respiratory_rate = models.FloatField(verbose_name=_("Respiratory Rate (breaths/min)"), null=True, blank=True)
    breathing_rhythm = models.CharField(verbose_name=_("Breathing Rhythm"), max_length=20, choices=BreathingRhythmChoices.choices, null=True, blank=True)
    moist_rales = models.BooleanField(verbose_name=_("Lung moist rales"), default=False, null=True, blank=True)
    peripheral_edema = models.BooleanField(verbose_name=_("Peripheral Edema"), null=True, blank=True)
    dyspnea = models.BooleanField(verbose_name=_("Dyspnea"), null=True, blank=True)
    dyspnea_type = models.CharField(verbose_name=_("Dyspnea Type"), max_length=20, choices=DyspneaTypeChoices.choices, null=True, blank=True)
    fatigue = models.BooleanField(verbose_name=_("Fatigue"), null=True, blank=True)
    fatigue_type = models.CharField(verbose_name=_("Fatigue Type"), max_length=255, choices=FatigueTypeChoices.choices, null=True, blank=True)
    heart_pain = models.BooleanField(verbose_name=_("Heart Pain"), null=True, blank=True)
    heart_pain_type = models.CharField(verbose_name=_("Heart Pain Type"), max_length=255, choices=HeartPainTypeChoices.choices, null=True, blank=True)

    class Meta:
        verbose_name = _("Physical Indicators")
        verbose_name_plural = _("Physical Indicators")
        
        
class PhysicalActivity(models.Model):

    """Physical activity model"""
    
    record = models.OneToOneField(HealthDiaryRecord, on_delete=models.CASCADE, related_name="physical_activity", unique=True)
    walking_speed = models.FloatField(verbose_name=_("Walking Speed"), null=True, blank=True)
    walking_duration = models.FloatField(verbose_name=_("Walking Duration (min)"), null=True, blank=True)
    distance_covered = models.FloatField(verbose_name=_("Distance Covered (m)"), null=True, blank=True)
    step_count = models.FloatField(verbose_name=_("Step Count"), null=True, blank=True)
    borg_scale = models.IntegerChoices(verbose_name=_("Borg Scale Perception of Physical Effort"), choices=BorgScalePerceptionOfPhysicalEffortChoices.choices, null=True, blank=True)

    class Meta:
        verbose_name = _("Physical Activity")
        verbose_name_plural = _("Physical Activities")
        

# class EmotionalState(models.Model):

#     """Emotional state model"""
    
#     record = models.OneToOneField(verbose_name=_("Record"), to=Record, on_delete=models.CASCADE, primary_key=True)
#     anxiety_level = models.FloatField(verbose_name=_("Anxiety Level"))
#     depression_level = models.FloatField(verbose_name=_("Depression Level"))

#     class Meta:
#         verbose_name = _("Emotional State")
#         verbose_name_plural = _("Emotional States")

