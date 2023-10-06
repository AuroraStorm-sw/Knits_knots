from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_all, name='product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.category_list,
         name='category_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
]
