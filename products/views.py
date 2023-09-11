from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categories(request):
    """
    View to make categories available for customers
    to browse through
    """
    return {
        'categories': Category.objects.all()
    }


def product_all(request):
    """
    View to display all the products for
    the customer
    """
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def product_detail(request, slug):
    """
    View to click on a specific product and
    get a detailed page for it
    """
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})