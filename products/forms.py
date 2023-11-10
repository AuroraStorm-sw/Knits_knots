from django import forms
from .models import Product, Category, Videocall
from django.forms.widgets import NumberInput
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from django.forms.fields import DateField


class ProductForm(forms.ModelForm):
    """
    A form for the superuser to add or
    edit products on the webpage
    """

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()


class VideocallForm(forms.ModelForm):

    class Meta:
        model = Videocall
        fields = ('email', 'calltype', 'booking_date', 'comment',)

        widgets = {
            'comment':  forms.Textarea(
                attrs={'placeholder': 'Tell us where you are in your crafting journey so we can help you get where you want to be!'}),
        }
