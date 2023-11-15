from django.shortcuts import render

def company_info(request):
    """
    View to display the template for
    company information
    """
    return render (request, 'company/company_info.html')
