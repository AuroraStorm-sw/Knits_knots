from django import forms
from .models import Product, Category, Videocall
from django.forms.widgets import NumberInput
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets


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


class DateInput(forms.DateInput):
    """
    A form to set the input type
    to date
    Source: https://stackoverflow.com/questions/3367091/
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """
    A form to set the input type
    to time
    Source: https://stackoverflow.com/questions/3367091/
    """
    input_type = 'time'


class VideocallForm(forms.ModelForm):

    class Meta:
        model = Videocall
        fields = ('email', 'calltype', 'booking_date', 'booking_time', 'comment',)

        widgets = {
            'booking_date': DateInput(),
            'booking_time': TimeInput(),
            'comment':  forms.Textarea(
                attrs={'placeholder': 'Tell us where you are in your crafting journey so we can help you get where you want to be!'}),
        }