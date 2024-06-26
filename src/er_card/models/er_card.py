from django.db import models
from django.utils.translation import gettext_lazy as _

from src.management.models import Doctor, Patient
from src.er_card.choices.er_card import *
from src.er_card.utils import get_file_path


class ElectronicRehabilitationCard(models.Model):
    
    """Electronic Rehabilitation Card model"""
    
    patient = models.ForeignKey(
        verbose_name=_("Patient"), to=Patient, 
        on_delete=models.CASCADE, related_name='er_cards'
    )
    created_by = models.ForeignKey(
        verbose_name=_("Created doctor"), to=Doctor, 
        on_delete=models.SET_NULL, related_name='er_cards', null=True
    )
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)

    activity_stage = models.PositiveSmallIntegerField(verbose_name=_("Stage of motor activity"))
    created_at = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Update date"), auto_now=True)
    
    class Meta:
        verbose_name = _("Electronic rehabilitation card")
        verbose_name_plural = _("Electronic rehabilitation cards")
        
    @property
    def is_archive(self):
        if not self.is_active:
            return True
    
    
class Event(models.Model):
    
    """Event model"""

    er_card = models.ForeignKey(
        verbose_name=_("ER card"), to=ElectronicRehabilitationCard,
        on_delete=models.CASCADE, related_name='events'
    )
    title = models.CharField(verbose_name=_("Event title"), max_length=255)
    type = models.CharField(verbose_name=_("Event type"), max_length=20, choices=EventTypeChoices)
    location = models.CharField(verbose_name=_("Event location"), max_length=20, choices=EventLocationChoices)
    start_date = models.DateTimeField(verbose_name=_("Event start date"))
    end_date = models.DateTimeField(verbose_name=_("Event end date"))
    description = models.TextField(verbose_name=_("Additional description"))

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


class ERCardAttachment(models.Model):

    """Attached File model"""

    er_card = models.ForeignKey(
        verbose_name=_("Electronic Rehabilitation Card"), to=ElectronicRehabilitationCard, 
        related_name='attachments',on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name=_("Title"), max_length=90)
    attachment = models.FileField(verbose_name=_("Attachment"), upload_to=get_file_path)

    class Meta:
        verbose_name = _("ER Card attachment")
        verbose_name_plural = _("ER Card attachments")

            
class AdmissionData(models.Model):
    
    """Admission data model"""
    
    er_card = models.OneToOneField(
        verbose_name=_("Electronic rehabilitation card"), to=ElectronicRehabilitationCard,
        on_delete=models.CASCADE, related_name="admission_data")
    
    admission_date = models.DateTimeField(verbose_name=_("Admission date"), unique=True)
    delivery_time = models.DurationField(verbose_name=_("Delivery time"), null=True, blank=True)
    patient_condition = models.CharField(
        verbose_name=_("Patient condition"), max_length=30, 
        choices=ConditionChoices.choices, null=True, blank=True
    )
    patient_complaints = models.TextField(verbose_name=_("Patient complaints"), null=True, blank=True)
    heart_stopped = models.BooleanField(verbose_name=_("Heart stopped"), default=False)
    
    # <-----Preliminary diagnosis-----> #
    
    hospitalization_date = models.DateField(_("Hospitalization date"))
    hospitalization_type = models.CharField(
        verbose_name=_("Hospitalization type"), max_length=15,
        choices=HospitalizationTypeChoices.choices
    )
    preliminary_diagnosis = models.ForeignKey(
        verbose_name=_("Preliminary diagnosis"), to="InternationalClassificationOfDiseases", 
        on_delete=models.SET_NULL, related_name='er_cards', null=True
    )
    diagnosed_by = models.CharField(
        verbose_name=_("Diagnosed by"), max_length=50, 
        choices=DiagnosedByTypeChoices.choices, null=True, blank=True
    )
    additional_information = models.TextField(verbose_name=_("Additional information"), null=True, blank=True)
        
    class Meta:
        verbose_name = _("Admission data")
        verbose_name_plural = _("Admission data")
        
        
class AdmissionAttachment(models.Model):

    """Admission attachment model"""

    admission_data = models.ForeignKey(
        verbose_name=_("Electronic Rehabilitation Card"), to=AdmissionData,
        related_name='attachments',on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name=_("Title"), max_length=90)
    attachment = models.FileField(verbose_name=_("Attachment"), upload_to=get_file_path)

    class Meta:
        verbose_name = _("Admission attachment")
        verbose_name_plural = _("Admission attachments")

        
class InternationalClassificationOfDiseases(models.Model):
    
    """International Classification of Diseases, 10th Revision (ICD-10)"""

    code = models.CharField(verbose_name=_("Diagnosis code"), max_length=15, unique=True)
    title = models.CharField(verbose_name=_("Diagnosis title"),max_length=255)

    class Meta:
        verbose_name = _("Diagnosis")
        verbose_name_plural = _("Diagnoses")  


        
        


