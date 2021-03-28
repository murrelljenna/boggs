from django.test import Client
from django.contrib.auth.models import User
from apps.tenant_db.serializers import AttendanceSerializer
from apps.tenant_db.models import Attendance, CallResult, Event, Contact
from apps.tenant_db.tests import TestUtils, fake_models

from hypothesis import given, settings
import hypothesis.strategies as st
import random
from hypothesis.extra.django import TestCase, from_model

class AttendancePostRouteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'testuser'
        password = '12345'
        cls.user = User.objects.create_user(username=username, password=password)
        cls.authorized_client = TestUtils.getAuthorizedClient(username, password)

    @given(from_model(Attendance, event=from_model(Event), contact=from_model(Contact, phone_number=st.text(min_size=1, max_size=10))))
    def test_post_attendance(self, attendance):
        serialized_attendance = AttendanceSerializer(attendance).data
        serialized_attendance.pop('id')

        response = self.authorized_client.post('/attendances', serialized_attendance)
        self.assertEqual(response.status_code, 201) 

        created_attendance = response.data

        created_attendance.pop('id')

        self.assertEqual(serialized_attendance, created_attendance)
