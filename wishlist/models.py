from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from products.models import Product
from profile.models import User

# Create your models here.


class Wishlist(models.Model):
    """
    Wishlist model for users to save
    items to favorites
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='wishlist'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='wishlist'
    )

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def get_products(self):
        """
        View to show the products on the wishlist
        """
        return self.products.all()

    def add_to_wishlist(self, product):
        """
        View to add a product to the wishlist,
        check if the product is already in the wishlist.
        """
        if product not in self.products.all():
            self.products.add(product)
            return True
        return False

    def remove_from_wishlist(self, product):
        """
        View to remove a product from the wishlist,
        check if the product is in the users wishlist.
        """
        if product in self.products.all():
            self.products.remove(product)
            return True
        return False
