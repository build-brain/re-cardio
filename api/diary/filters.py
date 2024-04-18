from django_filters import rest_framework as filters
from src.diary.models import *

class PhysicalActivityFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='record__creation_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='record__creation_date', lookup_expr='lte')

    class Meta:
        model = PhysicalActivity
        fields = ['start_date', 'end_date']
        
class PhysicalIndicatorsFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='record__creation_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='record__creation_date', lookup_expr='lte')

    class Meta:
        model = PhysicalIndicators
        fields = ['start_date', 'end_date']