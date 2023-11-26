from django.forms import CharField, TextInput
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Form for user to fill out their details """
    default_phone_number = CharField(
        widget=TextInput(attrs={'type': 'number', }))

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email_adress': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County/State/Locality',
        }

        # Add aria label to form fields
        self.fields['default_full_name'].widget.attrs.update({
            'aria-label': 'Full Name'
        })
        self.fields['default_email_adress'].widget.attrs.update({
            'aria-label': 'Email Address'
        })
        self.fields['default_phone_number'].widget.attrs.update({
            'aria-label': 'Phone number'
        })
        self.fields['default_postcode'].widget.attrs.update({
            'aria-label': 'Postal Code'
        })
        self.fields['default_town_or_city'].widget.attrs.update({
            'aria-label': 'Town or City'
        })
        self.fields['default_street_address1'].widget.attrs.update({
            'aria-label': 'Street Address 1'
        })
        self.fields['default_street_address2'].widget.attrs.update({
            'aria-label': 'Street Address 2'
        })
        self.fields['default_county'].widget.attrs.update({
            'aria-label': 'County/State/Locality'
        })

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # If-statement to ignore country field as it throws an HTML error
            # for placeholders on select fields
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
