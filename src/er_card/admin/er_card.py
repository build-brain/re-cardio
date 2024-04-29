from django.contrib import admin
from src.er_card.models.er_card import (
    ElectronicRehabilitationCard,
    AdmissionData,
    InternationalClassificationOfDiseases, 
    AttachedFile,
    ConditionAssessmentSheet
)


@admin.register(ElectronicRehabilitationCard)
class ElectronicRehabilitationCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'created_by', 'is_active', 'created_at', 'updated_at',)
    list_filter = ('is_active',)
    search_fields = ('patient__name', 'created_by__name',)
    

@admin.register(AdmissionData)
class AdmissionDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'er_card', 'admission_date', 'delivery_time', 'patient_condition', 'heart_stopped', 'hospitalization_date', 'hospitalization_type', 'preliminary_diagnosis', 'diagnosed_by')
    list_filter = ('patient_condition', 'heart_stopped', 'hospitalization_type', 'preliminary_diagnosis__code', 'diagnosed_by')
    search_fields = ('er_card__id', 'admission_date', 'preliminary_diagnosis__title', 'additional_information')


@admin.register(InternationalClassificationOfDiseases)
class InternationalClassificationOfDiseasesAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')
    search_fields = ('code', 'title')


@admin.register(AttachedFile)
class AttachedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'er_card', 'title', 'attachment')
    search_fields = ('title',)


@admin.register(ConditionAssessmentSheet)
class ConditionAssessmentSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'er_card', 'created_at', 'updated_at', 'is_active', 'created_by')
    list_filter = ('is_active',)
    search_fields = ('er_card__patient__first_name', 'er_card__patient__last_name', 'created_by__user__username')
    readonly_fields = ('created_at', 'updated_at')
