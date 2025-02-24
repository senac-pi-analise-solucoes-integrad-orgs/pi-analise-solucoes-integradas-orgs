from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from core.views import SpecialistViewSet

router = routers.DefaultRouter()
router.register('specialists', SpecialistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/api-token-auth/', rest_views.obtain_auth_token),
]
