from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderProduct


@receiver(post_save, sender=OrderProduct)
def update_on_save(sender, instance, created, **kwargs):
    """
    Signal to update the total sum when adding
    products
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderProduct)
def update_on_save(sender, instance, **kwargs):
    """
    Signal to update the total sum when deleting
    products
    """
    instance.order.update_total()
