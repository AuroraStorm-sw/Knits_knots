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

    context = {
        'products': products,
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
