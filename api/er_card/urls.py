from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'er_card', ElectronicRehabilitationCardViewSet)
router.register(r'icd', InternationalClassificationOfDiseasesViewSet)
router.register(r'admission_data', AdmissionDataViewSet)