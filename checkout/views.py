from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()  # instance of the order form, empty for now.
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M0qmvLaatIXVGEFpshiA9EeIoQZZQewfyxRJxRR71nJaUZcBXl7bU0iL2LL8uC0BIz71vWMeb74fQwynqa7c2YB00DClhm0SN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
