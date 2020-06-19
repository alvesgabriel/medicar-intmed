def test_list_medicos_not_authenticated(db, client):
    resp = client.get('/medicos/')
    assert resp.status_code == 401


def test_list_medicos_authenticated(db, client, auth_token):
    resp = client.get('/medicos/', **auth_token)
    assert resp.status_code == 200


def test_list_medicos(db, client, auth_token, medicos):
    resp = client.get('/medicos/', **auth_token)
    body = resp.json()
    assert body.get('count') > 0


def test_list_medicos_search(db, client, auth_token, medicos):
    resp = client.get('/medicos/?search=tony', **auth_token)
    body = resp.json()
    assert body.get('results')[0].get('nome') == 'Tony Tony Chopper'


def test_list_medicos_especialidade(db, client, auth_token, medicos):
    resp = client.get(f'/medicos/?especialidade={medicos[0].get("especialidade").id}', **auth_token)
    body = resp.json()
    assert body.get('count') == 2
