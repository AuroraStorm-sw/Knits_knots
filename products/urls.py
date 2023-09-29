from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_all, name='product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list,
         name='category_list'),
    path('add/', views.admin_add_product, name='admin_add_product'),
]
