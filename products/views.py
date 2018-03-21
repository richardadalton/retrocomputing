from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/product-list.html", {'products': products})    
    
def product_item(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product-item.html", {'product': product})    
