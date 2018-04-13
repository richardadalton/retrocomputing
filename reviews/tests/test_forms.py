from django.test import TestCase
from reviews.forms import ReviewForm

# Create your tests here.
class TestReviewForms(TestCase):
    def test_form_review_ok(self):
        form = ReviewForm({'content': "content", "rating": "5"})
        self.assertTrue(form.is_valid())
