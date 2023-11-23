from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm


def company_info(request):
    """
    View to display the template for
    company information
    """
    return render(request, 'company_info/company_info.html')


def company_faq(request):
    """
    View to display the template for
    company FAQs
    """
    return render(request, 'company_info/company_faq.html')


def company_contact(request):
    """
    View to display the template for
    company contact form and send a
    confirmation email
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            sender = settings.DEFAULT_FROM_EMAIL
            recipient = request.POST.get('email')
            email_subject = 'Thanks for your question!'
            email_message = 'We will get back to you as quickly as possibly! \
                Best regards, \
                    Knits&Knots'
            send_mail(email_subject, email_message, sender, [recipient])
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'There was an error with your message. \
                Please double check your information.')
    form = ContactForm()
    context = {
        'form': form
        }
    return render (request, 'contact/company_contact.html', context)
