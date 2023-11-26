from django.urls import path
from . import views

#URLS to view the home template

urlpatterns = [
    path('', views.home, name='home'),
]
