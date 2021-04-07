import random

from django.contrib.auth.models import User

from hypothesis import given, settings
from hypothesis.extra.django import TestCase

from apps.tenant_db.test import TestUtils, strategies

class BuildingsGetRouteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'testuser'
        password = '12345'
        cls.user = User.objects.create_user(username=username, password=password)
        cls.authorized_client = TestUtils.getAuthorizedClient(username, password)

    @given(strategies.buildings)
    @settings(max_examples=5)
    def test_get_buildings_count(self, buildings):
        response = self.authorized_client.get('/buildings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(buildings))

    @given(strategies.buildings)
    @settings(max_examples=5)
    def test_get_building_by_id(self, buildings):
        building = random.choice(buildings)
        response = self.authorized_client.get(f"/buildings/{building.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(building.id, response.json()['id'])
