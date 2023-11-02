from django.contrib import admin
from .models import Category, Product, Tag, Videocall
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        )

    prepopulated_fields = {"friendly_name": ["name",]}


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
        'description',
        'sku',
        'image',
        'price',
    )
    summernote_fields = ('description',)

    search_fields = [
        'name',
        'category',
    ]

    ordering = ('name', 'category')


@admin.register(Videocall)
class VideocallAdmin(admin.ModelAdmin):
    list_display = (
        'calltype',
        'booking_date',
        'comment',
        )

    search_fields = [
        'calltype',
    ]

    ordering = ('calltype',)
