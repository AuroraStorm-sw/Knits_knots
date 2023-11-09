from .models import Tag


def tags(request):
    """
    View to make tags available for customers
    to browse through
    """
    return {
        'tags': Tag.objects.all()
    }
