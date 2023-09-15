from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model for product categories
    """
    name = models.CharField(
        max_length=200,
        db_index=True)
    slug = models.SlugField(
        max_length=200,
        unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse(
            'products:category_list',
            args=[self.slug])

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    Model for product tags
    """
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True, blank=False,
        verbose_name='Tagname',
    )
    slug = models.SlugField(
        max_length=120,
        null=False,
        unique=True,
        blank=False,
        verbose_name='TagSlug',
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model for products
    """
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
    slug = models.SlugField(
        max_length=200)
    tags = models.ManyToManyField(
        Tag,
        related_name='products',
        verbose_name='Tags',)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])


