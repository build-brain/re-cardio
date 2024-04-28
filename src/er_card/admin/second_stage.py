from django.contrib import admin
from src.er_card.models.second_stage import (
    SecondStageData,
    MyocardialNecrosisBiochemicalMarker,
    AdditionalTestResult
)


@admin.register(SecondStageData)
class SecondStageDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'ca_sheet', 'examination_date', 'ecg_date', 'echocg_date', 'hm_ecg_date')
    list_filter = ('examination_date', 'ecg_date', 'echocg_date', 'hm_ecg_date')
    search_fields = ('ca_sheet__id',)
    readonly_fields = ('ca_sheet',)


@admin.register(MyocardialNecrosisBiochemicalMarker)
class MyocardialNecrosisBiochemicalMarkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'mnbm_date')
    list_filter = ('mnbm_date',)
    search_fields = ('title',)
    readonly_fields = ('second_stage',)


@admin.register(AdditionalTestResult)
class AdditionalTestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('second_stage',)
