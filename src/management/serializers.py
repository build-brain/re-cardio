from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from src.management.models import (
    User,
    Admin,
    Doctor,
    Patient,
    District,
    PatientAttachment
)


class ProfileMeta:
    exclude = ["password", "is_staff", "is_superuser", "verify_time", "verify_code"]
    read_only_fields = ["username", "user_type", "created_at", "updated_at", "last_login", "date_joined", "avatar"]


class UserSerializer(serializers.ModelSerializer):
    
    """User model serializer"""

    class Meta(ProfileMeta):
        model = User
        read_only_fields = ProfileMeta.read_only_fields


class ChangeAvatarSerializer(serializers.Serializer):
    
    """Change avatar serializer"""
    
    avatar = serializers.ImageField()


class ChangePasswordSerializer(serializers.Serializer):
    
    """Change password serializer"""
    
    password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)


class PhoneSerializer(serializers.Serializer):

    """Phone serializer"""

    phone = serializers.CharField(required=True)


class VerifySerializer(serializers.Serializer):
    
    """Verify serializer"""

    phone = serializers.CharField()
    code = serializers.IntegerField()


class AdminSerializer(serializers.ModelSerializer):

    """Admin model serializer"""

    class Meta(UserSerializer.Meta):
        model = Admin


class MeAdminSerializer(serializers.ModelSerializer):

    """Me admin model serializer"""

    class Meta(ProfileMeta):
        model = Admin


class DoctorSerializer(serializers.ModelSerializer):

    """Doctor model serializer"""

    class Meta(UserSerializer.Meta):
        model = Doctor


class MeDoctorSerializer(serializers.ModelSerializer):
    
    """Me doctor model serializer"""

    class Meta(ProfileMeta):
        model = Doctor


class PatientAttachmentSerializer(serializers.ModelSerializer):
    
    """Patient attachment model serializer"""

    class Meta:
        model = PatientAttachment
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):

    """Patient model serializer"""
    
    attachments = PatientAttachmentSerializer(many=True, read_only=True)
    
    class Meta(ProfileMeta):
        model = Patient
        read_only_fields = ProfileMeta.read_only_fields


class MePatientSerializer(serializers.ModelSerializer):
    
    """Me patient model serializer"""
    
    class Meta(ProfileMeta):
        model = Patient


class DistrictSerializer(serializers.ModelSerializer):
    
    """District model serializer"""
    
    class Meta:
        model = District
        fields = '__all__'
