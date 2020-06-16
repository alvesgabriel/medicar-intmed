import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'user',
    [
        {
            'email': 'rebecca.addler@gmail.com',
            'password': 'rebecca@123',
            'name': 'Rebecca Adler',
        }
    ]
)
def test_create(db, client, user):
    resp = client.post('/users/', user)
    assert resp.status_code == 201


def test_login(db, client, logged_user):
    resp = client.post(reverse('login_token'), data=logged_user)
    assert resp.status_code == 200
    assert isinstance(resp.json().get('token'), str)
