from django.urls import path
from . import views

# URLS for users to add and delete products to their wishlist

urlpatterns = [
    path('', views.wishlist_view, name='wishlist_view'),
    path('add_to_wishlist/<item_id>/',
         views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist_item/<item_id>/<redirect_from>/',
         views.delete_wishlist_item, name='delete_wishlist_item'),
]
