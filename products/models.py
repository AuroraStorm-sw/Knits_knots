from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import uuid
import datetime


class Category(models.Model):
    """ Model for product categories """
    name = models.CharField(
        max_length=200,
        db_index=True)

    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True)

    slug = models.CharField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Returns the products friendly name
        """
        return self.friendly_name


class Tag(models.Model):
    """ Model for product tags """
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Tag name',
    )

    slug = models.CharField(
        max_length=254,
        unique=True,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Model for products """
    category = models.ForeignKey(
        Category,
        related_name='product',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    name = models.CharField(
        max_length=200,
        blank=True)
    brand = models.CharField(
        max_length=200,
        blank=True)
    sku = models.CharField(
        max_length=60,
        null=True,
        blank=True)
    description = models.TextField(
        blank=True)
    image = models.ImageField(
        null=True,
        blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    tags = models.ManyToManyField(
        Tag,
        related_name='products',
        verbose_name='Tags',
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def _generate_sku_number(self):
        """
        Generate a random, unique SKU
        with UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to
        generate an order id if one hasn't
        been set
        """
        if not self.sku:
            self.sku = self._generate_sku_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Videocall(models.Model):
    """
    A model for registered users to book a private
    videocall tutorial
    """

    MATERIAL = 'Material'
    CROCHET = 'Crochet'
    KNITTING = 'Knitting'
    EMBROIDERY = 'Embroidery'
    CROSSTITCH = 'Cross-stitch'

    CALL_CHOICES = (
        (MATERIAL, 'Material'),
        (CROCHET, 'Crochet'),
        (KNITTING, 'Knitting'),
        (EMBROIDERY, 'Embroidery'),
        (CROSSTITCH, 'Cross-stitch'),
    )
    calltype = models.CharField(
        max_length=200,
        choices=CALL_CHOICES,
        default='Material'
    )
    email = models.EmailField(
        blank=False,
    )
    booking_date = models.DateTimeField(
        default=datetime.datetime.now,
        editable=True,
        blank=False
    )
    booking_time = models.TimeField(
        editable=True,
        blank=False
    )
    comment = models.TextField(
        max_length=500,
    )
    created_on = models.DateTimeField(
        default=datetime.datetime.now,
        blank=True,
    )

    def __str__(self):
        return self.calltype
