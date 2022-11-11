from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# Use receiver decorator telling it
# we're receiving post_save signals
# from the OrderLineItem model
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create.
    Special type of functioon which handles signals
    from the post_save event.
    Args:
        sender: OrderLineItem
        instance: actual instance of the model that sent it
        created (bool): new item? (or one being updated?)
        **kwargs
    Returns:
        Access instance.order (the order this specific
        line item is related to),
        Call update_total() method on it.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete.
    """
    instance.order.update_total()
