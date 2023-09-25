from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderFormAddress


def checkout(request):
    """ A view to return the checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your shopping basket is empty!')
        return redirect(reverse('product'))

    order_form = OrderFormAddress()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
