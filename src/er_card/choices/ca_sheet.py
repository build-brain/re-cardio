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
    

class CoronaryInsufficiencyChoices(models.IntegerChoices):
    
    """Коронарная недостаточность (стенокардия)"""
    
    # Cтенокардия отсутствует
    ABSENT = 1, _('Absent')
    # Cтенокардия редкая
    RARE = 2, _('Rare') # без изменений ЭКГ
    # Cтенокардия умеренная
    MODERATE = 3, _('Moderate') # (< 5 приступов в сутки)
    # Cтенокардия частая
    FREQUENT = 4, _('Frequent') # (> 5 приступов в сутки)
    

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
    

class MyocardiumDepthExtentChoices(models.IntegerChoices):
    
    """Глубина и обширность поражения миокарда"""
    
    # ИМ мелкоочаговый
    SMALL_FOCAL = 1, _('Small-focal')
    # ИМ крупноочаговый нетрансмуральный
    MACROFOCAL_NONTRANSMURAL = 2, _('Macrofocal nontransmural')
    # ИМ трансмуральный или циркулярный субэндокардиальный
    TRANSMURAL_CIRCULAR = 3, _('Transmural circular')


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


class ACSTypeChoices(models.TextChoices):

    """Тип острого коронарного синдрома"""

    # Острый миокардиальный инфаркт с подъемом сегмента ST
    STEMI = 'stemi', _('ST-Elevation Myocardial Infarction')
    # Острый миокардиальный инфаркт без подъема сегмента ST
    NSTEMI = 'nstemi', _('No ST-Elevation Myocardial Infarction')


class RiskTypeChoices(models.TextChoices):

    """Риск летальности"""

    # Низкий
    LOW = 'low', _('Low')
    # Средний
    MEDIUM = 'medium', _('Medium')
    # Высокий
    HIGH = 'high', _('High')

    
class ComplicationGroupChoices(models.IntegerChoices):
    
    """Группы осложнений"""

    # Первая группа осложнений
    I = 1, _('I complication group')
    # Вторая группа осложнений
    II = 2, _('II complication group')
    # Третья группа осложнений 
    III = 3, _('III complication group')
