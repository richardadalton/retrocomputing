from django.conf.urls import url, include
from .views import all_products, product_item

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^(\d+)$', product_item, name='product_item'),
]