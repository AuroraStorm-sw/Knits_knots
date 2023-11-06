from django import forms
from .models import Product, Category, Videocall


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()


class VideocallForm(forms.ModelForm):

    class Meta:
        model = Videocall
        fields = '__all__'
