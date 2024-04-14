from django.db import models
from django.utils.translation import gettext_lazy as _

from src.ca_sheet.choices.first_stage import *
from .base import ConditionAssessmentSheet


class FirstStageData(models.Model):

    """First stage of the patient condition assessment sheet model"""
    
    ca_sheet = models.OneToOneField(verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet, on_delete=models.CASCADE, related_name='first_stage')
    
    # <-----Patient complaints-----> #

    main_complaint = models.CharField(verbose_name=_("Main complaint"), max_length=250)
    side_complaints = models.TextField(verbose_name=_("Side complaints"), blank=True)

    # <-----Anamnesis data-----> #

    cardiovascular_diseases = models.BooleanField(verbose_name=_("Was cardiovascular diseases"), default=False)
    early_deaths = models.BooleanField(verbose_name=_("Was early deaths"), default=False)
    bad_habits = models.BooleanField(verbose_name=_("Has bad habits"), default=False)
    
    # <-----Hospitalizations due to CVD in the last 12 months-----> #
    
    cvd_hospitalizations = models.BooleanField(verbose_name=_("CVD hospitalizations"), default=False) # When you check the box, the fields are activated.
    latest_hospitalization = models.DateTimeField(verbose_name=_("Latest hospitalization date"), null=True, blank=True)
    hospitalization_reason = models.CharField(verbose_name=_("Hospitalization reason"), max_length=150, blank=True)
    disease_outcome_data = models.TextField(verbose_name=_("Disease outcome data"), blank=True)
    
    # <-----Allergic reactions-----> #
    
    allergic_reactions = models.BooleanField(verbose_name=_("Allergic reactions"), default=False) # When you check the box, the fields are activated.
    for_medicines = models.CharField(verbose_name=_("Allergic for medicines"), max_length=150, blank=True)
    for_food = models.CharField(verbose_name=_("Allergic for food"), max_length=150, blank=True)
    for_other = models.CharField(verbose_name=_("Allergic for other"), max_length=150, blank=True)
    
    # <-----CVD medications-----> # 

    cvd_medications = models.BooleanField(verbose_name=_("CVD medications taken"), default=False) # When you check the box, the fields are activated.
    medication_group = models.ForeignKey(verbose_name=_("Medication group"), to="MedicationGroup", on_delete=models.SET_NULL, related_name="ca_sheets", null=True, blank=True)
    medication_name = models.ForeignKey(verbose_name=_("Medication name"), to="Medication", on_delete=models.SET_NULL, related_name="ca_sheets", null=True, blank=True)
    dosage = models.CharField(verbose_name=_("Dosage"), max_length=150, blank=True)
    use_duration = models.CharField(verbose_name=_("Use duration"), max_length=150, blank=True)
    
    # <-----Adherence to therapy according to the Morisky-Green scale-----> #
    
    morisky_green = models.PositiveSmallIntegerField(verbose_name=_("Morisky Green"), choices=MoriskyGreenChoices.choices)
   
    class Meta:
        verbose_name = _("First stage data")
        verbose_name_plural = _("First stage data")


class MedicationGroup(models.Model):

    """Medication group model"""
    
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    description = models.TextField(verbose_name=_("Description"), blank=True)

    class Meta:
        verbose_name = _("Medication group")
        verbose_name_plural = _("Medication groups")

    def __str__(self):
        return self.name

        
class Medication(models.Model):

    """Medication model"""
    
    group = models.ForeignKey(verbose_name=_("Medication group"), to=MedicationGroup, on_delete=models.CASCADE, related_name="medications")
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    description = models.TextField(verbose_name=_("Description"), blank=True)

    class Meta:
        verbose_name = _("Medication")
        verbose_name_plural = _("Medications")

    def __str__(self):
        return self.name