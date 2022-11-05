from django import template


# In bag.html and checkout.html add:
# {% load bag_tools %}
# {{ item.product.price | calc_subtotal:item.quantity }}

# More info:
# Creating custom tags and filters
# https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
