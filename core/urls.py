from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from api.urls import router
from api.views import LogoutView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin-panel/', admin.site.urls),
    path('user/signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/logout/', LogoutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)