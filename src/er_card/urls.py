from rest_framework.routers import DefaultRouter

from .views import (
    ElectronicRehabilitationCardViewSet,
    AdmissionDataViewSet,
    InternationalClassificationOfDiseasesViewSet,
    AdmissionAttachmentViewSet,
    ERCardAttachmentViewSet,
    ConditionAssessmentSheetViewSet,
    ComplicationViewSet
)

router = DefaultRouter()

router.register(r'er-cards', ElectronicRehabilitationCardViewSet)
router.register(r'admission-data', AdmissionDataViewSet)
router.register(r'icd', InternationalClassificationOfDiseasesViewSet)
router.register(r'admission-attachments', AdmissionAttachmentViewSet)
router.register(r'er-card-attachments', ERCardAttachmentViewSet)
router.register(r'ca-sheets', ConditionAssessmentSheetViewSet)
router.register(r'complications', ComplicationViewSet)