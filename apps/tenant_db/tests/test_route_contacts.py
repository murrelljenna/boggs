from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.models import Contact
from apps.tenant_db.tests import TestUtils

class ContactsRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = TestUtils.getAuthorizedClient(username, password)

    def test_get_contacts_count(self):
        Contact.objects.create(
            first_name = "KRS",
            last_name = "-One",
        )
        response = self.client.get('/contacts/')
        self.assertEqual(len(response.data), 1)
