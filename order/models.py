import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
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
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=False,
        null=True,
        blank=False)
    order_id = models.CharField(
        max_length=200,
        null=True,
        editable=False)
    created = models.DateTimeField(
        auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Customer Order'
        verbose_name_plural = 'Customer Orders'

    def update_total(self):
        """
        Update the total sum including shipping
        for each orderitem added
        """
        self.order_total = self.orderitem.aggregate(
                            Sum('orderitem_total'))['orderitem_total__sum']
        if self.order_total < settngs.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def _generate_order_number(self):
        """
        Generate a random, unique order number
        with UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to
        generate an order id if one hasn't
        been set
        """
        if not self.order_id:
            self.order_id = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.order_id)


class OrderProduct(models.Model):
    """
    Model for products in a customer's
    order
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        related_name='orderitem',
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

    def save(self, *args, **kwargs):
        """
        Override the original save method to
        set the total cost for order items
        and update the customers order total
        """
        self.total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class ShippingAdress(models.Model):
    """
    Model for customer shipping address
    """
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
