from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
import stripe
from django.contrib import messages
from cart.utils import get_cart_items_and_total
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)    
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            # Save The Order
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            # Save the Order Line Items
            cart = request.session.get('cart', {})
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()
        
        
            # Charge the Card
            items_and_total = get_cart_items_and_total(cart)
            total = items_and_total['total']
            total_in_cent = int(total*100)
            try:
                customer = stripe.Charge.create(
                    amount=total_in_cent,
                    currency="EUR",
                    description="Dummy Transaction",
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")


            if customer.paid:
                messages.error(request, "You have successfully paid")

                # Send Email
                context = {
                    'site_name': "Blah Blah dot com",
                    'user': request.user,
                }
                context.update(items_and_total)
                message = render_to_string('checkout/text_confirmation_email.html', context)
                html_message = render_to_string('checkout/html_confirmation_email.html', context)
                
                subject = 'Thanks for buying our stuff!'
                message = message
                from_email = settings.SYSTEM_EMAIL
                to_email = [request.user.email]
    
                send_mail(subject,message,from_email,to_email,fail_silently=True,html_message=html_message)
        
                #Clear the Cart
                del request.session['cart']
                return redirect("home")
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE }
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items_and_total(cart)
        context.update(cart_items_and_total)
    
    return render(request, "checkout/checkout.html", context)