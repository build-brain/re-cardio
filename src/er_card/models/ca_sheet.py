from django.db import models
from django.utils.translation import gettext_lazy as _

from .er_card import ElectronicRehabilitationCard, InternationalClassificationOfDiseases
from src.er_card.choices import ca_sheet as ca_sheet_choices
from src.er_card.utils import calculate_grace_score, calculate_grace, calculate_patient_severity_class


class ConditionAssessmentSheet(models.Model):
    
    """Patient condition assessment sheet model"""
    
    er_card = models.OneToOneField(
        verbose_name=_("Electronic rehabilitation card"), to=ElectronicRehabilitationCard,
        on_delete=models.CASCADE, related_name="ch_sheet"
    )

    # <-----Adherence to therapy according to the Morisky-Green scale-----> #
    
    morisky_green = models.PositiveSmallIntegerField(
        verbose_name=_("Morisky Green"), choices=ca_sheet_choices.MoriskyGreenChoices.choices
    )
    
    # <-----Physical examination results-----> #

    examination_date = models.DateTimeField(verbose_name=_("Date of examination"))
    weight = models.FloatField(verbose_name=_("Weight"))
    height = models.FloatField(verbose_name=_("Height"))
    body_mass_index = models.FloatField(verbose_name=_("Body mass index"), editable=False)
    body_temperature = models.FloatField(verbose_name=_("Body temperature"))

    # <-----Blood pressure-----> #

    systolic_pressure = models.FloatField(verbose_name=_("Systolic blood pressure"))
    diastolic_pressure = models.FloatField(verbose_name=_("Diastolic blood pressure"))
    pulse_rate = models.FloatField(verbose_name=_("Radial artery pulse rate"))
    respiratory_rate = models.FloatField(verbose_name=_("Respiratory rate"), null=True, blank=True)
    spo2 = models.PositiveSmallIntegerField(verbose_name=_("SPO2"), null=True, blank=True)
    
    moist_rales = models.BooleanField(verbose_name=_("Lung moist rales"), default=False, blank=True)
    lower_limb_edema = models.BooleanField(verbose_name=_("Swelling of the lower limbs"), default=False, blank=True)
    
    # <-----Creatinine and Troponin I-----> #

    creatinine = models.FloatField(verbose_name=_('Serum creatinine'))
    troponin = models.FloatField(verbose_name=_('Troponin I'))    
    
    # <-----Classification-----> #
    
    coronary_insufficiency = models.PositiveSmallIntegerField(
        verbose_name=_("Coronary insufficiency"),
        choices=ca_sheet_choices.CoronaryInsufficiencyChoices.choices
    )
    killip = models.PositiveSmallIntegerField(
        verbose_name=_("AHF severity class according to the Killip classification"), 
        choices=ca_sheet_choices.AHFSeverityChoices.choices
    )
    nyha = models.PositiveSmallIntegerField(
        verbose_name=_("Functional class according to NYHA classification"), 
        choices=ca_sheet_choices.FunctionalClassChoices.choices
    )

    # <-----Electrocardiogram results-----> #

    st_segment_elevation = models.BooleanField(verbose_name=_("ST segment elevation"), default=False)
    t_wave_inversion = models.BooleanField(verbose_name=_("T wave inversion "), default=False)

    # <-----Acute Myocardial Infarction (AMI)-----> #
    
    ami_clinical_case = models.BooleanField(verbose_name=_("Clinical case of AMI"), default=False)
    ami_date = models.DateTimeField(verbose_name=_("Date of AMI"), null=True, blank=True)
    ami_localization = models.CharField(
        verbose_name=_("Localization of AMI"), max_length=150, 
        choices=ca_sheet_choices.AMILocalizationChoices.choices
    )
    mi_type = models.CharField(
        verbose_name=_("Type of Miocardium Infarction"), max_length=150, 
        choices=ca_sheet_choices.MITypeChoices.choices
    )
    myocardium_damage = models.PositiveSmallIntegerField(
        verbose_name=_("Depth and extent of myocardial damage"), 
        choices=ca_sheet_choices.MyocardiumDepthExtentChoices.choices
    ) 
    acs_characteristics = models.CharField(
        verbose_name=_("Characteristics of ACS"), max_length=150,
        choices=ca_sheet_choices.ACSCharacteristicsChoices.choices, blank=True
    )

    # <-----Invasive procedures-----> #

    coronary_angiography = models.BooleanField(verbose_name=_("Coronary angiography"), default=False)
    stenting = models.BooleanField(verbose_name=_("Stenting"), default=False)
    revascularization = models.BooleanField(verbose_name=_("Revascularization"), default=False)
    is_complete = models.BooleanField(verbose_name=_("Is complete"), default=False)

    # <-----Coronary angiography-----> #
    
    coronary_lesion_degree = models.CharField(
        verbose_name=_("Degree of the coronary lesion"), max_length=50, 
        choices=ca_sheet_choices.CoronaryLesionDegreeChoices.choices
    )
    affected_vessel_name = models.CharField(
        verbose_name=_("Name of the affected vessel"), max_length=50, 
        choices=ca_sheet_choices.AffectedVesselNameChoices.choices, null=True
    ) 
    vessel_lesion_volume = models.FloatField(verbose_name=_("Vessel lesion volume")) 
    index_syntax = models.FloatField(verbose_name=_("Index SYNTAX"), null=True, blank=True)
    # ca_attached = models.FileField(upload_to="uploads/coronary_angiography/", null=True, blank=True)
    
    # <-----Clinical diagnosis-----> #
    
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
    
    complications = models.ManyToManyField(
        verbose_name=_("Complications"), to='Complication',
        related_name='ca_sheets'
    )

    # <-----GRACE Scale-----> #
    
    grace_score = models.PositiveSmallIntegerField(verbose_name=_("GRACE score"), default=0, editable=False)
    stemi = models.BooleanField(verbose_name=_("is stemi"), default=False, editable=False)
    lethality_hospital = models.CharField(verbose_name=_("Lethality percent in hospital"), max_length=10, editable=False)
    lethality_six_months = models.CharField(verbose_name=_("Lethality percent in six months"), max_length=10, editable=False)
    risk_hospital = models.CharField(
        verbose_name=_("Lethality risk in hospital"), max_length=20,
        choices=ca_sheet_choices.RiskTypeChoices.choices, editable=False
    )
    risk_six_months = models.CharField(
        verbose_name=_("Lethality risk in six months"), max_length=20,
        choices=ca_sheet_choices.RiskTypeChoices.choices, editable=False
    )
    
    patient_severity_class = models.PositiveSmallIntegerField(verbose_name=_("Patient severity class"), editable=False)    

    created_at = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Update date"), auto_now=True)
    
    def save(self, *args, **kwargs):
        self.body_mass_index = self.weight / (self.height ** 2)
        if self.acs_characteristics == "mi_with_st":
            self.stemi = True
        self.grace_score = calculate_grace_score(instance=self)
        self.lethality_hospital, self.risk_hospital = calculate_grace(score=self.grace_score, stemi=self.stemi, hospital=True)
        self.lethality_six_months, self.risk_six_months = calculate_grace(score=self.grace_score, stemi=self.stemi)
        self.patient_severity_class = calculate_patient_severity_class(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Condition assessment sheet")
        verbose_name_plural = _("Condition assessment sheets")

    
class Complication(models.Model):
    
    """Complications groups model"""

    group = models.PositiveSmallIntegerField(
        verbose_name=_("Group"), choices=ca_sheet_choices.ComplicationGroupChoices
    )
    name = models.CharField(verbose_name=_("Complication"), max_length=150)
    
    class Meta:
        verbose_name = _("Complications group")
        verbose_name_plural = _("Complications groups")
        
    def __str__(self):
        return self.complication