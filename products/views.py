from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm


def product_all(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('product'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,

    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to click on a specific product and
    get a detailed page for it
    """
 
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def categories(request):
    """
    View to make categories available for customers
    to browse through
    """
    return {
        'categories': Category.objects.all()
    }


def category_list(request, category_slug):
    """
    View to display all the categories
    and each corresponding product
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category.html',
                  {'category': category, 'products': products})


def admin_add_product(request):
    """
    View for the admin to add new products
    to the webshop
    """
    form = ProductForm()

    return render(request, 'products/admin_add_product.html', {'form': form})
