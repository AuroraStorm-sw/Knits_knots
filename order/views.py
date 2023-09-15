from django.shortcuts import render


def profile(request):
    """
    A view to show the basket page for
    the customer
    """
    return render(request, 'profile/profile.html')
