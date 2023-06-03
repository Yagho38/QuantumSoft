from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import TemplateView
from .views import *
from django.contrib.auth import views as auth_views
import uuid


urlpatterns = [
    path('', home, name='home'),
]