from django.urls import path

from . import views
# URLS for users to view their order history

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
]
