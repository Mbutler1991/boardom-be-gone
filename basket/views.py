from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Basket, BasketItem
from products.models import Product

@login_required
def add_to_basket(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        user_basket, created = Basket.objects.get_or_create(user=request.user)
        basket_item, created = BasketItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            basket_item.quantity += 1
            basket_item.save()
        user_basket.items.add(basket_item)
        return redirect('product_detail', product_id=product_id)
    else:
        return redirect('product_detail', product_id=product_id)

@login_required
def view_basket(request):
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket_count = basket.items.count()
    return render(request, 'basket/basket.html', {'basket': basket, 'basket_count': basket_count})

@login_required
def remove_from_basket(request, basketitem_id):
    basket_item = get_object_or_404(BasketItem, pk=basketitem_id)
    basket_item.delete()
    return redirect('view_basket')