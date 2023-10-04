from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_view, name='wishlist_view'),
    path('add_to_wishlist/<item_id>/',
         views.add_to_wishlist, name='add_to_wishlist'),

]
