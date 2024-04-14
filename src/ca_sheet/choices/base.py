from django.db import models
from django.utils.translation import gettext_lazy as _
    

class PatientSeverityClassChoices(models.IntegerChoices):
    
    """Класс тяжести пациента"""

    # I класс тяжести
    I_CLASS = 1, _('I class')
    # II класс тяжести
    II_CLASS = 2, _('II class')
    # III класс тяжести
    III_CLASS = 3, _('III class')
    # IV класс тяжести
    IV_CLASS = 4, _('IV class')
    

class ACSTypeChoices(models.TextChoices):

    """Тип острого коронарного синдрома"""

    # Острый миокардиальный инфаркт с подъемом сегмента ST
    STEMI = 'stemi', _('ST-Elevation Myocardial Infarction')
    # Острый миокардиальный инфаркт без подъема сегмента ST
    NSTEMI = 'nstemi', _('No ST-Elevation Myocardial Infarction')


class LethalityTypeChoices(models.TextChoices):

    """Вил летальности"""

    # Внутригоспитальная
    IN_HOSPITAL = 'in_hospital', _('In hospital'),
    # В течение 6 месяцев
    SIX_MONTHS = 'six_months', _('Within six months')


class RiskChoices(models.TextChoices):

    """Риск"""

    # Низкий
    LOW = 'low', _('Low')
    # Средний
    MEDIUM = 'medium', _('Medium')
    # Высокий
    HIGH = 'high', _('High')