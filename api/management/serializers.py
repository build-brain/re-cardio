from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from src.management.models import *


class ProfileMeta:
    exclude = ["password", "is_staff", "is_superuser", "verify_time", "verify_code"]
    read_only_fields = ["username", "user_type", "created_at", "updated_at", "last_login"]


class UserSerializer(serializers.ModelSerializer):
    """ """

    class Meta(ProfileMeta):
        model = User
        read_only_fields = ProfileMeta.read_only_fields


class ChangeAvatarSerializer(serializers.Serializer):
    """ """
    avatar = serializers.ImageField()


class ChangePasswordSerializer(serializers.Serializer):
    """ """
    password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)


class VerifySerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.IntegerField()


class AdminSerializer(serializers.ModelSerializer):
    """ """

    class Meta(UserSerializer.Meta):
        model = Admin


class MeAdminSerializer(AdminSerializer):
    class Meta(ProfileMeta):
        model = Admin
        read_only_fields = ProfileMeta.read_only_fields


class DoctorSerializer(serializers.ModelSerializer):
    """ """

    class Meta(UserSerializer.Meta):
        model = Doctor


class MeDoctorSerializer(AdminSerializer):
    class Meta(ProfileMeta):
        model = Doctor
        read_only_fields = ProfileMeta.read_only_fields


class PatientSerializer(serializers.ModelSerializer):
    """ """

    class Meta(UserSerializer.Meta):
        model = Patient


class MePatientSerializer(AdminSerializer):
    class Meta(ProfileMeta):
        model = Patient
        read_only_fields = ProfileMeta.read_only_fields
        

# class AttachedFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AttachedFile
#         fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'