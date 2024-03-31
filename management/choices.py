from django.db import models
from django.utils.translation import gettext_lazy as _
 

class UserTypeChoices(models.TextChoices):
    ADMIN = 'ADMIN', _('Admin') # администратор
    DOCTOR = 'DOCTOR', _('Doctor') # доктор
    PATIENT = 'PATIENT', _('Patient') # пациент


class GenderChoices(models.TextChoices):
    MALE = 'MALE', _('Male') # мужчина
    FEMALE = 'FEMALE', _('Female') # женщина


class EthnicityChoices(models.TextChoices):
    ASIAN = 'ASIAN', _('Asian') # азиаты
    EUROPEAN = 'EUROPEAN', _('European') # европейцы
    OTHER = 'OTHER', _('Other') # прочие


class SocialGroupChoices(models.TextChoices):
    CHILDREN = 'CHILDREN', _('Children') # дети, до 16 лет
    ADULTS = 'ADULT', _('Adult') # трудоспособные, мужчины 16-59 лет, женщины 16-54 лет
    PENSIONERS = 'PENSIONER', _('Pensioner') # пенсионеры, мужчины >59 лет, женщины >54 лет
    OTHER = 'OTHER', _('Other') # прочие, любого возраста


class ProfessionChoices(models.TextChoices):
    FARMER = 'FARMER', _('Farmer') # дехкане, работники, занятые в сельском хозяйстве без в/о
    WORKER = 'WORKER', _('Worker') # рабочие, любые профессии или род деятельности без в/о
    EMPLOYEE = 'EMPLOYEE', _('Employee') # служащие, любые профессии или род деятельности с в/о
    FREELANCER = 'FREELANCER', _('Freelancer') # лица свободных профессий
    CLERGY = 'CLERGY', _('Clergy') # священнослужители
    OTHER = 'OTHER', _('Other') # прочие
