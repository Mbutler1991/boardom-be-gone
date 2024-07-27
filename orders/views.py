from django.shortcuts import render
from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.models import Basket
from django.http import JsonResponse, HttpResponseBadRequest
import stripe
from django.conf import settings

def order(request):
    try:
        basket = Basket.objects.get(user=request.user)
        basket_items = basket.items.all()  
        grand_total_price = basket.total_price() 
        if request.method == 'POST':
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                order = order_form.save()
                for item in basket_items:
                    order_line_item = OrderLineItem(
                        order=order,
                        product=item.product,
                        quantity=item.quantity
                    )
                    order_line_item.save()
                return render(request, 'orders/order_complete.html')
        else:
            order_form = OrderForm()
        return render(request, 'orders/order.html', {'order_form': order_form, 'basket_items': basket_items, 'grand_total_price': grand_total_price})
    except Basket.DoesNotExist:
        return HttpResponseBadRequest('Basket does not exist')

