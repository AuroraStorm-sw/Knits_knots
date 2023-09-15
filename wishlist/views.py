from django.shortcuts import render


def wishlist(request):
    """
    A view to return the wishlist
    for authorized users
    """

    return render(request, 'wishlist/wishlist.html')
