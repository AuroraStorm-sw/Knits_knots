from django.contrib import admin
from .models import Order, OrderLineItem

# Add all model fields to the admin page
# Source: https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'user_profile',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_basket',
        'stripe_pid',
        )

    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_basket',
        'stripe_pid',
        )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total',
        )

    search_fields = (
        'customer',
        'order_id',
    )

    ordering = ('-date',)
