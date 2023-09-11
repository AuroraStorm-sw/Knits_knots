from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
]
