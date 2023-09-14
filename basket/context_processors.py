from .basket import Basket


def basket(request):
    """
    A view to show the basket page for
    the customer across the website
    """
    return render(request, 'basket/basket.html')
