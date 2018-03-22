from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_items = []
    total = 0
    for item_id, item_quantity in cart.items():
        this_product = get_object_or_404(Product, pk=item_id)
        this_total = this_product.price * Decimal(item_quantity)
        total += this_total
        this_item = {
            'product_id': item_id, 
            'image': this_product.image,
            'name': this_product.name,
            'quantity': item_quantity,
            'price': this_product.price,
            'total': this_total,
        }
        cart_items.append(this_item)

    return { 'cart_items': cart_items, 'total': total }
    