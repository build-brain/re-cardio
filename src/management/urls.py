from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    AdminViewSet,
    DoctorViewSet,
    PatientViewSet,
    DistrictViewSet,
    PatientAttachmentViewSet
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'patient-attachments', PatientAttachmentViewSet)
