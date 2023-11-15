from django.urls import path, include
from . import views

urlpatterns = [
path('', views.company_info, name='company_info'),
]