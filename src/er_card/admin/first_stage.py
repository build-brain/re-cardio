from django.contrib import admin
from src.er_card.models.first_stage import (
    FirstStageData, 
    MedicationGroup, 
    Medication
)


@admin.register(FirstStageData)
class FirstStageDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'ca_sheet', 'main_complaint', 'cvd_medications', 'morisky_green')
    list_filter = ('cvd_medications', 'morisky_green')
    search_fields = ('main_complaint',)
    readonly_fields = ('ca_sheet',)


@admin.register(MedicationGroup)
class MedicationGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'name', 'description')
    list_filter = ('group',)
    search_fields = ('name', 'group__name')