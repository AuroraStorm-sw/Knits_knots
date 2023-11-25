from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """ Form to contact the company """
    class Meta:
        model = Contact
        fields = '__all__'
