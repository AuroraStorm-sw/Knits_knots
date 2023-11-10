from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category, Tag, Videocall
from .forms import ProductForm, VideocallForm


def tags(request):
    """
    View to make tags available for customers
    to browse through
    """
    return {
        'tags': Tag.objects.all()
    }


def category(request):
    """
    View to make categories available for customers
    to browse through
    """
    return {
        'categories': Category.objects.all()
    }



def product_all(request):
    """
    A view to show all products,
    including sorting and search queries
    """

    products = Product.objects.all()
    categories = None
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                product = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'categories': categories,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to click on a specific product and
    get a detailed page for it
    """

    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})


def videocall(request):
    """
    View for customers to book a
    videocall
    """
    if request.method == 'POST':
        form = VideocallForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your booking is complete!')
            return redirect('/products/videocall_success')

        else:
            form = VideocallForm()
            messages.warning(request, 'Booking failed! Please try again.')

    else:
        form = VideocallForm()
        if 'submitted' in request.GET:
            form = VideocallForm()

    form = VideocallForm()
    template = 'products/videocall.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def videocall_success(request):
    """
    Handle successful videocall orders
    """

    messages.success(request, f'Call successfully booked! \
        A confirmation email will be sent to.')

    template = 'products/videocall_success.html'

    return render(request, template, )



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
