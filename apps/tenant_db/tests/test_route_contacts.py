from django.test import TestCase, Client
from django.contrib.auth.models import User

class ContactsRouteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
