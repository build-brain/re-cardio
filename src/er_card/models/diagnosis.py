from django.db import models
from django.utils.translation import gettext_lazy as _

from .er_card import ConditionAssessmentSheet, InternationalClassificationOfDiseases
from src.er_card.choices import diagnosis as diagnosis_choices


class ClinicalDiagnosis(models.Model):
    
    """Clinical diagnosis, assessment of the severity of the condition 
    and prognosis of the disease model"""

    ca_sheet = models.OneToOneField(
        verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet, 
        on_delete=models.CASCADE, related_name='clinical_diagnosis'
    )

    issue_date = models.DateTimeField(verbose_name=_("Issue date"))
    primary_disease = models.ForeignKey(
        verbose_name=_("Primary disease"), to=InternationalClassificationOfDiseases, 
        on_delete=models.SET_NULL, related_name='clinical_diagnosis', null=True
    )
    accompanying_pathologies = models.BooleanField(verbose_name=_("Accompanying pathologies"), default=False)
    accompanying_pathologies_type = models.ForeignKey(
        verbose_name=_("Accompanying pathologies type"), to=InternationalClassificationOfDiseases,
        on_delete=models.SET_NULL, related_name='accompanying_pathologies', null=True, blank=True
    )

    # <-----Complications-----> #
    
    complications_group_1 = models.ManyToManyField(
        verbose_name=_("Group 1 complications"), to='Complication',
        related_name='diagnoses_group_1', blank=True
    )
    complications_group_2 = models.ManyToManyField(
        verbose_name=_("Group 3 complications"), to='Complication',
        related_name='diagnoses_group_2', blank=True
    )
    complications_group_3 = models.ManyToManyField(
        verbose_name=_("Group 3 complications"), to='Complication',
        related_name='diagnoses_group_3', blank=True
    )
    
    grace = models.ForeignKey(verbose_name=_("GRACE Scale"), to='GraceScale', on_delete=models.SET_NULL, null=True)
    # patient_severity_class = models.PositiveSmallIntegerField(verbose_name=_("Patient severity class"), choices=PatientSeverityClassChoices.choices)

    additional_information = models.TextField(verbose_name=_("Additional information"), blank=True)

    class Meta:
        verbose_name = _("Clinical diagnosis")
        verbose_name_plural = _("Clinical diagnoses")


    def __str__(self):
        return str(self.primary_disease.name)
    
    
class Complication(models.Model):
    
    """Complications groups model"""

    group = models.PositiveSmallIntegerField(verbose_name=_("Group"))
    complication = models.CharField(verbose_name=_("Complication"), max_length=150)
    
    class Meta:
        verbose_name = _("Complications group")
        verbose_name_plural = _("Complications groups")
        
    def __str__(self):
        return self.group_name

        
class GraceScale(models.Model):

    """GRACE Scale model"""

    acs_type = models.CharField(
        verbose_name=_('Acute Coronary Syndrome Type'), max_length=10,
        choices=diagnosis_choices.ACSTypeChoices.choices
    )
    lethality_type = models.CharField(
        verbose_name=_('Lethality type'), max_length=20,
        choices=diagnosis_choices.LethalityTypeChoices.choices
    )
    score_range_start = models.PositiveIntegerField(verbose_name=_('Score range start'), null=True, blank=True)
    score_range_end = models.PositiveIntegerField(verbose_name=_('Score range end'), null=True, blank=True)
    risk = models.CharField(
        verbose_name=_('Risk'), max_length=15,
        choices=diagnosis_choices.RiskChoices.choices
    )
    lethality_start = models.FloatField(verbose_name=_('Lethality percentage start'), null=True, blank=True)
    lethality_end = models.FloatField(verbose_name=_('Lethality percentage end'), null=True, blank=True)

    class Meta:
        verbose_name = 'GRACE Scale'
        verbose_name_plural = 'GRACE Scale'

    def __str__(self):
        return f'{self.acs_type} - {self.lethality_type} - {self.risk}'