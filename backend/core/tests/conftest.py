import pytest


@pytest.fixture()
def logged_user(db, client):
    user = {
        'email': 'rebecca.addler@gmail.com',
        'password': 'gam@12345',
        'name': 'Rebecca Adler',
    }
    resp = client.post('/users/', user)
    if resp.status_code == 201:
        return {
            'username': user['email'],
            'password': user['password'],
        }
