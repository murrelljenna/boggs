from django.test import Client
from django.contrib.auth.models import User
from django.test.utils import override_settings
from apps.tenant_db.models import Attendance, CallResult, Event, Contact
from apps.tenant_db.tests import TestUtils

from hypothesis import given, settings
import hypothesis.strategies as st
import random
from hypothesis.extra.django import TestCase, from_model

class AttendanceGetRouteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        username = 'testuser'
        password = '12345'
        cls.user = User.objects.create_user(username=username, password=password)
        cls.authorized_client = TestUtils.getAuthorizedClient(username, password)

    @given(st.lists(from_model(Attendance, event=from_model(Event), contact=from_model(Contact, phone_number=st.text(max_size=10)))))
    @settings(max_examples=5)
    def test_get_attendance_count(self, attendances):
        response = self.authorized_client.get('/attendances')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(attendances))

    @given(st.lists(from_model(Attendance, event=from_model(Event), contact=from_model(Contact, phone_number=st.text(max_size=10))), min_size=1))
    @settings(max_examples=5)
    def test_get_attendance_by_id(self, attendances):
        attendance = random.choice(attendances)
        response = self.authorized_client.get(f"/attendances/{attendance.id}/")
        self.assertEqual(response.status_code, 200)
        response_attendance = response.json()
        response_attendance.pop('id')

        expected_attendance = {
            'event': attendance.event.id,
            'contact': attendance.contact.id,
            'result': attendance.result.value
        }
        
        self.assertEqual(response_attendance, expected_attendance)

    @given(st.lists(from_model(Attendance, event=from_model(Event), contact=from_model(Contact, phone_number=st.text(max_size=10))), min_size=1))
    @settings(max_examples=5)
    def test_get_attendance_by_event_id(self, attendances):
        attendance = random.choice(attendances)
        response = self.authorized_client.get(f"/attendances", {'event': attendance.event.id})
        self.assertEqual(response.status_code, 200)

        response_attendance = response.json()[0]
        self.assertEqual(response_attendance['id'], attendance.id)

    @given(st.integers(min_value=5))
    @settings(max_examples=5)
    def test_get_attendance_by_event_id_fail(self, eventId):
        response = self.authorized_client.get(f"/attendances?event={eventId}")
        self.assertEqual(response.status_code, 400)
