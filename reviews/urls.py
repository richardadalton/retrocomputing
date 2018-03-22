from django.conf.urls import url, include
from .views import add_a_review

urlpatterns = [
    url(r'^add/$', add_a_review, name='add_a_review'),
]