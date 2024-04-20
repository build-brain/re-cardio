from django.db import models
from django.utils.translation import gettext_lazy as _

class GeneralConditionChoices(models.TextChoices):
    
    """Самочувствие в целом"""

    # Хорошее
    GOOD = 'good', _("Good")
    # Удовлетворительное
    SATISFACTORY = 'satisfactory', _("Satisfactory")
    # Неудовлетворительное
    UNSATISFACTORY = 'unsatisfactory', _("Unsatisfactory")


class PulseOnExertionChoices(models.TextChoices):

    """АД и пульс при физических нагрузках"""
    
    # В рекомендуемых пределах (индивидуально);
    RECOMMENDED_LIMITS = 'recommended_limits', _("Within Recommended Limits (Individual)"),
    # Кратковременное превышение;
    BRIEF_EXCEEDING = 'brief_exceeding', _("Brief Exceeding"),
    # Длительное превышение.
    PROLONGED_EXCEEDING = 'prolonged_exceeding', _("Prolonged Exceeding")


class BreathingRhythmChoices(models.TextChoices):

    """Ритмичность и аритмичность"""

    # Ритмичная
    RHYTHMIC = 'rhythmic', _("Rhythmic"),
    # Аритмичная
    ARRHYTHMIC = 'arrhythmic', _("Arrhythmic")

class DyspneaTypeChoices(models.TextChoices):

    """Тип дыхательной недостаточности"""
    
    # Инспираторная
    INSPIRATORY = 'inspiratory', _("Inspiratory"),
    # Экспираторная
    EXPIRATORY = 'expiratory', _("Expiratory"),
    # Смешанная
    MIXED = 'mixed', _("Mixed")


class FatigueTypeChoices(models.TextChoices):

    """Тип утомляемости"""

    # Умеренное
    MODERATE = 'moderate', _("Moderate"),
    # Выраженное, быстро проходящее
    QUICKLY_PASSING = 'quickly_passing', _("Expressed Quickly Passing")
    # Выраженное, кратковременное (до 5 минут)
    SHORT_TERM = 'short_term', _("Expressed Short-term")
    # Выраженное, длительное.
    LONG_TERM = 'long_term', _("Expressed Long-term")


class HeartPainTypeChoices(models.TextChoices):
    
    """Вид боли в области сердца"""
    
    # Нерегулярная
    IRREGULAR = 'irregular', _("Irregular")
    # Легко купируется без нитроглицерина
    RELIVED_WITHOUT_NITROGLYCERIN = 'relieved_without_nitroglycerin', _("Easily Relieved Without Nitroglycerin")
    #  Купируется только нитроглицерином.
    RELIVED_ONLY_NITROGLYCERIN = 'relieved_only_nitroglycerin', _("Relieved Only With Nitroglycerin")

    
class BorgScalePerceptionOfPhysicalEffortChoices(models.IntegerChoices):

    """Восприятие физической нагрузки по шкале Борга"""
    
    # Состояние покоя
    RESTING_STATE = 0, _("Resting State")
    # Очень легко
    VERY_LIGHT = 1, _("Very Light")
    # Легко
    LIGHT = 2, _("Light")
    # Умеренная нагрузка
    MODERATE = 3, _("Moderate")
    # Довольно тяжело
    FAIRLY_HARD = 4, _("Fairly Hard")
    # Тяжело
    HARD = 5, _("Hard")
    # Тяжелее
    HARDER = 6, _("Hard")
    # Очень тяжело
    VERY_HARD = 7, _("Very Hard")
    # Тяжелее очень тяжелого
    VERY_HARDER = 8, _("Very Hard")
    # Очень очень тяжело
    VERY_VERY_HARD = 9, _("Very, Very Hard")
    # Максимальная нагрузка
    MAXIMUM_EFFORT = 10, _("Maximum Effort")