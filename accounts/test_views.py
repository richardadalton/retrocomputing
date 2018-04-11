from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from .views import login

# Create your tests here.
class TestAccountsViews(TestCase):
    def test_GET_login_ok(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        
    def test_GET_login_resolves_to_login_form(self):
        found = resolve('/accounts/login/')  
        self.assertEqual(found.func, login)  
        
    def test_POST_can_log_in(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/", {'username_or_email': 'user', 'password': 'password'})
        self.assertIn('_auth_user_id', self.client.session)
        self.assertRedirects(response, "/", status_code=302, target_status_code=200)

    def test_POST_cannot_log_in_with_email(self):
        self.user = User.objects.create_user(username='user', password='password', email="user@example.com")
        response = self.client.post("/accounts/login/", {'username_or_email': 'user@example.com', 'password': 'password'})
        self.assertIn('_auth_user_id', self.client.session)
        self.assertRedirects(response, "/", status_code=302, target_status_code=200)

    def test_POST_cannot_log_in_wrong_password(self):
        self.user = User.objects.create_user(username='user', password='password', email="user@example.com")
        response = self.client.post("/accounts/login/", {'username_or_email': 'user@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)

    def test_POST_can_redirect_after_login(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/?next=/accounts/profile/", {'username_or_email': 'user', 'password': 'password'})
        self.assertRedirects(response, "/accounts/profile/", status_code=302, target_status_code=200)
    
    def test_profile_requires_login(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/?next=/accounts/profile/", {'username_or_email': 'user', 'password': 'password'})
        self.assertRedirects(response, "/accounts/profile/", status_code=302, target_status_code=200)
        
        
    def test_can_logout(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/", {'username_or_email': 'user', 'password': 'password'})
        self.assertIn('_auth_user_id', self.client.session)
        response = self.client.get("/accounts/logout/")
        self.assertNotIn('_auth_user_id', self.client.session)
        
    def test_GET_register_seller(self):
        response = self.client.get("/accounts/register/seller")
        self.assertEqual(response.status_code, 200)

    def test_POST_register_seller(self):
        details = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post("/accounts/register/seller", details)
        self.assertRedirects(response, "/", status_code=302, target_status_code=200)

    def test_POST_redirect_after_register_seller(self):
        details = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post("/accounts/register/seller?next=/accounts/profile/", details)
        self.assertRedirects(response, "/accounts/profile/", status_code=302, target_status_code=200)


    def test_GET_register_buyer(self):
        response = self.client.get("/accounts/register/buyer")
        self.assertEqual(response.status_code, 200)

    def test_POST_register_buyer(self):
        details = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password',
            'city': 'city',
        }
        response = self.client.post("/accounts/register/buyer", details)
        self.assertRedirects(response, "/", status_code=302, target_status_code=200)

    def test_POST_redirect_after_register_buyer(self):
        details = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password',
            'city': 'city',
        }
        response = self.client.post("/accounts/register/buyer?next=/accounts/profile/", details)
        self.assertRedirects(response, "/accounts/profile/", status_code=302, target_status_code=200)
