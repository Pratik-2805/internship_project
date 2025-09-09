from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User

class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_and_token(self):
        resp = self.client.post('/api/auth/register/', {'email':'a@a.com','name':'A','password':'strongpass123'}, format='json')
        self.assertEqual(resp.status_code, 201)
        resp2 = self.client.post('/api/auth/token/', {'email':'a@a.com','password':'strongpass123'}, format='json')
        self.assertEqual(resp2.status_code, 200)
        self.assertIn('access', resp2.data)
