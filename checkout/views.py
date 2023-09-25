from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderFormAddress

import stripe


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
        'stripe_public_key': 'pk_test_51NuB5lEXoN90z8qxh1VctlmnA1Sq1qobFGgGLWyrcePkIoZZsoEueAt1u00yX66lz3tCh21thuKAKSZbGEn6gBiq00Giibjwoc',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
