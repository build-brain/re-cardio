from django.db import models
from django.utils.translation import gettext_lazy as _

from er_card.models import ElectronicRehabilitationCard
from management.models import Doctor

from .choices import *
from .utils import get_file_path

class ConditionAssessmentSheet(models.Model):
    
    """Patient condition assessment sheet model"""
    
    er_card = models.ForeignKey(verbose_name=_("Electronic rehabilitation card"), to=ElectronicRehabilitationCard, on_delete=models.CASCADE, related_name="ch_sheets")
    created_at = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Update date"), auto_now=True)
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)
    created_doctor = models.ForeignKey(verbose_name=_("Created doctor"), to=Doctor, on_delete=models.SET_NULL, related_name="ca_sheets", null=True)
    
    class Meta:
        verbose_name = _("Condition assessment sheet")
        verbose_name_plural = _("Condition assessment sheets")
        
    def __str__(self):
        return self.er_card.patient.first_name


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
        

class SecondStageData(models.Model):

    """Second stage of the patient condition assessment sheet model"""

    ca_sheet = models.OneToOneField(verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet, on_delete=models.CASCADE, related_name='second_stage')

    # <-----Physical examination results-----> #

    examination_date = models.DateTimeField(verbose_name=_("Date of examination"))
    weight = models.FloatField(verbose_name=_("Weight"))
    height = models.FloatField(verbose_name=_("Height"))
    body_mass_index = models.FloatField(verbose_name=_("Body mass index"))
    body_temperature = models.FloatField(verbose_name=_("Body temperature"))

    # <-----Blood pressure-----> #

    systolic_pressure = models.FloatField(verbose_name=_("Systolic blood pressure"))
    diastolic_pressure = models.FloatField(verbose_name=_("Diastolic blood pressure"))
    radial_artery_pulse_rate = models.FloatField(verbose_name=_("Radial artery pulse rate"), null=True, blank=True)
    respiratory_rate = models.FloatField(verbose_name=_("Respiratory rate"), null=True, blank=True)
    
    moist_rales = models.BooleanField(verbose_name=_("Lung moist rales"), default=False, blank=True)
    lower_limb_edema = models.BooleanField(verbose_name=_("Swelling of the lower limbs"), default=False, blank=True)

    # <-----Electrocardiogram(ECG) data-----> #

    ecg_date = models.DateTimeField(verbose_name=_("ECG date"))
    heart_rate = models.FloatField(verbose_name=_("Heart rate"))
    heart_rhythm = models.CharField(verbose_name=_("Heart rhythm"), max_length=100)
    st_segment_depression = models.BooleanField(verbose_name=_("ST segment depression"), default=False)
    st_segment_depression_duration = models.BooleanField(verbose_name=_("ST segment depression duration"), default=False)
    st_segment_elevation = models.BooleanField(verbose_name=_("ST segment elevation"), default=False)
    q_wave_or_qs_complex = models.BooleanField(verbose_name=_("Pathalogical Q wave or QS complex"), default=False)
    t_wave_inversion = models.BooleanField(verbose_name=_("T wave inversion "), default=False)
    ecg_attachment = models.FileField(verbose_name=_("ECG attachment"), upload_to="uploads/ecg/% Y/% m/% d/", null=True, blank=True)

    # <-----Echocardiography(EchoCG) data-----> #

    echocg_date = models.DateTimeField(verbose_name=_("Echocardiography date"))
    interventricular_septum_hypertrophy = models.BooleanField(verbose_name=_("Interventricular septum hypertrophy"), default=False)
    lv_posterior_wall_hypertrophy  = models.BooleanField(verbose_name=_("Left ventricular posterior wall hypertrophy"), default=False)
    lv_end_diastolic_size = models.BooleanField(verbose_name=_("Left ventricular end diastolic size"), default=False)
    hypokinesia_presence = models.BooleanField(verbose_name=_("Presence of hypokinesia"), default=False)
    akinesia_presence = models.BooleanField(verbose_name=_("Presence of akinesia"), default=False)
    dyskinesia_presence = models.BooleanField(verbose_name=_("Presence of dyskinesia"), default=False)
    acute_aneurysm = models.BooleanField(verbose_name=_("Acute aneurysm"), default=False)
    myocardial_rupture = models.BooleanField(verbose_name=_("Myocardial rupture"), default=False)
    left_ventricle_decreased_pumping_function = models.CharField(verbose_name=_("Left ventricular decreased pumping function"), max_length=10, choices=EjectionFractionChoices.choices) 
    heart_cavity_platelet_vegetations = models.BooleanField(verbose_name=_("Platelet vegetations in heart cavity valves"), default=False)
    echocg_attachment = models.FileField(verbose_name=_("EchoCG attachment"), upload_to="uploads/echocg/% Y/% m/% d/", null=True, blank=True)

    # <-----Holter Monitoring ECG data-----> #

    hm_ecg_date = models.DateTimeField(verbose_name=_("Holter Monitoring ECG date"))
    heart_rate_max = models.FloatField(verbose_name=_("Maximum heart rate"), null=True, blank=True)
    heart_rate_min = models.FloatField(verbose_name=_("Minimum heart rate"), null=True, blank=True)
    heart_rate_avg = models.FloatField(verbose_name=_("Average heart rate"))
    heart_rhythm_disorders = models.BooleanField(verbose_name=_("Heart rhythm disorders"), default=False) # When you check the box, the fields are activated.
    heart_rhythm_disorders_type = models.CharField(verbose_name=_("Heart rhythm disorders type"), max_length=100, choices=HeartRhythmChoices.choices, null=True, blank=True)
    
    SDNN = models.FloatField(verbose_name=_("Heart rate variability SDNN"), null=True, blank=True)
    SDNN_5 = models.FloatField(verbose_name=_("Heart rate variability SDNN 5"), null=True, blank=True)
    SDANN = models.FloatField(verbose_name=_("Heart rate variability SDANN"), null=True, blank=True)
    
    hm_st_segment_depression = models.BooleanField(verbose_name=_("ST segment depression"), default=False)
    hm_st_segment_depression_duration = models.BooleanField(verbose_name=_("ST segment depression duration"), default=False)
    hm_st_segment_elevation = models.BooleanField(verbose_name=_("ST segment elevation"), default=False)
    hm_q_wave_or_qs_complex = models.BooleanField(verbose_name=_("Pathalogical Q wave or QS complex"), default=False)
    hm_t_wave_inversion = models.BooleanField(verbose_name=_("T wave inversion "), default=False)
    hm_ecg_attachment = models.FileField(verbose_name=_("Holter Monitoring ECG attachment"), upload_to="uploads/hm_ecg/% Y/% m/% d/", null=True, blank=True)

    # <-----Myocardial necrosis biochemical markers(MNBM) data-----> #
    
    # erythrocyte_sedimentation_rate = models.FloatField(verbose_name=_("Erythrocyte sedimentation rate"))
    # serum_creatinine = models.FloatField(verbose_name=_("Serum creatinine"))
    # glycated_hemoglobin = models.FloatField(verbose_name=_("Glycated hemoglobin"))
    # glomerular_filtration_rate = models.FloatField(verbose_name=_("Glomerular filtration rate"))
    # creatine_phosphokinase_mb = models.FloatField(verbose_name=_("Creatine phosphokinase-MB"))
    # troponin_i = models.FloatField(verbose_name=_("Troponin-I"))
    # c_reactive_protein = models.FloatField(verbose_name=_("C reactive protein"))
    # brain_natriuretic_propeptide = models.FloatField(verbose_name=_("Brain natriuretic propeptide"))
    # mnbm_attachment = models.FileField(verbose_name=_("MNBM attachment"), upload_to="uploads/% Y/% m/% d/")

    # <-----Attachment and laboratory results-----> #

    # general_blood_analysis = models.FileField(verbose_name=_("General blood analysis"), upload_to="uploads/% Y/% m/% d/")
    # general_urine_analysis = models.FileField(verbose_name=_("General urine analysis"), upload_to="uploads/% Y/% m/% d/")
    # lipidogram = models.FileField(verbose_name=_("Lipidogram"), upload_to="uploads/% Y/% m/% d/")
    # peripheral_vessels_ultrasound = models.FileField(verbose_name=_("Peripheral vessels ultrasound"), upload_to="uploads/% Y/% m/% d/")
    # abdominal_organs_ultrasound = models.FileField(verbose_name=_("Abdominal organs ultrasound"), upload_to="uploads/% Y/% m/% d/")

    class Meta:
        verbose_name = _("Second stage data")
        verbose_name_plural = _("Second stage data")


