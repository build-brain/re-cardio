from django.db import models
from django.utils.translation import gettext_lazy as _

from src.er_card.choices import extra_data as extra_data_choices
from .ca_sheet import ConditionAssessmentSheet


class ExtraData(models.Model):

    """Extra data of the patient condition assessment sheet model"""
    
    ca_sheet = models.OneToOneField(
        verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet,
        on_delete=models.CASCADE, related_name='first_stage'
    )
    
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
    
    
class ElectroCardiogramData(models.Model):

    """Second stage of the patient condition assessment sheet model"""

    ca_sheet = models.OneToOneField(
        verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet,
        on_delete=models.CASCADE, related_name='second_stage'
    )

    ecg_date = models.DateTimeField(verbose_name=_("ECG date"))
    heart_rate = models.FloatField(verbose_name=_("Heart rate"))
    heart_rhythm = models.CharField(
        verbose_name=_("Heart rhythm"), max_length=50, 
        choices=extra_data_choices.HeartRhythmChoices.choices
    )
    st_segment_depression = models.BooleanField(verbose_name=_("ST segment depression"), default=False)
    st_segment_depression_duration = models.BooleanField(verbose_name=_("ST segment depression duration"), default=False)
    # st_segment_elevation = models.BooleanField(verbose_name=_("ST segment elevation"), default=False)
    q_wave_or_qs_complex = models.BooleanField(verbose_name=_("Pathalogical Q wave or QS complex"), default=False)
    # t_wave_inversion = models.BooleanField(verbose_name=_("T wave inversion "), default=False)
    ecg_attachment = models.FileField(verbose_name=_("ECG attachment"), upload_to="uploads/ca_cheet/ecg/", null=True, blank=True)
    ecg_additional = models.FileField(verbose_name=_("ECG additional"), upload_to="uploads/ca_cheet/ecg/", null=True, blank=True)


class EchocardiographyData(models.Model):

    """Third stage of the patient condition assessment sheet model"""

    ca_sheet = models.OneToOneField(
        verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet,
        on_delete=models.CASCADE, related_name='third_stage'
    )

    echocg_date = models.DateTimeField(verbose_name=_("Echocardiography date"))
    interventricular_septum_hypertrophy = models.BooleanField(verbose_name=_("Interventricular septum hypertrophy"), default=False)
    lv_posterior_wall_hypertrophy  = models.BooleanField(verbose_name=_("Left ventricular posterior wall hypertrophy"), default=False)
    lv_end_diastolic_size = models.BooleanField(verbose_name=_("Left ventricular end diastolic size"), default=False)
    hypokinesia_presence = models.BooleanField(verbose_name=_("Presence of hypokinesia"), default=False)
    akinesia_presence = models.BooleanField(verbose_name=_("Presence of akinesia"), default=False)
    dyskinesia_presence = models.BooleanField(verbose_name=_("Presence of dyskinesia"), default=False)
    acute_aneurysm = models.BooleanField(verbose_name=_("Acute aneurysm"), default=False)
    myocardial_rupture = models.BooleanField(verbose_name=_("Myocardial rupture"), default=False)
    left_ventricle_decreased_pumping_function = models.CharField(
        verbose_name=_("Left ventricular decreased pumping function"), max_length=10,
        choices=extra_data_choices.EjectionFractionChoices.choices
    ) 
    heart_cavity_platelet_vegetations = models.BooleanField(verbose_name=_("Platelet vegetations in heart cavity valves"), default=False)
    echocg_attachment = models.FileField(verbose_name=_("EchoCG attachment"), upload_to="uploads/ca_cheet/echocg/", null=True, blank=True)
    echocg_additional = models.FileField(verbose_name=_("EchoCG additional"), upload_to="uploads/ca_sheet/echocg/", null=True, blank=True)


