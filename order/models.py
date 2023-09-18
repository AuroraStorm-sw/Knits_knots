from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Order(models.Model):
    """
    Model for customer order
    """
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SHIPPED, 'Shipped'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    date_ordered = models.DateTimeField(
        auto_now_add=True)
    complete = models.BooleanField(
        default=False,
        null=True,
        blank=False)
    order_id = models.CharField(
        max_length=200,
        null=True)
    created = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Customer Order'
        verbose_name_plural = 'Customer Orders'


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True)
    date_ordered = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        ordering = ('-date_ordered',)


class ShippingAdress(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    address = models.CharField(
        max_length=200,
        null=True)
    city = models.CharField(
        max_length=200,
        null=True)
    state = models.CharField(
        max_length=200,
        null=True)
    zipcode = models.CharField(
        max_length=200,
        null=True)
    date_added = models.DateField(
        auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ('-order',)
