from django import forms
from order.models import Order, ShippingAdress


class OrderForm(forms.ModelForm):
