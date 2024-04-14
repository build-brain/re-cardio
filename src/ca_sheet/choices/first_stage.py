from django.db import models
from django.utils.translation import gettext_lazy as _


class MoriskyGreenChoices(models.IntegerChoices):
    
    """Приверженность к терапии по шкале Мориски-Грин"""

    # Неприверженный
    DISAFFECTED = 1, _('Disaffected')
    # Неприверженный
    UNCOMMITTED = 2, _('Uncommitted')
    # Недостаточно  приверженный
    UNDERCOMMITTED = 3, _('Under committed')
    # Комплаентный 
    COMPLAINT = 4, _('Complaint')