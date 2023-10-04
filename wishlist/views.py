from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings

from products.models import Product
from .models import Wishlist


@login_required
def wishlist_view(request):
    """
    View to display user's wishlist
    """
    wishlist_item_count = 0

    try:
        all_wishlist_items = Wishlist.objects.filter(user=request.user.id)[0]
    except IndexError:
        wishlist_item = None
    else:
        wishlist_item = all_wishlist_items.products.all()
        wishlist_item_count = all_wishlist_items.products.all().count()

    if not wishlist_item:
        messages.info(request, 'Your wishlist is empty!')

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_item': wishlist_item,
        'wishlist_item_count': wishlist_item_count
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):
    """View to add a product to favourites"""

    product = get_object_or_404(Product, pk=item_id)
    try:
        wishlist_item = get_object_or_404(Wishlist, user=request.user.id)
    except Http404:
        wishlist_item = Wishlist.objects.create(user=request.user)

    if product in wishlist_item.products.all():
        messages.info(request, 'The product is already in your wishlist!')
        messages.info(request, f'{product.name} is already in your \
            wishlist!')

    else:
        wishlist_item.products.add(product)
        messages.success(request, f'{product.name} successfully added \
            to your wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))
