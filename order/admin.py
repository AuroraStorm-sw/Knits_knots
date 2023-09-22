from django.contrib import admin
from .models import Order, OrderProduct, ShippingAdress

# Add all model fields to the admin page
# Source: https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page


class OrderItemAdminInline(admin.TabularInline):
    """
    Class to display ordered items on the same page
    as customer orders in case adjustments needs to be made
    """
    model = OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Class to display custom orders
    """
    inlines = (OrderItemAdminInline,)

    list_display = (
        'order_id',
        'customer',
        'date_ordered',
        'status',
        'created',
        'grand_total',
        'order_total',
    )

    search_fields = (
        'customer',
        'order_id',
    )

    ordering = (
        '-date_ordered',
    )

    readonly_fields = (
        'order_id',
        'date_ordered',
        'status',
        'created',
        'grand_total',
        'order_total',
    )


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    """
    Class to add an inline display for ordered items
    in OrderAdmin
    """
    list_display = [field.name for field in OrderProduct._meta.get_fields()]

    search_fields = (
        'order',
        'date_ordered',
    )


@admin.register(ShippingAdress)
class ShippingAdressAdmin(admin.ModelAdmin):
    """
    Class for customer adress
    """
    list_display = [field.name for field in ShippingAdress._meta.get_fields()]

    search_fields = (
        'customer',
        'order',
        'date_added',
    )
