from django.contrib.auth.models import User
from hypothesis import given, settings
from hypothesis.extra.django import TestCase

from apps.tenant_db.test import TestUtils, strategies


class ContactsGetRouteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'testuser'
        password = '12345'
        cls.user = User.objects.create_user(username=username, password=password)
        cls.authorized_client = TestUtils.getAuthorizedClient(username, password)

    @given(strategies.contacts)
    @settings(max_examples=strategies.max_examples)
    def test_get_contacts_count(self, contacts):
        response = self.authorized_client.get('/contacts/')
        self.assertEqual(len(response.data), len(contacts))
