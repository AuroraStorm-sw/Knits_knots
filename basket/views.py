from django.shortcuts import render, redirect, reverse, HttpResponse


def basket(request):
    """
    A view to show the basket page for
    the customer
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    A view to add a quantity of products to
    the shopping basket
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
