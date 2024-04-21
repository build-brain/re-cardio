from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from src.management.models import *


class ProfileMeta:
    exclude = ["password", "is_staff", "is_superuser", "verify_time", "verify_code"]
    read_only_fields = ["username", "user_type", "created_at", "updated_at", "last_login", "date_joined", "avatar"]


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


class MeAdminSerializer(serializers.ModelSerializer):
    class Meta(ProfileMeta):
        model = Admin


class DoctorSerializer(serializers.ModelSerializer):
    """ """

    class Meta(UserSerializer.Meta):
        model = Doctor



class MeDoctorSerializer(serializers.ModelSerializer):
    class Meta(ProfileMeta):
        model = Doctor


class PatientSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Patient
        fields = [
            "id", "first_name", "last_name", "middle_name", "is_active", "phone", "birth_date",
            "pinfl", "passport", "passport_attachment", "additional_information", "age", "gender",
            "ethnicity", "social_group", "profession", "demographic_additional", "additional_phone_number", 
            "email", "telegram_username", "region", "city", "mahalla", "street", "building",
            "latitude", "longitude", "created_by", "curator", "district", "admission_data"
        ]
        read_only_fields = ProfileMeta.read_only_fields


class MePatientSerializer(serializers.ModelSerializer):
    class Meta(ProfileMeta):
        model = Patient


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'