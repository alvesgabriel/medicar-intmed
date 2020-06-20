def test_list_especialiades_not_authenticated(db, client):
    resp = client.get('/especialidades/')
    assert resp.status_code == 401


def test_list_especialiades_authenticated(db, client, auth_token):
    resp = client.get('/especialidades/', **auth_token)
    assert resp.status_code == 200


def test_list_especialiades_search(db, client, auth_token, especialidades):
    resp = client.get('/especialidades/?search=logia', **auth_token)
    body = resp.json()
    assert body.get('count') == 3
