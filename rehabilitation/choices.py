from django.db import models
from django.utils.translation import gettext_lazy as _


class ConditionChoices(models.TextChoices):
    SATISFACTORY = 'SATISFACTORY', _('Satisfactory') # удовлетворительное
    MODERATE = 'MODERATE', _('Moderate severity') # средней тяжести
    SEVERE = 'SEVERE', _('Severe') # тяжёлое
    EXTREMELY_SEVERE = 'EXTREMELY_SEVERE', _('Extremely severe') # крайне тяжёлое


class DiagnosedByTypeChoices(models.TextChoices):
    
    # Направившее лечебно-профилактическое учреждение 
    OUTPATIENT_FACILITY = 'OUTPATIENT FACILITY', _('Outpatient facility')    
    # Бригада скорая медицинская помощь
    AMBULANCE_BRIGADE = 'AMBULANCE BRIGADE', _('Ambulance brigade')
    # Приёмное отделение лечебно-профилактическое учреждение
    RECEPTION_DEPARTMENT = 'RECEPTION DEPARTMENT', _('Reception department') 
    # Cтационарное отделение лечебно-профилактическое учреждение
    INPATIENT_FACILITY = 'INPATIENT FACILITY', _('Inpatient facility')
    
    
class HospitalizationTypeChoices(models.TextChoices):
    PLANNED = 'PLANNED', _('Planned') # плановая
    URGENT = 'URGENT', _('Urgent') # неотложная
    EMERGENCY = 'EMERGENCY', _('Emergency') # экстренная