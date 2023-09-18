from django.contrib import admin
from .models import Order, OrderProduct, ShippingAdress

# Add all model fields to the admin page
# Source: https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'customer',
        'date_ordered',
        'complete',
        'created',
    )

    search_fields = (
        'customer',
        'order_id',
    )

    ordering = (
        'date_ordered',
    )


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderProduct._meta.get_fields()]

    search_fields = (
        'order',
        'date_ordered',
    )


@admin.register(ShippingAdress)
class ShippingAdressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ShippingAdress._meta.get_fields()]

    search_fields = (
        'customer',
        'order',
        'date_added',
    )
