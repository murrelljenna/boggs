from django.test import Client
from django.contrib.auth.models import User
from django.test.utils import override_settings
from apps.tenant_db.models import Activity, CallResult, Contact
from apps.tenant_db.tests import TestUtils

from hypothesis import given, settings
import hypothesis.strategies as st
import random
from hypothesis.extra.django import TestCase, from_model

class ActivitiesGetRouteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'testuser'
        password = '12345'
        cls.user = User.objects.create_user(username=username, password=password)
        cls.authorized_client = TestUtils.getAuthorizedClient(username, password)

    @given(st.lists(from_model(Activity, contact=from_model(Contact, phone_number=st.text(max_size=10,alphabet=st.characters(min_codepoint=1))))))
    @settings(max_examples=5)
    def test_get_activity_count(self, activities):
        response = self.authorized_client.get('/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(activities))

    @given(
        st.lists(
            from_model(
                Activity,
                contact=from_model(
                    Contact, 
                    phone_number=st.text(
                        max_size=10,
                        alphabet=st.characters(min_codepoint=1)
                    )
                )
            ), 
        min_size=1)
    )
    @settings(max_examples=5)
    def test_get_activity_by_id(self, activities):
        activity = random.choice(activities)
        response = self.authorized_client.get(f"/activities/{activity.id}/")
        self.assertEqual(response.status_code, 200)
        response_activity = response.json()
        response_activity.pop('id')
        response_activity.pop('created_at')
        response_activity.pop('updated_at')

        expected_activity = {
            'contact': activity.contact.id,
            'code': activity.code.value,
            'status': activity.status.value,
            'notes': activity.notes
        }
        
        self.assertEqual(response_activity, expected_activity)

    @given(st.lists(from_model(Activity, contact=from_model(Contact, phone_number=st.text(max_size=10, alphabet=st.characters(min_codepoint=1)
))), min_size=1))
    @settings(max_examples=5)
    def test_get_activity_by_contact_id(self, activities):
        activity = random.choice(activities)
        response = self.authorized_client.get(f"/activities/", {'contact': activity.contact.id})
        self.assertEqual(response.status_code, 200)

        for response_activity in response.json():
            self.assertEqual(response_activity['contact'], activity.contact.id)

    @given(st.integers(min_value=500))
    @settings(max_examples=5)
    def test_get_activity_by_contact_id_fail(self, contactId):
        response = self.authorized_client.get(f"/activities/", {'contact': contactId})
        self.assertEqual(response.status_code, 400)
