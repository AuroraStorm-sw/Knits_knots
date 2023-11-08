from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


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

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    color = None

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated quantity')
    else:
        basket[item_id] = quantity
        messages.success(request,
                         f'Successfully added {product.name} to the basket!')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """
    A view to update a quantity of products in
    the shopping basket
    """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    color = None

    if 'product_color' in request.POST:
        color = request.POST['product_color']
    basket = request.session.get('basket', {})

    if color:
        if quantity > 0:
            basket[item_id]['items_by_color'][color] = quantity
        else:
            del basket[item_id]['items_by_color'][color]
            if not basket[item_id]['items_by_color']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    messages.success(request, f'Successfully updated basket!')

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def delete_from_basket(request, item_id):
    """
    A view to update a quantity of products in
    the shopping basket
    """

    product = get_object_or_404(Product, pk=item_id)

    try:
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        basket = request.session.get('basket', {})

        if color:
            del basket[item_id]['items_by_color'][color]
            if not basket[item_id]['items_by_color']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)
        messages.success(request, f'Successfully deleted item!')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request,
                       f'An error occurred when removing the item: {e}')
        return HttpResponse(status=500)
