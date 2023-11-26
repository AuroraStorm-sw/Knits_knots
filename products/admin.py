from django.contrib import admin
from .models import Category, Product, Tag, Videocall
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Admin for Tag model """
    list_display = (
        'name',
        'slug',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Admin for category model """
    list_display = (
        'name',
        'friendly_name',
        'slug',
        )

    prepopulated_fields = {"friendly_name": ["name", ]}
    prepopulated_fields = {"slug": ["slug", ]}


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """ Admin for Product model and Summernote """
    list_display = (
        'id',
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
    """ Admin for Videocall model """
    list_display = (
        'id',
        'calltype',
        'booking_date',
        'comment',
        )

    search_fields = [
        'calltype',
    ]

    ordering = ('calltype',)
