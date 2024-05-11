from rest_framework import routers
from .views import HealthDiaryRecordViewSet

router = routers.DefaultRouter()

router.register(r'health-diary-records', HealthDiaryRecordViewSet)
