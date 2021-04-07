from django.test import Client

def getAuthorizedClient(username, password):
    token = Client().post('/token-auth/', {'username': username, 'password': password})
    token_header = f"Bearer {token.data['access']}"
    return Client(HTTP_AUTHORIZATION=token_header)
