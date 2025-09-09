from django.test import TestCase
from rest_framework.test import APIClient
from accounts.models import User
from .models import Task

class TasksTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='u@u.com', password='testpass123')
        resp = self.client.post('/api/auth/token/', {'email':'u@u.com','password':'testpass123'}, format='json')
        self.token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_task_and_owner(self):
        resp = self.client.post('/api/tasks/', {'title':'T1','description':'d'}, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        t = Task.objects.first()
        self.assertEqual(t.owner, self.user)
