from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def view_cart(request):
    
    cart = request.session.get('cart', {})

    cart_items = []
    for item_id, item_quantity in cart.items():
        this_product = get_object_or_404(Product, pk=item_id)
        this_item = {
            'image': this_product.image,
            'name': this_product.name,
            'quantity': item_quantity,
            'price': this_product.price,
            'total': 0,
        }
        cart_items.append(this_item)
    
    args = {'cart_items': cart_items, 'total': 999 }
    
    return render(request, "cart/view_cart.html", args)
    

def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('home')
