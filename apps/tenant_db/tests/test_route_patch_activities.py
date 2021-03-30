from django.test import Client
from django.contrib.auth.models import User
from django.test.utils import override_settings
from apps.tenant_db.models import Activity, CallResult, Contact, CallResult
from apps.tenant_db.tests import TestUtils

from hypothesis import given, settings
import hypothesis.strategies as st
import random
from hypothesis.extra.django import TestCase, from_model

class ActivitiesPatchRouteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'testuser'
        password = '12345'
        cls.user = User.objects.create_user(username=username, password=password)
        cls.authorized_client = TestUtils.getAuthorizedClient(username, password)

    @given(st.lists(from_model(Activity, contact=from_model(Contact, phone_number=st.text(max_size=10,alphabet=st.characters(min_codepoint=1)))), min_size=1))
    @settings(max_examples=5)
    def test_patch_activity_status(self, activities):
        activity = random.choice(activities)
        response = self.authorized_client.patch(f"/activities/{activity.id}/", content_type='application/json', data={'status': 'Y'})
        self.assertEqual(response.status_code, 200)
        activity = Activity.objects.get(id=activity.id)
        self.assertEqual(activity.status, CallResult.YES)
