from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.main, name='mainpage'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('courses/<int:id>', views.course, name='coursepage'),
]