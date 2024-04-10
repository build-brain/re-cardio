from django.db import models
from django.utils.translation import gettext_lazy as _

from management.models import Doctor, Patient


class ElectronicRehabilitationCard(models.Model):
    
    """Electronic Rehabilitation Card model"""
    
    patient = models.ForeignKey(verbose_name=_("Patient"), to=Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(verbose_name=_("Created doctor"), to=Doctor, on_delete=models.SET_NULL, related_name='er_cards', null=True)
    admission_data = models.ForeignKey(verbose_name=_("Admission data"), to="management.AdmissionData", on_delete=models.SET_NULL, related_name='er_cards', null=True)
    # ca_sheet = models.ForeignKey(verbose_name=_("CA sheet"), to="ca_sheet.ConditionAssessmentSheet", on_delete=models.SET_NULL, related_name='er_cards', null=True)
    
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)
    created_at = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Update date"), auto_now=True)
    
    class Meta:
        verbose_name = _("Electronic rehabilitation card")
        verbose_name_plural = _("Electronic rehabilitation cards")
        
    @property
    def is_archive(self):
        if not self.is_active:
            return True

# class AttachedFile(models.Model):

#     """Attached File model"""

#     er_card = models.ForeignKey(verbose_name=_("ER card"), to=ElectronicRehabilitationCard, on_delete=models.CASCADE)
#     title = models.CharField(verbose_name=_("Title"), max_length=90)
#     file = models.FileField(verbose_name=_("File"), upload_to="uploads/% Y/% m/% d/")

#     class Meta:
#         verbose_name = _("Attached file")
#         verbose_name_plural = _("Attached files")