class HolterMonitoringECGData(models.Model):

    """Holter monitoring ECG data model"""

    ca_sheet = models.OneToOneField(
        verbose_name=_("Condition Assessment sheet"), to=ConditionAssessmentSheet,
        on_delete=models.CASCADE, related_name='holter_monitoring_ecg'
    )

    hm_ecg_date = models.DateTimeField(verbose_name=_("Holter Monitoring ECG date"))
    heart_rate_max = models.FloatField(verbose_name=_("Maximum heart rate"), null=True, blank=True)
    heart_rate_min = models.FloatField(verbose_name=_("Minimum heart rate"), null=True, blank=True)
    heart_rate_avg = models.FloatField(verbose_name=_("Average heart rate"))
    heart_rhythm_disorders = models.BooleanField(verbose_name=_("Heart rhythm disorders"), default=False) # When you check the box, the fields are activated.
    heart_rhythm_disorders_type = models.CharField(
        verbose_name=_("Heart rhythm disorders type"), max_length=31,
        choices=extra_data_choices.HeartRhythmDisordersChoices.choices, null=True, blank=True
    )
    
    SDNN = models.FloatField(verbose_name=_("Heart rate variability SDNN"), null=True, blank=True)
    SDNN_5 = models.FloatField(verbose_name=_("Heart rate variability SDNN 5"), null=True, blank=True)
    SDANN = models.FloatField(verbose_name=_("Heart rate variability SDANN"), null=True, blank=True)
    
    hm_st_segment_depression = models.BooleanField(verbose_name=_("ST segment depression"), default=False)
    hm_st_segment_depression_duration = models.BooleanField(verbose_name=_("ST segment depression duration"), default=False)
    hm_st_segment_elevation = models.BooleanField(verbose_name=_("ST segment elevation"), default=False)
    hm_q_wave_or_qs_complex = models.BooleanField(verbose_name=_("Pathalogical Q wave or QS complex"), default=False)
    hm_t_wave_inversion = models.BooleanField(verbose_name=_("T wave inversion "), default=False)
    hm_ecg_attachment = models.FileField(verbose_name=_("Holter Monitoring ECG attachment"), upload_to="uploads/ca_sheet/hm_ecg/", null=True, blank=True)
    hm_ech_additional = models.FileField(verbose_name=_("Holter Monitoring ECG additional"), upload_to="uploads/ca_sheet/hm_ecg/", null=True, blank=True)

    def __str__(self):
        return self.title
   
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
    
       
class MyocardialNecrosisBiochemicalMarker(models.Model):

    """Myocardial necrosis biochemical marker(MNBM) model"""

    second_stage = models.ForeignKey(
        verbose_name=_("Second stage data"), to=ConditionAssessmentSheet, 
        on_delete=models.CASCADE, related_name='mnbm_data'
    )
    title = models.CharField(
        verbose_name=_("MNBM title"), max_length=5, 
        choices=extra_data_choices.MyocardialNecrosisBiochemicalMarkerChoices.choices
    )
    value = models.FloatField(verbose_name=_("MNBM value"))
    date = models.DateField(verbose_name=_("MNBM date"))
    file = models.FileField(verbose_name=_("MNBM file"), upload_to="uploads/ca_sheet/mnbm/")
    comment = models.TextField(verbose_name=_("Comment"), null=True, blank=True)
    
    class Meta:
        verbose_name = _("Myocardial necrosis biochemical marker")
        verbose_name_plural = _("Myocardial necrosis biochemical markers")
    
    
class AdditionalTestResult(models.Model):

    """Additional test results model"""

    second_stage = models.ForeignKey(
        verbose_name=_("Second stage data"), to=ConditionAssessmentSheet,
        on_delete=models.CASCADE, related_name='additional_test_results'
    )
    title = models.CharField(verbose_name=_("Title"), max_length=90)
    date = models.DateTimeField(verbose_name=_("Create date"), auto_now_add=True)
    file = models.FileField(verbose_name=_("File"), upload_to="uploads/ca_sheet/additional_test_results/", null=True, blank=True)
    comment = models.TextField(verbose_name=_("Comment"), null=True, blank=True)
    
    class Meta:
        verbose_name = _("Additional test result")
        verbose_name_plural = _("Additional test results")

    def __str__(self):
        return self.title