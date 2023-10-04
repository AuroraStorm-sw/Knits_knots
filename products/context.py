from .models import Category, Tag


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def tags(request):
    """
    View to make categories available for customers
    to browse through
    """
    return {
        'tags': Tag.objects.all()
    }
