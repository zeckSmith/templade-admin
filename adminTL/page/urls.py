
from django.urls import path
from .views import dashboard

from django.conf import settings
from django.conf.urls.static import static


# app_name = 'page'

urlpatterns = [
    path("", dashboard, name='dashboard')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
