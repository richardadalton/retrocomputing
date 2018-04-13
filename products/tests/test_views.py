from django.test import TestCase
from products.models import Product

class TestAccountsViews(TestCase):
    def test_search_products(self):
        product_abc = Product(name="ABC", price="1")
        product_abc.save()
        product_def = Product(name="DEF", price="1")
        product_def.save()
        product_abd = Product(name="ABD", price="1")
        product_abd.save()

        response = self.client.get("/search?query=AB&match=contains")
        products = response.context[-1]['products'].all()
        self.assertEqual(len(products), 2)
        self.assertIn(product_abc, products)
        self.assertIn(product_abd, products)
