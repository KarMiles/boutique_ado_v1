from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        models = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # List comprehension - for loop to add items to a list
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
