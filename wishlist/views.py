from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import Http404

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
        wishlist = get_object_or_404(Wishlist, user=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, f'{product.name} is already in your \
            wishlist!')

    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} successfully added \
            to your wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_wishlist_item(request, item_id):
    """
    A view to delete a wishlist product
    """
    product = get_object_or_404(Product, pk=item_id)
    wishlist = get_object_or_404(Wishlist, user=request.user.id)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f'{product.name} successfully removed \
            from your wishlist!')
    else:
        messages.error(request, f'{product.name} is not in your wishlist!')

    if redirect_from == 'wishlist':
        redirect_url = reverse('wishlist')
    else:
        redirect_url = reverse('product_detail', args=[product.id])

    return redirect(redirect_url)

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
