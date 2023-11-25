from django.shortcuts import render


def handler404(request, exception):
    """
    A view for an error page if the user
    tries to visit an unexisting page
    """
    return render(request, "errors/404.html", status=404)


def handler500(request, exception):
    """
    A view for an error page if the user
    gets an internal error
    """
    return render(request, "errors/500.html", status=500)