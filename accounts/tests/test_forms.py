from django.test import TestCase
from django.urls import resolve
from accounts.forms import UserLoginForm
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


    def test_forms_register_with_duplicate_email(self):
        self.user = User.objects.create_user(username='user', password='password', email="user@example.com")
        details = {
            'username': 'a_different_user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post("/accounts/register/seller", details)
        self.assertFormError(response, 'form', 'email', 'Email addresses must be unique.')

    def test_forms_register_with_different_passwords(self):
        details = {
            'username': 'a_different_user',
            'email': 'user@example.com',
            'password1': 'password1',
            'password2': 'password2'
        }
        response = self.client.post("/accounts/register/seller", details)
        self.assertFormError(response, 'form', 'password2', 'Passwords do not match')

    def test_forms_register_with_empty_password(self):
        details = {
            'username': 'a_different_user',
            'email': 'user@example.com',
            'password1': '',
            'password2': ''
        }
        response = self.client.post("/accounts/register/seller", details)
        self.assertFormError(response, 'form', 'password1', 'This field is required.')
        self.assertFormError(response, 'form', 'password2', 'This field is required.')
