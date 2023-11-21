from django.shortcuts import render

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
    return render (request, 'contact/company_contact.html')
