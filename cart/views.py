from django.shortcuts import render, HttpResponse, get_object_or_404
from products.models import Product

# Create your views here.
def add_to_cart(request):
    id = request.POST['id']
    quantity = request.POST['quantity']
    product = get_object_or_404(Product, pk=id)
    return HttpResponse("You want to add {0} of {1}".format(quantity, product.name))