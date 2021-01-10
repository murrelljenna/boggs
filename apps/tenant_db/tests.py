from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.

class AuthenticationTest(TestCase):
    """ For testing authentication routes and token provisioning """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token_response = self.client.post('/token-auth/', {'username': self.user.username, 'password': '12345'})
        pass

    def test_acquire_token(self):
        """Supplying correct credentials to token route should return a JWT"""
        self.assertEqual(self.token_response.status_code, 200)
        self.assertIn('access', self.token_response.data)
        self.assertIn('refresh', self.token_response.data)
        pass

    def test_validate_token(self):
        response = self.client.get('/contacts/', HTTP_AUTHORIZATION=f"Bearer {self.token_response.data['access']}")
        self.assertEqual(response.status_code, 200)
        pass
