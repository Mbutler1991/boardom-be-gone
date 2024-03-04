from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SavedForLater
from products.models import Product
from django.contrib.auth.models import User

@login_required
def save_for_later(request, product_id):
    if request.method == 'POST' or request.method == 'GET':
        product = Product.objects.get(pk=product_id)
        SavedForLater.objects.create(user=request.user, product=product)
        return redirect('saved_for_later')
    else:
        return redirect('home')

@login_required
def saved_for_later(request):
    saved_items = SavedForLater.objects.filter(user=request.user)
    return render(request, 'saved/saved.html', {'saved_items': saved_items})

@login_required
def remove_from_saved(request, saved_id):
    saved_item = SavedForLater.objects.get(pk=saved_id)
    saved_item.delete()
    return redirect('saved_for_later')
