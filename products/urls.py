from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
