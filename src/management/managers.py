from datetime import date

from django.db import models, transaction
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """ """
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError(_("Users must have a phone"))
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, phone, password):
    #     user = self.create_user(phone=phone, password=password)
    #     user.user_type = "SUPERUSER"
    #     user.is_active = True
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using=self._db)
    #     return user

    # @transaction.atomic
    # def signup(self, first_name, password, phone, is_entity, last_name="", company_name=None, tin=None):
    
    #         owner.set_password(password)
    #         owner.generate_verify_code()
    #         owner.save(using=self._db)

    #     else:
    #         customer = Customer(
    #             is_active=False,
    #             phone=phone,
    #             first_name=first_name,
    #             last_name=last_name
    #         )

    #         customer.set_password(password)
    #         customer.generate_verify_code()
    #         customer.save(using=self._db)


