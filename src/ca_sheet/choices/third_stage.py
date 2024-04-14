from django.db import models
from django.utils.translation import gettext_lazy as _


class HeartRhythmDisturbancesChoices(models.TextChoices):
    
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


class CoronaryInsufficiencyChoices(models.TextChoices):
    
    """Коронарная недостаточность (стенокардия)"""
    
    # Cтенокардия отсутствует
    ABSENT = 'absent', _('Absent')
    # Cтенокардия редкая
    RARE = 'rare', _('Rare') # без изменений ЭКГ
    # Cтенокардия умеренная
    MODERATE = 'moderate', _('Moderate') # (< 5 приступов в сутки)
    # Cтенокардия частая
    FREQUENT = 'frequent', _('Frequent') # (> 5 приступов в сутки)
    

class AHFSeverityChoices(models.IntegerChoices):
    
    """Класс тяжести ОСН по классификации Киллипа"""

    # Норма, Нет клинических признаков недостаточности левого желудочка
    NORMAL = 1, _('Normal')
    # Слегка уменьшено, Легкая и умеренная недостаточность левого желудочка
    SLIGHTLY_REDUCED = 2, _('Slightly reduced') 
    # Аномальный, Острая недостаточноть левого желудочка, отёк легких
    ANOMALOUS = 3, _('Anomalous')
    # Тяжелая степень недостаточности, Кардиогенный шок: гипотония, тахикардия, 
    # энцефалопатия, похолодание оконечностей, олигоурия, гипоксия
    SEVERE_DEFICENCY = 4, _('Severe deficiency')
    

class FunctionalClassChoices(models.IntegerChoices):
    
    """Функциональный класс по классификации NYHA"""

    # Норма, Обычная физическая активность не приводит к появлению усталости, 
    # одышки или сердцебиения. Допустимая нагрузка ≤ 7 МЕТ.
    NORMAL = 1, _('Normal')
    # Легкий, Обычная физическая нагрузка приводит к появлению усталости, 
    # одышки, сердцебиения. Допустимая нагрузка ≤ 5 МЕТ.
    LIGHT = 2, _('Light') 
    # Умеренный, Хорошее самочувствие в покое. Небольшая физическая нагрузка
    # приводит к появлению усталости, одышки, сердцебиения. Допустимая нагрузка ≤ 2 МЕТ.
    MODERATE = 3, _('Anomalous')
    # Тяжелый, Симптомы возникают в состоянии покоя; любая физическая нагрузка 
    # усиливает дискомфорт. Нагрузки не допускаются.
    SEVERRE = 4, _('Severe')


class AMILocalizationChoices(models.TextChoices):
    
    """Локализация ОИМ"""

    # Передняя стенка
    ANTERIOR_WALL = 'anterior_wall', _('Anterior wall')
    # Передневерхушечный
    ANTERIOR_APICAL = 'anterior_apical', _('Anterior-apical')
    # Переднебоковой
    ANTEROLATERAL = 'anterolateral', _('Anterolateral')
    # Переднеперегородочный
    ANTERIOR_SEPTAL = 'anterior_septal', _('Anterior septal')
    # Диафрагмальный
    DIAPHRAGMATIC = 'diaphragmatic', _('Diaphragmatic')
    # Нижнебоковой
    INFEROLATERAL = 'inferolateral', _('Inferolateral') 
    # Нижнезадний
    INFEROPOSTERIOR = 'inferoposterior', _('Inferoposterior')
    # Нижнебазальный
    INFEROBASAL = 'inferobasal', _('Inferobasal')
    # Верхушечно-боковой
    APICAL_LATERAL = 'apical_lateral', _('Apical-lateral')
    # Базальнолатеральный
    BASALOLATERAL = 'basalolateral', _('Basal-lateral')
    # Верхнебоковой
    SUPEROLATERAL = 'superolateral', _('Superolateral') 
    # Боковой
    LATERAL = 'lateral', _('Lateral')
    # Задний
    REAR = 'rear', _('Rear')
    # Заднебазальный
    POSTEROBASAL = 'posterobasal', _('Posterobasal')
    # Заднебоковой
    POSTEROLATERAL = 'posterolateral', _('Posterolateral')
    # Заднеперегородочный
    POSTEROSEPTAL = 'posteroseptal', _('Posteroseptal')
    # Перегородочный
    SEPTAL = 'septal', _('Septal')
    # Правый желудочек
    RIGHT_VENTRICLE = 'right_ventricle', _('Right ventricle')

    
