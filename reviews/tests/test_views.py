from django.test import TestCase
from reviews.forms import ReviewForm
from django.contrib.auth.models import User
from products.models import Product
from reviews.models import Review

# Create your tests here.
class TestReviewViews(TestCase):
    def test_POST_create_review(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.client.login(username='user', password='password')
        
        product = Product(price = 1)
        product.save()
        
        response = self.client.post("/reviews/add/", {'product': 1,'content': 'content', 'rating': '5'})
        self.assertRedirects(response, "/products/1", status_code=302, target_status_code=200)

    def test_POST_can_not_create_review_if_not_logged_in(self):
        product = Product(price = 1)
        product.save()
        
        response = self.client.post("/reviews/add/", {'product': 1,'content': 'content', 'rating': '5'})
        self.assertEqual(response.status_code, 403)

    def test_review_string_representation(self):
        review = Review(content="This is a review", rating=4)
        self.assertEqual(str(review), "This is a review (4)")

