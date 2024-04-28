from django.db import models
from django.utils.translation import gettext_lazy as _

from src.management.models import Doctor, Patient

from src.er_card.choices.er_card import *
from src.er_card.utils import get_file_path_er_card


class ElectronicRehabilitationCard(models.Model):
    
    """Electronic Rehabilitation Card model"""
    
    patient = models.ForeignKey(verbose_name=_("Patient"), to=Patient, on_delete=models.CASCADE, related_name='er_cards')
    created_by = models.ForeignKey(verbose_name=_("Created doctor"), to=Doctor, on_delete=models.SET_NULL, related_name='er_cards', null=True)
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)
    created_at = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Update date"), auto_now=True)
    
    # <-----Admission data-----> #
    
    admission_date = models.DateTimeField(verbose_name=_("Admission date"), unique=True)
    delivery_time = models.DurationField(verbose_name=_("Delivery time"), null=True, blank=True)
    patient_condition = models.CharField(verbose_name=_("Patient condition"), max_length=30, choices=ConditionChoices.choices, null=True, blank=True)
    patient_complaints = models.TextField(verbose_name=_("Patient complaints"), null=True, blank=True)
    heart_stopped = models.BooleanField(verbose_name=_("Heart stopped"), default=False)
    
    # <-----Preliminary diagnosis-----> #
    
    hospitalization_date = models.DateField(_("Hospitalization date"))
    hospitalization_type = models.CharField(verbose_name=_("Hospitalization type"), max_length=15, choices=HospitalizationTypeChoices.choices)
    preliminary_diagnosis = models.ForeignKey(verbose_name=_("Preliminary diagnosis"), to="InternationalClassificationOfDiseases", on_delete=models.SET_NULL, related_name='er_cards', null=True)
    diagnosed_by = models.CharField(verbose_name=_("Diagnosed by"), max_length=50, choices=DiagnosedByTypeChoices.choices, null=True, blank=True)
    additional_information = models.TextField(verbose_name=_("Additional information"), null=True, blank=True)
    
    class Meta:
        verbose_name = _("Electronic rehabilitation card")
        verbose_name_plural = _("Electronic rehabilitation cards")
        
    @property
    def is_archive(self):
        if not self.is_active:
            return True
        
        
class InternationalClassificationOfDiseases(models.Model):
    
    """International Classification of Diseases, 10th Revision (ICD-10)"""

    code = models.CharField(verbose_name=_("Diagnosis code"), max_length=15, unique=True)
    title = models.CharField(verbose_name=_("Diagnosis title"),max_length=255)

    class Meta:
        verbose_name = _("Diagnosis")
        verbose_name_plural = _("Diagnoses")  


class AttachedFile(models.Model):

    """Attached File model"""

    er_card = models.ForeignKey(verbose_name=_("Electronic Rehabilitation Card"), to=ElectronicRehabilitationCard, related_name='attachments',on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Title"), max_length=90)
    attachment = models.FileField(verbose_name=_("Attachment"), upload_to=get_file_path_er_card, max_length=255)

    class Meta:
        verbose_name = _("Attached file")
        verbose_name_plural = _("Attached files")


class ConditionAssessmentSheet(models.Model):
    
    """Patient condition assessment sheet model"""
    
    er_card = models.OneToOneField(verbose_name=_(
        "Electronic rehabilitation card"), to=ElectronicRehabilitationCard,
        on_delete=models.CASCADE, related_name="ch_sheet"
    )
    created_by = models.ForeignKey(
        verbose_name=_("Created doctor"), to='management.Doctor',
        on_delete=models.SET_NULL, related_name="ca_sheets", null=True
    )
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)
    created_at = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Update date"), auto_now=True)

    class Meta:
        verbose_name = _("Condition assessment sheet")
        verbose_name_plural = _("Condition assessment sheets")

