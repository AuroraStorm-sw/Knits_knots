from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.company_info, name='company_info'),
    path('faq', views.company_faq, name='company_faq'),
    path('contact', views.company_contact, name='company_contact'),
]
