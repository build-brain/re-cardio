from django.db import models
from django.utils.translation import gettext_lazy as _


class EjectionFractionChoices(models.TextChoices):
    
    """Cнижение насосной функции левого желудочка"""

    # Фракция выброса менее 54%
    LT_54 = 'lt-54', _('Less than 54%')
    # Фракция выброса менее 40%
    LT_40 = 'lt-40', _('Less than 40%')

    
class HeartRhythmChoices(models.TextChoices):
    
    """Сердечный ритм"""
    
    # Нормальный синусовый
    NORMAL_SINUS = 'normal_sinus', _('Normal sinus rhythm')
    # Аритмия любого вида
    ARRHYTHMIA = 'arrhythmia', _('Arrhythmia of any kind')
    # Ритм ЭКС
    EX_RHYTHM = 'ex_rhythm', _('EX rhythm')