from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_all, name='product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list,
         name='category_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
