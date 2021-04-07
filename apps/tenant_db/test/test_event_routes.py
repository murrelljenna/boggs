from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.tenant_db.serializers import EventSerializer
from apps.tenant_db.models import Event
from apps.tenant_db.test import TestUtils

class EventsRouteTest(TestCase):
    def setUp(self):
        username = 'testuser'
        password = '12345'
        self.user = User.objects.create_user(username=username, password=password)
        self.client = TestUtils.getAuthorizedClient(username, password)

    def test_get_events_count(self):
        event = Event.objects.create(
            name = "British Ale",
        )
        response = self.client.get('/events/')
        self.assertEqual(len(response.data), 1)

    def test_get_events(self):
        Event.objects.create(
            name = "Catan Party",
            location = "My pad",
            description = "byob"
        )

        response = self.client.get('/events/')

        response_event = response.json()[0]
        response_event.pop('id')

        expected_event = {
            'name': 'Catan Party',
            'location': "My pad", 
            'description': "byob"
        }
        
        self.assertEqual(response_event, expected_event)

    def test_get_event_by_id(self):
        Event.objects.create(
            id = 1,
            name = "Catan Party",
            location = "My pad",
            description = "byob"
        )

        response = self.client.get('/events/1/')
        response_event = response.json()
        response_event.pop('id')
        expected_event = {
            'name': 'Catan Party',
            'location': "My pad",
            'description': "byob"
        }
        
        self.assertEqual(response_event, expected_event)
