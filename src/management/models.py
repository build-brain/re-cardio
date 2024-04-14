from random import randint
from datetime import date

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone

from solo.models import SingletonModel

from .choices import *
from .managers import UserManager
from .services.tasks import send_verify_code, send_password
from .utils import get_passport_path


class User(AbstractUser, PermissionsMixin):

    """Main user"""

    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="avatars/", default=settings.NO_AVATAR)
    phone = models.CharField(verbose_name=_("Phone Number"), max_length=15, unique=True)

    middle_name = models.CharField(verbose_name=_("Middle name"), max_length=50, blank=True)
    birth_date = models.DateField(verbose_name=_("Birth date"), default=date(1900, 1, 1))
    pinfl = models.CharField(verbose_name=_("PINFL"), max_length=14)
    passport = models.CharField(verbose_name=_("Passport serial and number"), max_length=9, null=True, blank=True)
    passport_attachment = models.FileField(verbose_name=_("Passport attachment"), upload_to=get_passport_path, null=True, blank=True)

    verify_code = models.PositiveSmallIntegerField(verbose_name=_("Verify Code"), default=0)
    verify_time = models.DateTimeField(verbose_name=_("Verify Time"), default=timezone.now)

    created_at = models.DateTimeField(verbose_name=_("Created Time"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated Time"), auto_now=True)

    user_type = models.CharField(verbose_name=_("User type"), max_length=10, choices=UserTypeChoices.choices)

    email = None
    groups = None
    user_permissions = None

    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def save(self, *args, **kwargs):
        if not self.password:
            self.set_password(self.pinfl)

        self.user_type = self.get_user_type()
        self.username = self.phone
        super().save(*args, **kwargs)

    def get_user_type(self):
        if isinstance(self, Doctor):
            return "DOCTOR"
        elif isinstance(self, Patient):
            return "PATIENT"
        elif isinstance(self, Admin):
            return "ADMIN"
        else:
            return self.user_type

    def change_password(self, password, new_password, confirm_password):
        """ """
        if not self.check_password(password):
            raise ValidationError(_("Password is incorrect!"))

        if new_password != confirm_password:
            raise ValidationError(_("New password and confirmation password are equal!"))

        self.set_password(confirm_password)
        super().save()

    def reset_password(self):
        password = randint(100000, 999999)
        self.set_password(str(password))
        super().save()
        return send_password.delay(self.phone, password)

    def change_avatar(self, avatar):
        self.avatar = avatar
        super().save()

    def generate_verify_code(self):
        code = randint(1000, 9999)
        self.is_active = False
        self.verify_code = code
        self.verify_time = timezone.now() + timezone.timedelta(minutes=settings.VERIFY_CODE_MINUTES)
        return send_verify_code.delay(self.phone, code)

    def regenerate_verify_code(self):
        result = self.generate_verify_code()
        super().save()
        return result

    def verify(self, code):
        if self.verify_code == code and self.verify_time >= timezone.now():
            self.is_active = True
            super().save()
            return True
        return False


class Admin(User, SingletonModel):

    """Admin user model"""

    singleton_instance_id = 2

    class Meta:
        db_table = "admin"
        verbose_name = _("Admin")


class Doctor(User):

    """Doctor user model""" 

    class Meta:
        db_table = "doctor"
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")


class Patient(User):

    """Patient user model"""

    created_by = models.ForeignKey(verbose_name=_("Created doctor"), to=Doctor, related_name="created_patients", on_delete=models.SET_NULL, null=True)
    curator = models.ForeignKey(verbose_name=_("Curator doctor"), to=Doctor, related_name="patients", on_delete=models.SET_NULL, null=True)

    # <-----Demographic data-----> #

    age = models.PositiveSmallIntegerField(verbose_name=_("Age"))
    gender = models.CharField(verbose_name=_("Gender"), max_length=6,choices=GenderChoices.choices)
    ethnicity = models.CharField(verbose_name=_("Ethnicity"), max_length=15, choices=EthnicityChoices.choices, null=True,blank=True)
    social_group = models.CharField(verbose_name=_("Social group"), max_length=20, choices=SocialGroupChoices.choices, null=True, blank=True)
    profession = models.CharField(verbose_name=_("Profession"), max_length=20, choices=ProfessionChoices.choices, null=True, blank=True)

    # <-----Contact data-----> #
    
    additional_phone_number = models.CharField(verbose_name=_("Additional phone Number"), max_length=15, null=True, blank=True)
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)
    telegram_username = models.CharField(verbose_name=_("Telegram username"), max_length=50, null=True, blank=True)

    # <-----Address data-----> #

    district = models.ForeignKey(verbose_name=_("District"), to="District", on_delete=models.SET_NULL, null=True, blank=True)
    # region = models.ForeignKey(verbose_name=_("Region"), to="Region", on_delete=models.SET_NULL, null=True, blank=True)
    region = models.CharField(verbose_name=_("Region"), max_length=150, null=True, blank=True)
    city = models.CharField(verbose_name=_("City"), max_length=150, null=True, blank=True)
    mahalla = models.CharField(verbose_name=_("Mahalla"), max_length=150, null=True, blank=True)
    street = models.CharField(verbose_name=_("Street"), max_length=150, null=True, blank=True)
    building = models.CharField(verbose_name=_("Building"), max_length=10, null=True, blank=True)
    latitude = models.DecimalField(verbose_name=_("Latitude"), max_digits=40, decimal_places=20, null=True, blank=True)
    longitude = models.DecimalField(verbose_name=_("Longitude"), max_digits=40, decimal_places=20, null=True, blank=True)


    class Meta:
        db_table = "patient"
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")


class District(models.Model):

    """District model"""

    name = models.CharField(verbose_name=_("District"), max_length=100)

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")

    def __str__(self):
        return self.name


# class Region(models.Model):

#     """Region model"""

#     name = models.CharField(verbose_name=_("Region"), max_length=100)
#     district = models.ForeignKey(verbose_name=_("District"), to=District, on_delete=models.CASCADE, related_name='regions')

#     class Meta:
#         verbose_name = _("Region")
#         verbose_name_plural = _("Regions")

#     def __str__(self):
#         return self.name