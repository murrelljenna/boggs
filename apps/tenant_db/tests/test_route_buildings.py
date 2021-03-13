from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.models import Building
from apps.tenant_db.tests import TestUtils

class BuildingsRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = TestUtils.getAuthorizedClient(username, password)

    def test_get_buildings_count(self):
        Building.objects.create(
            street_number = "Electric",
            street_name = "Avenue",
            postal_code = "atwtih",
        )
        response = self.client.get('/buildings/')
        self.assertEqual(len(response.data), 1)
