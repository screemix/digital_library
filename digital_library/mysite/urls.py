from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home')
]

