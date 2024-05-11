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
    
    
class HeartRhythmDisordersChoices(models.TextChoices):
    
    """Формы нарушений ритма сердца"""
    
    # Синусовая тахикардия
    SINUS_TACHYCARDIA = 'sinus_tachycardia', _('Sinus tachycardia')
    # Синусовая брадикардия
    SINUS_BRADYCARDIA = 'sinus_bradycardia', _('Sinus bradycardia')
    # Синусовая аритмия
    SINUS_ARRHYTHMIA = 'sinus_arrhythmia', _('Sinus arrhythmia')
    # Синдром слабости синусового узла
    SICK_SINUS_SYNDROME = 'sick_sinus_syndrome', _('Sick sinus syndrome')
    # Нижнепредсердный ритм
    LOW_ATRIAL_RHYTHM = 'low_atrial_rhythm', _('Low atrial rhythm')
    # Атриовентрикулярный ритм
    ATRIOVENTRICULAR_RHYTHM = 'atrioventricular_rhythm', _('Atrioventricular rhythm')
    # Идиовентрикулярный ритм
    IDIOVENTRICULAR_RHYTHM = 'idioventricular_rhythm', _('Idioventricular rhythm')
    # Предсердная экстрасистолия
    ATRIAL_PREMATURE_BEAT = 'atrial_premature_beat', _('Atrial premature beat')
    # Атриовентрикулярная экстрасистолия
    ATRIOVENTRICULAR_PREMATURE_BEAT = 'atrioventricular_premature_beat', _('Atrioventricular premature beat')
    # Желудочковая экстрасистолия
    VENTRICULAR_PREMATURE_BEAT = 'ventricular_premature_beat', _('Ventricular premature beat')
    # Пароксизмальная тахикардия
    PAROXYSMAL_TACHYCARDIA = 'paroxysmal_tachycardia', _('Paroxysmal tachycardia')
    # Синоаурикулярная блокада
    SINOATRIAL_BLOCK = 'sinoatrial_block', _('Sinoatrial block')
    # Атриовентрикулярная блокада
    ATRIOVENTRICULAR_BLOCK = 'atrial_block', _('Atrioventricular block')
    # Неполная блокада левой ножки пучка Гиса
    LEFT_BUNDLE_BRANCH_BLOCK = 'left_bundle_branch_block', _('Left bundle branch block')
    # Неполная блокада правой ножки пучка Гиса
    RIGHT_BUNDLE_BRANCH_BLOCK = 'right_bundle_branch_block', _('Right bundle branch block')
    # WPW синдром
    WOLFF_PARKINSON_WHITE_SYNDROME = 'wolff_parkinson_white_syndrome', _('Wolff-Parkinson-White syndrome')
    # Трепетание предсердий
    ATRIAL_FLUTTER = 'atrial_flutter', _('Atrial flutter')
    # Фибрилляция предсердий
    ATRIAL_FIBRILLATION = 'atrial_fibrillation', _('Atrial fibrillation')
    # Трепетание желудочков
    VENTRICULAR_FLUTTER = 'ventricular_flutter', _('Ventricular flutter')
    # Фибрилляция желудочков
    VENTRICULAR_FIBRILLATION = 'ventricular_fibrillation', _('Ventricular fibrillation')


class MyocardialNecrosisBiochemicalMarkerChoices(models.TextChoices):
    
    """Биохимические маркеры некроза миокарда"""

    # Скорость оседания эритроцитов 
    ESR = 'esr', _('Erythrocyte sedimentation rate')
    # Гликированный гемоглобин 
    GH = 'gh', _('Glycated hemoglobin')
    # Скорость клубочковой фильтрации по CKD-EPI 
    GFR = 'gfr', _('Glomerular filtration rate by CKD-EPI')
    # Креатинфосфокиназа-МВ
    CRMB = 'crmb', _('Creatine phosphokinase-MB')
    # С-реактивный белок
    CRP = 'crp', _('C-reactive protein')
    # Мозговой натрийуретический пропептид 
    BNP = 'bnp', _('Brain natriuretic propeptide')





    
