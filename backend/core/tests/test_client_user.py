import pytest


@pytest.mark.parametrize(
    'user',
    [
        {
            'email': 'rebecca.addler@gmail.com',
            'password': 'rebeca@123',
            'name': 'Rebecca Adler',
        }
    ]
)
def test_create(db, client, user):
    resp = client.post('/users/', user)
    assert resp.status_code == 201