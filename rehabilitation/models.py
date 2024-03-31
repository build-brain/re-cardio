from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import *


class ElectronicRehabilitationCard(models.Model):
    
    """Electronic Rehabilitation Card model"""
    
    patient = models.OneToOneField(
        _("Patient"),
        to="management.Patient",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Update date"), auto_now=True)
    is_active = models.BooleanField(_("Is active"), default=True)
    doctor = models.ForeignKey(
        verbose_name=_("Created doctor"),
        to="management.Doctor", 
        on_delete=models.SET_NULL,
        null=True
    )
    
    admission_date = models.DateTimeField(
        _("Admission date"),
        null=True,
        blank=True
    )
    delivery_time = models.DurationField(
        _("Delivery time"), 
        null=True, 
        blank=True
    )
    patient_condition = models.CharField(
        _("Patient condition"), 
        max_length=30,
        choices=ConditionChoices.choices,
        null=True,
        blank=True
    )
    patient_complaints = models.TextField(
        _("Patient complaints"),
        null=True,
        blank=True
    )
    heart_stopped = models.BooleanField(_("Heart stopped"), default=False)
    
    # <-----Preliminary diagnosis-----> #
    
    preliminary_diagnosis = models.ForeignKey(
        _("Preliminary diagnosis"),
        to="PreliminaryDiagnosis",
        on_delete=models.SET_NULL,
        related_name='er_cards',
        null=True
    )
    diagnosed_by = models.CharField(
        _("Diagnosed by"),
        max_length=50,
        choices=DiagnosedByTypeChoices.choices,
        null=True,
        blank=True
    )
    hospitalization_type = models.CharField(
        _("Hospitalization type"),
        max_length=15,
        choices=HospitalizationTypeChoices.choices
    )
    hospitalization_date = models.DateField(_("Hospitalization date"))
    additional_information = models.TextField(
        _("Additional information"),
        null=True,
        blank=True
    )
    attached_files = models.FileField(_("Attached files"), upload_to='attached_files/')
    
    @property
    def is_archive(self):
        if not self.status:
            return True
        

class PreliminaryDiagnosis(models.Model):
    
    """Preliminary diagnosis model"""

    code = models.CharField(verbose_name=_("Diagnosis code"), max_length=15)
    title = models.CharField(verbose_name=_("Diagnosis title"),max_length=150)

    class Meta:
        verbose_name = _("Diagnosis")
        verbose_name_plural = _("Diagnoses")