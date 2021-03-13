from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.serializers import EventSerializer
from apps.tenant_db.models import Attendance, CallResult
from apps.tenant_db.tests import TestUtils

class EventsRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = TestUtils.getAuthorizedClient(username, password)

        event = Event.objects.create(
            name = "Catan Party",
            location = "My pad",
            description = "byob"
        )

        contact = Contact.objects.create(
            first_name = "KRS",
            last_name = "-One",
        )

        attendance = Attendance.objects.create(
            event = event,
            contact = contact,
            result = CallResult.NO
        )

    def test_get_attendance_count(self):
        response = self.client.get('/attendances/')
        self.assertEqual(len(response.data), 1)

    def test_get_attendance(self):
        response = self.client.get('/attendances/')

        response_attendance = response.json()[0]
        response_attendance.pop('id')

        expected_attendance = {
            'event': 1,
            'contact': 1, 
            'result': CallResult.NO
        }
        
        self.assertEqual(response_attendance, expected_attendance)

    def test_get_attendance_by_id(self):
        response = self.client.get('/attendances/1/')
        response_attendance = response.json()
        response_attendance.pop('id')

        expected_attendance = {
            'event': 1,
            'contact': 1, 
            'result': CallResult.NO
        }
        
        self.assertEqual(response_attendance, expected_attendance)
