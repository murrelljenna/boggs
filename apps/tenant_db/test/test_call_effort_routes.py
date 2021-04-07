from django.contrib.auth.models import User
from apps.tenant_db.models import Contact
from apps.tenant_db.test import TestUtils, strategies

from hypothesis import given, settings
import random
from hypothesis.extra.django import TestCase, from_model

class CallEffortRouteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'testuser'
        password = '12345'
        cls.user = User.objects.create_user(username=username, password=password)
        cls.authorized_client = TestUtils.getAuthorizedClient(username, password)
    
    @given(strategies.contacts)
    @settings(max_examples=strategies.max_examples)
    def test_create_call_effort_all_contacts(self, contacts):
        response = self.authorized_client.post(
            f"/efforts/calls/",
            content_type='application/json',
            data={'name': 'waddap'}
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json()), len(contacts))

    @given(strategies.contacts)
    @settings(max_examples=strategies.max_examples)
    def test_create_call_effort_filters_building(self, contacts):
        buildingId = random.choice(contacts).address.id
        response = self.authorized_client.post(
            f"/efforts/calls/?address={buildingId}",
            content_type='application/json',
            data={'name': 'waddap'}
        )
        
        self.assertEqual(response.status_code, 201)
        for activity in response.json():
            contact = Contact.objects.get(id=activity['contact'])
            self.assertEqual(contact.address.id, buildingId)
