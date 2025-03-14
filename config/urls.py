from django.urls import include
from rest_framework import routers
from rest_framework.authtoken import views as rest_views

from core.views import SpecialistViewSet

router = routers.DefaultRouter()
router.register('specialists', SpecialistViewSet)
from django.contrib import admin
from django.urls import path
from core.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', register_user, name='register_user'),
    path('api-token-auth/', rest_views.obtain_auth_token),
]