class MITypeChoices(models.TextChoices):

    """Тип Инфаркта миокарда"""

    TYPE_1  = 'type_1',  _('Spontaneous MI caused by rupture or erosion of the ASB')
    TYPE_2  = 'type_2',  _('Secondary myocardial infarction associated with decreased oxygen supply')
    TYPE_3  = 'type_3',  _('Sudden coronary death')
    TYPE_4A = 'type_4a', _('MI associated with PCI')
    TYPE_4B = 'type_4b', _('MI associated with stent thrombosis after PCI')
    TYPE_4C = 'type_4c', _('MI associated with restenosis after PCI')
    TYPE_5  = 'type_5',  _('MI associated with coronary artery bypass grafting.')
    

class MyocardiumDepthExtentChoices(models.TextChoices):
    
    """Глубина и обширность поражения миокарда"""
    
    # ИМ мелкоочаговый
    SMALL_FOCAL = 'small_focal', _('Small-focal')
    # ИМ крупноочаговый нетрансмуральный
    MACROFOCAL_NONTRANSMURAL = 'macrofocal_nontransmural', _('Macrofocal nontransmural')
    # ИМ трансмуральный или циркулярный субэндокардиальный
    TRANSMURAL_CIRCULAR = 'transmural_circular', _('Transmural circular')


class ACSCharacteristicsChoices(models.TextChoices):
    
    """Характеристика острого коронарного синдрома"""

    # Нестабильная стенокардия
    UNSTABLE_ANGINA = 'unstable_angina', _('Unstable angina')
    # ИМ без подъема сегмента ST (ИМбST)
    MI_WITHOUT_ST = 'mi_without_st', _('Myocardial Infarction without ST')
    # ИМ с элевацией сегмента ST (ИМсST)
    MI_WITH_ST = 'mi_with_st', _('Myocardial Infarction with ST')
    # ИМ без зубца Q
    MI_WITHOUT_Q_WAVE = 'mi_without_q_wave', _('Myocardial Infarction without Q wave')
    # ИМ с зубцом Q
    MI_WITH_Q_WAVE = 'mi_with_q_wave', _('Myocardial Infarction with Q wave')

    
class CoronaryLesionDegreeChoices(models.TextChoices):
    
    """Степень поражения коронарного русла"""

    # Однососудистое
    SINGLE_VESSEL = 'single_vessel', _('Single vessel')
    # Двухсосудистое
    TWO_VESSEL = 'two_vessel', _('Two vessel')
    # Многососудистое
    MULTIVESSEL = 'multivessel', _('Multivessel')


class AffectedVesselNameChoices(models.TextChoices):
    
    """Название пораженного сосуда"""

    # Ствол левой коронарной артерии
    LEFT_CORONARY_ARTERY_TRUNK = 'left_coronary_artery_trunk', _('Left coronary artery trunk')
    # Передняя нисходящая артерия 
    ANTERIOR_DESCENDING_ARTERY = 'anterior_descending_artery', _('Anterior descending artery')
    # Диагональная(ые) артерия(и)
    DIAGONAL_ARTERY = 'diagonal_artery', _('Diagonal artery')
    # Огибающая артерия
    CIRCUMFLEX_ARTERY = 'circumflex_artery', _('Circumflex artery')
    # Ветвь тупого края
    BLUNT_EDGE_BRANCH = 'blunt_edge_branch', _('Blunt edge branch')
    # Перегородочные межжелудочковые ветви
    SEPTAL_INTERVENTRICULAR_BRANCHES = 'septal_interventricular_branches', _('Septal interventricular branches')
    # Промежуточная артерия
    INTERMEDIATE_ARTERY = 'intermediate_artery', _('Intermediate artery')
    # Правая коронарная артерия
    RIGHT_CORONARY_ARTERY = 'right_coronary_artery', _('Right coronary artery')
    # Ветвь острого края
    SHARP_EDGE_BRANCH = 'sharp_edge_branch', _('Sharp edge branch')
    # Артерия синоатриального узла
    SINOATRIAL_NODE_ARTERY = 'sinoatrial_node_artery', _('Sinoatrial node Artery')
    # Задняя межжелудочковая ветвь
    POSTERIOR_INTERVENTRICULAR_BRANCH = 'posterior_interventricular_branch', _('Posterior interventricular branch')