

def get_items_in_cart_count(request):
    cart = request.session.get('cart', {})
    
    count = 0
    for id, quantity in cart.items():
        count += quantity
    
    return {'items_in_cart': count}