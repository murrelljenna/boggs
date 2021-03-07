from django.test import TestCase, Client
from django.contrib.auth.models import User

class AuthenticationRouteTest(TestCase):
    """ For testing authentication routes and token provisioning """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
    def test_acquire_token_success(self):
        """Supplying correct credentials to token route should return a JWT"""
        token_response = self.client.post('/token-auth/', {'username': self.user.username, 'password': '12345'})

        self.assertEqual(token_response.status_code, 200)
        self.assertIn('access', token_response.data)
        self.assertIn('refresh', token_response.data)

    def test_acquire_token_fail(self):
        token_response = self.client.post('/token-auth/', {'username': self.user.username, 'password': 'invalid_password'})

        self.assertEqual(token_response.status_code, 401)
       

    def test_validate_token(self):
        token_response = self.client.post('/token-auth/', {'username': self.user.username, 'password': '12345'})
        response = self.client.get('/contacts/', HTTP_AUTHORIZATION=f"Bearer {token_response.data['access']}")
        self.assertEqual(response.status_code, 200)
