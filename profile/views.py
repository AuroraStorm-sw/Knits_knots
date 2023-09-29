from django.shortcuts import render, get_object_or_404

from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """ A view to return the profile page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated profile!')
        else:
            messages.error(request, 'Update failed, please ensure the form is valid!')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, 'profile/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
