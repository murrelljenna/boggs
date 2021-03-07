from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.models import Contact

def getAuthorizedClient(username, password):
    token = Client().post('/token-auth/', {'username': username, 'password': password})
    token_header = f"Bearer {token.data['access']}"
    return Client(HTTP_AUTHORIZATION=token_header)

class BuildingsRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = getAuthorizedClient(username, password)

    def test_get_contacts(self):
        Contact.objects.create(
            first_name = "KRS",
            last_name = "-One",
        )
        response = self.client.get('/contacts/')
        self.assertEqual(len(response.data), 1)
