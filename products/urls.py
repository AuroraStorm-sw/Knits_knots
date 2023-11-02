from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.product_all, name='product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('summernote/', include('django_summernote.urls')),
]
