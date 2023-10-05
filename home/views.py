from django.shortcuts import render


def home(request):
    """
    A view to return the home page
    """

    return render(request, 'home/index.html')


def error_404_page(request, exception):
    """ 
    A view for an error page if the user
    tries to visit an unexisting page
    """
    return render(request, "errors/404.html", status=404)