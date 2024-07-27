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
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
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
        return render(request, 'orders/order.html', {'order_form': order_form, 'stripe_public_key': stripe_public_key, 'basket_items': basket_items, 'grand_total_price': grand_total_price})
    except Basket.DoesNotExist:
        return HttpResponseBadRequest('Basket does not exist')

def create_payment_intent(request):
    basket = request.session.get('basket', {})
    if not basket:
        return HttpResponseBadRequest('Basket is empty')
    
    total_amount = calculate_total_amount(basket)

    payment_intent = stripe.PaymentIntent.create(
        amount=total_amount, 
        currency='eur',
        payment_method_types=['card'],
        metadata={'integration_check': 'accept_a_payment'},
    )

    return JsonResponse({'client_secret': payment_intent.client_secret})

def calculate_total_amount(basket):
    total_amount = 0
    for item_id, item_info in basket.items():
        subtotal = item_info['quantity'] * item_info['price']
        total_amount += subtotal
    return total_amount

def process_payment(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payment_method_id = request.POST.get('payment_method_id')
    
    try:
        stripe.PaymentIntent.confirm(
            payment_method_id,
            payment_intent_id=request.session.get('payment_intent_id')
        )
        return JsonResponse({'success': True})
    except stripe.error.CardError as e:
        error_msg = e.error.message
        return JsonResponse({'success': False, 'error_msg': error_msg}, status=400)
    except Exception as e:
        error_msg = str(e)
        return JsonResponse({'success': False, 'error_msg': error_msg}, status=500)