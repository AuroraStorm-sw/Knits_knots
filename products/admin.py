from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
        )

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
        'description',
        'sku',
        'image',
        'price',
        'slug',
    )

    search_fields = [
        'name',
        'category',
    ]

    ordering = ('name', 'category')

    prepopulated_fields = {'slug': ('name',)}
