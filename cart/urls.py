from django.conf.urls import url, include
from .views import add_to_cart

urlpatterns = [
    url(r'^add/$', add_to_cart, name='add_to_cart'),
]