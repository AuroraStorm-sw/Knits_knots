from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):

    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})
