from rest_framework import routers
from .views import RecordViewSet, PhysicalIndicatorsViewSet, PhysicalActivityViewSet

router = routers.DefaultRouter()

router.register(r'records', RecordViewSet)
router.register(r'physical-indicators', PhysicalIndicatorsViewSet)
router.register(r'physical-activity', PhysicalActivityViewSet)