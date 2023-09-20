from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_all, name='product'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
