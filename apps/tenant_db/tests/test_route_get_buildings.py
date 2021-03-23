from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.models import Building
from apps.tenant_db.tests import TestUtils, fake_models

class BuildingsGetRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = TestUtils.getAuthorizedClient(username, password)

    @classmethod
    def setUpTestData(cls):
        cls.building = fake_models.buildings[0]
        cls.building.save()

    def test_get_buildings_count(self):
        response = self.client.get('/buildings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_buildings(self):
        response = self.client.get('/buildings/')
        self.assertEqual(response.status_code, 200)

        response_building = response.json()[0]
        response_building.pop('id')
        response_building.pop('created_at')
        response_building.pop('updated_at')

        expected_building = {
            'street_number': self.building.street_number,
            'street_name': self.building.street_name,
            'postal_code': self.building.postal_code,
        }

        self.assertEqual(response_building, expected_building)

    def test_get_building_by_id(self):
        response = self.client.get(f"/buildings/{self.building.id}/")
        self.assertEqual(response.status_code, 200)
        response_building = response.json()
        response_building.pop('id')
        response_building.pop('created_at')
        response_building.pop('updated_at')

        expected_building = {
            'street_number': self.building.street_number,
            'street_name': self.building.street_name,
            'postal_code': self.building.postal_code,
        }
        
        self.assertEqual(response_building, expected_building)

