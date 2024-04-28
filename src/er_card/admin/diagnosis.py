from django.contrib import admin
from src.er_card.models.diagnosis import (
    ClinicalDiagnosis, 
    Complication,
    GraceScale
)
    

@admin.register(ClinicalDiagnosis)
class ClinicalDiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'ca_sheet', 'issue_date', 'primary_disease', 'accompanying_pathologies', 'grace')
    list_filter = ('primary_disease', 'accompanying_pathologies', 'grace')
    search_fields = ('primary_disease__name', 'ca_sheet__er_card__patient__first_name', 'ca_sheet__er_card__patient__last_name')
    readonly_fields = ('issue_date',)


@admin.register(Complication)
class ComplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'complication')
    list_filter = ('group',)
    search_fields = ('complication',)


@admin.register(GraceScale)
class GraceScaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'acs_type', 'lethality_type', 'score_range_start', 'score_range_end', 'risk', 'lethality_start', 'lethality_end')
    list_filter = ('acs_type', 'lethality_type', 'risk')
    search_fields = ('acs_type', 'lethality_type', 'risk')