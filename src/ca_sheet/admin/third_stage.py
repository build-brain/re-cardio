from django.contrib import admin
from src.ca_sheet.models.third_stage import *

@admin.register(ThirdStageData)
class ThirdStageDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'ca_sheet', 'coronary_insufficiency', 'ahf_severity_class', 'nyha_functional_class')
    list_filter = ('coronary_insufficiency', 'ahf_severity_class', 'nyha_functional_class')
    search_fields = ('ca_sheet__id',)
    readonly_fields = ('ca_sheet',)
