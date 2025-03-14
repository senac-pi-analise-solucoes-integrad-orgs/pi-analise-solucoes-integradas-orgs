from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from core.views import SpecialistViewSet, register_user
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

router = routers.DefaultRouter()
router.register('specialists', SpecialistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', rest_views.obtain_auth_token),
    path('cadastro/', TemplateView.as_view(template_name='cadastro.html'), name='cadastro'),
    path('register/', register_user, name='register'),  # Adicione esta linha
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
