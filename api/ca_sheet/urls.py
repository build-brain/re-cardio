from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'medication-groups', MedicationGroupViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'condition-assessments', ConditionAssessmentSheetViewSet)
router.register(r'first-stage-data', FirstStageDataViewSet)
router.register(r'second-stage-data', SecondStageDataViewSet)
router.register(r'mnbm', MyocardialNecrosisBiochemicalMarkerViewSet)
router.register(r'additional-test-results', AdditionalTestResultViewSet)
router.register(r'third-stage-data', ThirdStageDataViewSet)
