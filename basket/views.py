from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse


def basket(request):
    """
    A view to show the basket page for
    the customer
    """
    return render(request, 'basket/basket.html')


# def basket_add(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         product = get_object_or_404(Product, id=product_id)
#         basket.add(product=product, qty=product_qty)

#         basketqty = basket.__len__()
#         response = JsonResponse({'qty': basketqty})
#         return response


def add_to_basket(request, item_id):
    """
    A view to add a quantity of products to
    the shopping basket
    """

    quantity = str(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(bag.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
