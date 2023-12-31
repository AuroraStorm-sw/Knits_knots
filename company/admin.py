from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Admin for contact model """
    list_display = (
        'email',
        'subject',
        )
