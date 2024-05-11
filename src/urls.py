from core.routers import DefaultRouter
from src.management.urls import router as management_router
from src.er_card.urls import router as er_card_router
from src.diary.urls import router as diary_router


router = DefaultRouter()

router.extend(management_router)
router.extend(er_card_router)
router.extend(diary_router)

