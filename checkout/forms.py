from django import forms
from order.models import Order, ShippingAdress


class OrderFormAddress(forms.ModelForm):
    model = ShippingAdress
    fields = (
        'name',
        'surname',
        'email',
        'address',
        'city',
        'postcode',
        'country',
    )

    def __init__(self, *args, **kwargs):
        """
        Placeholders for form input fields
        """
        super()-__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'surname': 'Surname',
            'email': 'Email',
            'adress': 'Address',
            'city': 'City',
            'postcode': 'Postal code',
            'country': 'Country',
        }

    self.fields['name'].widget.attrs['autofocus'] = True
