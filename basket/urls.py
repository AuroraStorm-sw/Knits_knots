from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket, name='basket'),
]