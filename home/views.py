from django.shortcuts import render
from products.models import Product
import random

def home_view(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    random_products = products[:5]
    return render(request, 'home/home.html', {'random_products': random_products})