from django.conf.urls import url, include
from . import urls_reset
from .views import register_buyer, register_seller, profile, logout, login

urlpatterns = [
    url(r'^register/buyer$', register_buyer, name='register_buyer'),
    url(r'^register/seller$', register_seller, name='register_seller'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]