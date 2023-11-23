from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm

def company_info(request):
    """
    View to display the template for
    company information
    """
    return render (request, 'company_info/company_info.html')


def company_faq(request):
    """
    View to display the template for
    company FAQs
    """
    return render (request, 'company_info/company_faq.html')


def company_contact(request):
    """
    View to display the template for
    company contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'There was an error with your message. \
                Please double check your information.')
    form = ContactForm()
    context = {
        'form': form
        }
    return render (request, 'contact/company_contact.html', context)
