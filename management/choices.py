from django.db import models
from django.utils.translation import gettext_lazy as _
 

class UserTypeChoices(models.TextChoices):
    
    # Администратор
    ADMIN = 'admin', _('Admin')
    # Доктор
    DOCTOR = 'doctor', _('Doctor')
    # Пациент
    PATIENT = 'patient', _('Patient')


class GenderChoices(models.TextChoices):

    # Мужчина
    MALE = 'male', _('Male')
    # Женщина
    FEMALE = 'female', _('Female')


class EthnicityChoices(models.TextChoices):

    # Азиаты
    ASIAN = 'asian', _('Asian')
    # Европейцы
    EUROPEAN = 'european', _('European')
    # Прочие
    OTHER = 'other', _('Other')


class SocialGroupChoices(models.TextChoices):

    # Дети, до 16 лет
    CHILD = 'child', _('Child')
    # Трудоспособные, мужчины 16-59 лет, женщины 16-54 лет
    ADULTS = 'adult', _('Adult')
    # Пенсионеры, мужчины >59 лет, женщины >54 лет
    PENSIONERS = 'pensioner', _('Pensioner')
    # Прочие, любого возраста
    OTHER = 'other', _('Other')


class ProfessionChoices(models.TextChoices):

    # Дехкане, работники, занятые в сельском хозяйстве без в/о
    FARMER = 'farmer', _('Farmer') 
    # Рабочие, любые профессии или род деятельности без в/о
    WORKER = 'worker', _('Worker') 
    # Служащие, любые профессии или род деятельности с в/о
    EMPLOYEE = 'employee', _('Employee') 
    # Лица свободных профессий
    FREELANCER = 'freelancer', _('Freelancer') 
    # Священнослужители
    PRIEST = 'priest', _('Priest') 
    # Прочие
    OTHER = 'other', _('Other')

    
class ConditionChoices(models.TextChoices):

    # Удовлетворительное состояние
    SATISFACTORY = 'satisfactory', _('Satisfactory')
    # Состояние средней тяжести
    MODERATE = 'moderate', _('Moderate severity')
    # Тяжёлое состояние
    SEVERE = 'severe', _('Severe')
    # Крайне тяжёлое состояние
    EXTREMELY_SEVERE = 'extremely_severe', _('Extremely severe')


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