class MyocardialNecrosisBiochemicalMarker(models.Model):

    """Myocardial necrosis biochemical marker(MNBM) model"""

    second_stage = models.ForeignKey(verbose_name=_("Second stage data"), to=SecondStageData, on_delete=models.CASCADE, related_name='mnbm_data')
    title = models.CharField(verbose_name=_("MNBM title"), max_length=90)
    mnbm_date = models.DateField(verbose_name=_("MNBM date"))
    file = models.FileField(verbose_name=_("MNBM file"), upload_to=get_file_path)
    
    class Meta:
        verbose_name = _("MNBM attached file")
        verbose_name_plural = _("MNBM attached files")

    def __str__(self):
        return self.title
    

class AdditionalTestResult(models.Model):

    """Additional test results model"""

    second_stage = models.ForeignKey(verbose_name=_("Second stage data"), to=SecondStageData, on_delete=models.CASCADE, related_name='additional_test_results')
    title = models.CharField(verbose_name=_("Title"), max_length=90)
    file = models.FileField(verbose_name=_("File"), upload_to=get_file_path)
    created_at = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Update date"), auto_now=True)

    class Meta:
        verbose_name = _("Additional test result")
        verbose_name_plural = _("Additional test results")

    def __str__(self):
        return self.title


class ThirdStageData(models.Model):

    """First stage of the patient condition assessment sheet model"""
    
    ca_sheet = models.OneToOneField(verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet, on_delete=models.CASCADE, related_name='third_stage')
    
    coronary_insufficiency = models.CharField(verbose_name=_("Coronary insufficiency"), max_length=10, choices=CoronaryInsufficiencyChoices.choices)
    ahf_severity_class = models.PositiveSmallIntegerField(verbose_name=_("AHF severity class according to the Killip classification"), choices=AHFSeverityChoices.choices)
    nyha_functional_class = models.PositiveSmallIntegerField(verbose_name=_("Functional class according to NYHA classification"), choices=FunctionalClassChoices.choices)

    # <-----Acute Myocardial Infarction (AMI)-----> #
    
    clinical_case_ami = models.BooleanField(verbose_name=_("Clinical case of AMI"), default=False)
    ami_date = models.DateTimeField(verbose_name=_("Date of AMI"), null=True, blank=True)
    ami_localization = models.CharField(verbose_name=_("Localization of AMI"), max_length=150, choices=AMILocalizationChoices.choices, blank=True)
    mi_type = models.CharField(verbose_name=_("Type of Miocardium Infarction"), max_length=150, choices=MITypeChoices.choices, blank=True)
    myocardium_depth_extent = models.CharField(verbose_name=_("Depth and extent of myocardial damage"), max_length=150, choices=MyocardiumDepthExtentChoices.choices, blank=True) 
    acs_characteristics = models.CharField(verbose_name=_("Characteristics of ACS"), max_length=150, choices=ACSCharacteristicsChoices.choices, blank=True)

    # <-----Invasive procedures-----> #

    coronary_angiography = models.BooleanField(verbose_name=_("Coronary angiography"), default=False)
    stenting = models.BooleanField(verbose_name=_("Stenting"), default=False)
    revascularization = models.BooleanField(verbose_name=_("Revascularization"), default=False)
    is_complete = models.BooleanField(verbose_name=_("Is complete"), default=False)

    # <-----Coronary angiography-----> #
    
    coronary_lesion_degree = models.CharField(verbose_name=_("Degree of the coronary lesion"), max_length=150, choices=CoronaryLesionDegreeChoices.choices)
    affected_vessel_name = models.CharField(verbose_name=_("Name of the affected vessel"),max_length=50, choices=AffectedVesselNameChoices.choices, null=True) 
    # affected_vessel_name = models.ForeignKey(verbose_name=_("Name of the affected vessel"),to="AffectedVesselName", on_delete=models.SET_NULL, related_name='third_stage_data', null=True) 
    vessel_lesion_volume = models.FloatField(verbose_name=_("Vessel lesion volume")) 
    index_syntax = models.FloatField(verbose_name=_("Index SYNTAX"), null=True, blank=True)
    ca_attached = models.FileField(upload_to="uploads/coronary_angiography/% Y/% m/% d/", null=True, blank=True)
    
    class Meta:
        verbose_name = _("First stage data")
        verbose_name_plural = _("First stage data")
        
        
