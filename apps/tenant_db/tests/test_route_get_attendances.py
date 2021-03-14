from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.models import Attendance, CallResult, Event, Contact
from apps.tenant_db.tests import TestUtils, fake_models

class AttendanceGetRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = TestUtils.getAuthorizedClient(username, password)

    @classmethod
    def setUpTestData(cls):
        cls.attendance = fake_models.attendances[0]
        cls.attendance.event.save()
        cls.attendance.contact.save()
        cls.attendance.save()

    def test_get_attendance_count(self):
        response = self.client.get('/attendances/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_attendance(self):
        response = self.client.get('/attendances/')
        self.assertEqual(response.status_code, 200)

        response_attendance = response.json()[0]
        response_attendance.pop('id')

        expected_attendance = {
            'event': 1,
            'contact': 1, 
            'result': CallResult.NO
        }
        
        self.assertEqual(response_attendance, expected_attendance)

    def test_get_attendance_by_id(self):
        response = self.client.get(f"/attendances/{self.attendance.id}/")
        self.assertEqual(response.status_code, 200)
        response_attendance = response.json()
        response_attendance.pop('id')

        expected_attendance = {
            'event': self.attendance.event.id,
            'contact': self.attendance.contact.id,
            'result': self.attendance.result.value
        }
        
        self.assertEqual(response_attendance, expected_attendance)

    def test_get_attendance_by_event_id(self):
        response = self.client.get(f"/attendances/?event={self.attendance.event.id}")
        self.assertEqual(response.status_code, 200)

        response_attendance = response.json()[0]
        response_attendance.pop('id')

        expected_attendance = {
            'event': self.attendance.event.id,
            'contact': self.attendance.contact.id,
            'result': self.attendance.result.value
        }
        
        self.assertEqual(response_attendance, expected_attendance)
