from django.db import models
from django.utils.translation import gettext_lazy as _

from src.ca_sheet.utils import get_file_path
from src.ca_sheet.choices.second_stage import *
from .base import ConditionAssessmentSheet

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
    heart_rhythm = models.CharField(verbose_name=_("Heart rhythm"), max_length=50, choices=HeartRhythmChoices.choices)
    st_segment_depression = models.BooleanField(verbose_name=_("ST segment depression"), default=False)
    st_segment_depression_duration = models.BooleanField(verbose_name=_("ST segment depression duration"), default=False)
    st_segment_elevation = models.BooleanField(verbose_name=_("ST segment elevation"), default=False)
    q_wave_or_qs_complex = models.BooleanField(verbose_name=_("Pathalogical Q wave or QS complex"), default=False)
    t_wave_inversion = models.BooleanField(verbose_name=_("T wave inversion "), default=False)
    ecg_attachment = models.FileField(verbose_name=_("ECG attachment"), upload_to="uploads/ecg/", null=True, blank=True)
    ecg_additional = models.FileField(verbose_name=_("ECG additional"), upload_to="uploads/ecg/", null=True, blank=True)

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
    echocg_attachment = models.FileField(verbose_name=_("EchoCG attachment"), upload_to="uploads/echocg/", null=True, blank=True)
    echocg_additional = models.FileField(verbose_name=_("EchoCG additional"), upload_to="uploads/echocg/", null=True, blank=True)

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
    hm_ecg_attachment = models.FileField(verbose_name=_("Holter Monitoring ECG attachment"), upload_to="uploads/hm_ecg/", null=True, blank=True)
    hm_ech_additional = models.FileField(verbose_name=_("Holter Monitoring ECG additional"), upload_to="uploads/hm_ecg/", null=True, blank=True)

    # <-----Myocardial necrosis biochemical markers(MNBM) data-----> #
    
    # <-----Attachment and laboratory results-----> #

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
        verbose_name = _("Myocardial necrosis biochemical marker")
        verbose_name_plural = _("Myocardial necrosis biochemical markers")

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