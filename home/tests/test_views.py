from django.test import TestCase
from django.urls import resolve
from products.views import all_products

# Create your tests here.
class TestHomePage(TestCase):
    def test_root_url_returns_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, all_products)  