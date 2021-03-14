from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.serializers import AttendanceSerializer
from apps.tenant_db.models import Attendance, CallResult, Event, Contact
from apps.tenant_db.tests import TestUtils, fake_models

class AttendancePostRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = TestUtils.getAuthorizedClient(username, password)

    def test_post_attendance_count(self):
        attendance = fake_models.attendances[0]
        attendance.event.save()
        attendance.contact.save()
        serializer = AttendanceSerializer(attendance)

        response = self.client.post('/attendances/', serializer.data)
        self.assertEqual(response.status_code, 201) 
        self.assertEqual(len(Attendance.objects.all()), 1)

    def test_post_attendance(self):
        attendance = fake_models.attendances[0]
        attendance.event.save()
        attendance.contact.save()
        serializer = AttendanceSerializer(attendance)

        response = self.client.post('/attendances/', serializer.data)
        self.assertEqual(response.status_code, 201) 

        expected_attendance = serializer.data
        created_attendance = response.data

        expected_attendance.pop('id')
        created_attendance.pop('id')

        self.assertEqual(expected_attendance, created_attendance)
