from django.test import TestCase
from django.urls import resolve
from .forms import UserLoginForm
from django.contrib.auth.models import User

# Create your tests here.
class TestAccountsForms(TestCase):
    def test_form_login_ok(self):
        form = UserLoginForm({'username_or_email': "user", "password": "password"})
        self.assertTrue(form.is_valid())

    def test_forms_required_fields(self):
        response = self.client.post("/accounts/login/", {})
        self.assertFormError(response, 'form', 'username_or_email', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_forms_user_does_not_exist(self):
        response = self.client.post("/accounts/login/", {'username_or_email': 'user', 'password': 'password'})
        self.assertFormError(response, 'form', None, 'Your username or password are incorrect')
