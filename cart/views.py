from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_cart(request):
    
    cart_items = [
        {
            'image': '/media/images/spectrum128K.png',
            'name': 'Spectrum 128K',
            'quantity': '1',
            'price': '100',
            'total': '100',
        },
        {
            'image': '/media/images/sinclair_ql.png',
            'name': 'Sinclair QL',
            'quantity': '1',
            'price': '50',
            'total': '50',
        },
    ]
    args = {'cart_items': cart_items, 'total': 999 }
    
    return render(request, "cart/view_cart.html", args)
    

def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('home')
