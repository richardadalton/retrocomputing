from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_cart(request):
    return render(request, "cart/view_cart.html")
    

def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('home')
