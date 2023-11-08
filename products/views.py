from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category, Tag, Videocall
from .forms import ProductForm, VideocallForm


def product_all(request):
    """
    A view to show all products,
    including sorting and search queries
    """

    p = Paginator(Product.objects.all(), 9)
    page = request.GET.get('page')
    products = p.get_page(page)
    categories = Category.objects.all()

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

    # p = Paginator(Product.objects.all(), 12)
    # page = request.GET.get('page')
    # products = p.get_page(page)
    # categories = Category.objects.all()
    # context = {
    #         'products': products,
    #         'categories': categories,
    #     }
    # query = request.POST.get('search_query')

    # if 'search_query' in request.GET:
    #         query = request.GET.get('search_query')
    #         if query == '' or query == 'All Categories':
    #             p = Paginator(Product.objects.all(), 12)
    #             page = request.GET.get('page')
    #             products = p.get_page(page)
    #             context = {
    #                 'products': products,
    #                 'categories': categories,
    #             }
    #             return render(
    #                 request,
    #                 'products/products.html',
    #                 context
    #             )
    #         else:
    #             products = Product.objects.filter(
    #                 Q(name__icontains=query) |
    #                 Q(description__icontains=query) |
    #                 Q(category__name__icontains=query) |
    #                 Q(brand__name__icontains=query) |
    #                 Q(tags__name__icontains=query)
    #             ).distinct()
    #             p = Paginator(products, 12)
    #             page = request.GET.get('page')
    #             products = p.get_page(page)
    #             context = {
    #                 'products': products,
    #                 'categories': categories,
    #                 'search_term': query,
    #             }
    #             return render(request, 'products/products.html', context)
    # return render(request, 'products/products.html', context)



def product_detail(request, product_id):
    """
    View to click on a specific product and
    get a detailed page for it
    """

    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})


def categories(request):
    """
    View to make categories available for customers
    to browse through
    """
    return {
        'categories': Category.objects.all()
    }


def videocall(request):
    """
    View for customers to order a
    videocall
    """
    if request.method == 'POST':
        video_form = VideocallForm(request.POST, request.FILES)
        if video_form.is_valid():
            videocall = video_form.save()
            messages.success(request, 'Successfully booked videocall!')
        else:
            messages.error(request, 'Failed to book videocall!'
                           'Please ensure the form is valid.')
    else:
        video_form = VideocallForm()

    template = 'products/videocall.html'
    
    context = {
        'video_form': video_form,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """
    View to add a new product to
    the store for the store manager
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, this is a superuser only function!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View to edit an existing product
    for store manager
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, this is a superuser only function!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    View to delete a product for store manager
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops, this is a superuser only function!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, f'{product.name} has been deleted!')
        return redirect(reverse('product'))

    return render(request, 'products/delete_product.html')
