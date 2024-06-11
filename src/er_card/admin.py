from django.contrib import admin
from .models import (
    ElectronicRehabilitationCard, 
    Event, 
    ERCardAttachment, 
    AdmissionData, 
    AdmissionAttachment, 
    InternationalClassificationOfDiseases, 
    ConditionAssessmentSheet, 
    Complication
)


class EventInline(admin.TabularInline):
    model = Event


class ERCardAttachmentInline(admin.TabularInline):
    model = ERCardAttachment


class AdmissionAttachmentInline(admin.TabularInline):
    model = AdmissionAttachment


@admin.register(ElectronicRehabilitationCard)
class ElectronicRehabilitationCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'created_by', 'is_active']
    inlines = [EventInline, ERCardAttachmentInline]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'er_card', 'title', 'type', 'location', 'start_date', 'end_date']


@admin.register(ERCardAttachment)
class ERCardAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'er_card', 'title']


@admin.register(AdmissionData)
class AdmissionDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'er_card', 'admission_date', 'patient_condition', 'heart_stopped']
    inlines = [AdmissionAttachmentInline]


@admin.register(AdmissionAttachment)
class AdmissionAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'admission_data', 'title']


@admin.register(InternationalClassificationOfDiseases)
class InternationalClassificationOfDiseasesAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'title']


@admin.register(ConditionAssessmentSheet)
class ConditionAssessmentSheetAdmin(admin.ModelAdmin):
    list_display = ['id', 'er_card', 'morisky_green', 'examination_date', 'weight', 'height', 'body_mass_index', 'body_temperature', 'systolic_pressure', 'diastolic_pressure', 'pulse_rate', 'respiratory_rate', 'spo2', 'moist_rales', 'lower_limb_edema', 'creatinine', 'troponin', 'coronary_insufficiency', 'killip', 'nyha', 'st_segment_elevation', 't_wave_inversion', 'ami_clinical_case', 'ami_date', 'ami_localization', 'mi_type', 'myocardium_damage', 'acs_characteristics', 'coronary_angiography', 'stenting', 'revascularization', 'revascularization_type', 'coronary_lesion_degree', 'affected_vessel_name', 'vessel_lesion_volume', 'index_syntax', 'issue_date', 'primary_disease', 'accompanying_pathologies', 'accompanying_pathologies_type', 'grace_score', 'patient_severity_class', 'created_at', 'updated_at']
    list_filter = ['morisky_green', 'examination_date', 'coronary_insufficiency', 'killip', 'nyha', 'st_segment_elevation', 't_wave_inversion', 'ami_clinical_case', 'ami_date', 'mi_type', 'myocardium_damage', 'acs_characteristics', 'coronary_angiography', 'stenting', 'revascularization', 'coronary_lesion_degree', 'issue_date', 'primary_disease', 'accompanying_pathologies', 'accompanying_pathologies_type', 'grace_score', 'patient_severity_class', 'created_at', 'updated_at']
    search_fields = ['er_card__patient__first_name', 'er_card__patient__last_name', 'examination_date', 'primary_disease__title']
    readonly_fields = ['body_mass_index', 'grace_score', 'lethality_hospital', 'lethality_six_months', 'risk_hospital', 'risk_six_months', 'patient_severity_class']


@admin.register(Complication)
class ComplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'name']
    list_filter = ['group']
    search_fields = ['name']
