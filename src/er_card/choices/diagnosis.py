from django.db import models
from django.utils.translation import gettext_lazy as _


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