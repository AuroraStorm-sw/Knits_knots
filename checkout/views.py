from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderFormAddress
from products.models import Product
from order.models import Order, OrderProduct, ShippingAdress
from basket.context import basket_contents

import stripe
import json


def checkout(request):
    """ A view to return the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'name': request.POST['name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'address': request.POST['address'],
            'city': request.POST['city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderFormAddress(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            # pid = request.POST.get('client_secret').split('_secret')[0]
            # order.stripe_pid = pid
            # order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_product = OrderProduct(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_product.save()
                    else:
                        for color, quantity in item_data['items_by_size'].items():
                            order_product = OrderProduct(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_color=color,
                            )
                            order_product.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our \
                             database. Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderFormAddress()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
             did you forget to set it?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    message.success(request, f'Order successfully processed, \
        Your order number is {order_number}. A confirmation \
            email will be sent to {order.email} ')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
