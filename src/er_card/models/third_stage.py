from django.db import models
from django.utils.translation import gettext_lazy as _

from src.er_card.choices import third_stage as third_choices
from .er_card import ConditionAssessmentSheet


class ThirdStageData(models.Model):

    """First stage of the patient condition assessment sheet model"""
    
    ca_sheet = models.OneToOneField(
        verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet, 
        on_delete=models.CASCADE, related_name='third_stage'
    )
    
    coronary_insufficiency = models.CharField(
        verbose_name=_("Coronary insufficiency"), max_length=10, 
        choices=third_choices.CoronaryInsufficiencyChoices.choices
    )
    ahf_severity_class = models.PositiveSmallIntegerField(
        verbose_name=_("AHF severity class according to the Killip classification"), 
        choices=third_choices.AHFSeverityChoices.choices
    )
    nyha_functional_class = models.PositiveSmallIntegerField(
        verbose_name=_("Functional class according to NYHA classification"), 
        choices=third_choices.FunctionalClassChoices.choices
    )

    # <-----Acute Myocardial Infarction (AMI)-----> #
    
    clinical_case_ami = models.BooleanField(verbose_name=_("Clinical case of AMI"), default=False)
    ami_date = models.DateTimeField(verbose_name=_("Date of AMI"), null=True, blank=True)
    ami_localization = models.CharField(
        verbose_name=_("Localization of AMI"), max_length=150, 
        choices=third_choices.AMILocalizationChoices.choices, blank=True
    )
    mi_type = models.CharField(
        verbose_name=_("Type of Miocardium Infarction"), max_length=150, 
        choices=third_choices.MITypeChoices.choices, blank=True
    )
    myocardium_depth_extent = models.CharField(
        verbose_name=_("Depth and extent of myocardial damage"), max_length=150, 
        choices=third_choices.MyocardiumDepthExtentChoices.choices, blank=True
    ) 
    acs_characteristics = models.CharField(
        verbose_name=_("Characteristics of ACS"), max_length=150,
        choices=third_choices.ACSCharacteristicsChoices.choices, blank=True
    )

    # <-----Invasive procedures-----> #

    coronary_angiography = models.BooleanField(verbose_name=_("Coronary angiography"), default=False)
    stenting = models.BooleanField(verbose_name=_("Stenting"), default=False)
    revascularization = models.BooleanField(verbose_name=_("Revascularization"), default=False)
    is_complete = models.BooleanField(verbose_name=_("Is complete"), default=False)

    # <-----Coronary angiography-----> #
    
    coronary_lesion_degree = models.CharField(
        verbose_name=_("Degree of the coronary lesion"), max_length=50, 
        choices=third_choices.CoronaryLesionDegreeChoices.choices
    )
    affected_vessel_name = models.CharField(
        verbose_name=_("Name of the affected vessel"), max_length=50, 
        choices=third_choices.AffectedVesselNameChoices.choices, null=True
    ) 
    vessel_lesion_volume = models.FloatField(verbose_name=_("Vessel lesion volume")) 
    index_syntax = models.FloatField(verbose_name=_("Index SYNTAX"), null=True, blank=True)
    ca_attached = models.FileField(upload_to="uploads/coronary_angiography/", null=True, blank=True)
    
    class Meta:
        verbose_name = _("First stage data")
        verbose_name_plural = _("First stage data")