from django.contrib import admin
from src.er_card.models.third_stage import (
    ThirdStageData
)


@admin.register(ThirdStageData)
class ThirdStageDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'ca_sheet', 'coronary_insufficiency', 'ahf_severity_class', 'nyha_functional_class')
    list_filter = ('coronary_insufficiency', 'ahf_severity_class', 'nyha_functional_class')
    search_fields = ('ca_sheet__id',)
    readonly_fields = ('ca_sheet',)
