from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
import uuid

urlpatterns = [
	path('', include('Produto.urls')),
	path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
