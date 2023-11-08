from django import forms
from .models import Product, Category, Videocall
from django.forms.widgets import NumberInput
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from django.forms.fields import DateField


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()


class VideocallForm(forms.ModelForm):
    # Date input source:
    # https://stackoverflow.com/questions/5449604
    date_input = forms.DateTimeField(
        label="Date",
        required=True,
        widget=NumberInput(attrs={'type':'date'})
    )
    booking_date = forms.DateTimeField()

    class Meta:
        model = Videocall
        fields = ('calltype', 'booking_date', 'email', 'comment',)
    
    def __init__(self, *args, **kwargs):
        super(VideocallForm, self).__init__(*args, **kwargs)
        self.fields['booking_date'].widget = widgets.AdminSplitDateTime()