# class AffectedVesselName(models.Model):
    
#     """Название пораженного сосуда"""

#     name = models.CharField(verbose_name=_("Name"), max_length=90)
    
#     class Meta:
#         verbose_name = _("Affected vessel name")
#         verbose_name_plural = _("Affected vessel names")
        
#     def __str__(self):
#         return self.name
        

class ClinicalDiagnosis(models.Model):
    
    """Clinical diagnosis, assessment of the severity of the condition 
    and prognosis of the disease model"""

    issue_date = models.DateTimeField(verbose_name=_("Issue date"))
    primary_disease = models.ForeignKey(verbose_name=_("Primary disease"), to='management.InternationalClassificationOfDiseases', on_delete=models.SET_NULL, related_name='clinical_diagnosis', null=True)
    accompanying_pathologies = models.BooleanField(verbose_name=_("Accompanying pathologies"), default=False)
    accompanying_pathologies_type = models.ForeignKey(verbose_name=_("Accompanying pathologies type"), to='management.InternationalClassificationOfDiseases', on_delete=models.SET_NULL, related_name='accompanying_pathologies', null=True, blank=True)

    # <-----Complications-----> #
    
    complications_group_1 = models.ManyToManyField(verbose_name=_("Group 1 complications"), to='Complication', blank=True, related_name='diagnoses_group_1')
    complications_group_2 = models.ManyToManyField(verbose_name=_("Group 3 complications"), to='Complication', blank=True, related_name='diagnoses_group_2')
    complications_group_3 = models.ManyToManyField(verbose_name=_("Group 3 complications"), to='Complication', blank=True, related_name='diagnoses_group_3')
    
    # grace = models.PositiveSmallIntegerField(verbose_name=_("GRACE"))
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

    
# class ScaleGRACE(models.Model):
    
#     """Шкала GRACE"""

#     title = models.CharField(verbose_name=_("ACS type"), max_length=20, choices=ACSTypeChoices.choices)
#     lethality = models.CharField(verbose_name=_("Type"), max_length=50)


        