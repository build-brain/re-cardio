from django.db import models
from django.utils.translation import gettext_lazy as _

class DiagnosedByTypeChoices(models.TextChoices):
    
    # Направившее лечебно-профилактическое учреждение 
    OUTPATIENT_FACILITY = 'outpatient_facility', _('Outpatient facility')    
    # Бригада скорая медицинская помощь
    AMBULANCE_BRIGADE = 'ambulance_brigade', _('Ambulance brigade')
    # Приёмное отделение лечебно-профилактическое учреждение
    RECEPTION_DEPARTMENT = 'reception_department', _('Reception department') 
    # Cтационарное отделение лечебно-профилактическое учреждение
    INPATIENT_FACILITY = 'inpatient_facility', _('Inpatient facility')
    
    
class HospitalizationTypeChoices(models.TextChoices):

    # Плановая госпитализация
    PLANNED = 'planned', _('Planned') 
    # Неотложная госпитализация
    URGENT = 'urgent', _('Urgent')
    # Экстренная госпитализация
    EMERGENCY = 'emergency', _('Emergency')

    
class ConditionChoices(models.TextChoices):

    # Удовлетворительное состояние
    SATISFACTORY = 'satisfactory', _('Satisfactory')
    # Состояние средней тяжести
    MODERATE = 'moderate', _('Moderate severity')
    # Тяжёлое состояние
    SEVERE = 'severe', _('Severe')
    # Крайне тяжёлое состояние
    EXTREMELY_SEVERE = 'extremely_severe', _('Extremely severe')


