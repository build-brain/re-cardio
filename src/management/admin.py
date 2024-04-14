from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    exclude = ('password', 'username', 'is_staff', 'is_superuser', 'verify_time', 'verify_code')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    exclude = ('password', 'username', 'is_staff', 'is_superuser', 'verify_time', 'verify_code')

# @admin.register(AttachedFile)
# class AttachedFileAdmin(admin.ModelAdmin):
#     pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass