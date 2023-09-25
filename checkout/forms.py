from django import forms
from order.models import Order, OrderProduct, ShippingAdress


class OrderFormAddress(forms.ModelForm):
    class Meta:
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
            super().__init__(*args, **kwargs)
            placeholders = {
                'name': 'Name',
                'surname': 'Surname',
                'email': 'Email',
                'address': 'Address',
                'city': 'City',
                'postcode': 'Postal code',
                'country': 'Country',
            }

            self.fields['full_name'].widget.attrs['autofocus'] = True

            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
