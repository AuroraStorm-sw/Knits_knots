from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Category, Product, Tag

from .models import Category


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


def product_all(request):
    """
    View to display all the products for
    the customer and product search
    """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria found")
                return redirect(reverse('products:product_all'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, slug):
    """
    View to click on a specific product and
    get a detailed page for it
    """
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html',
                  {'product': product})
