def test_list_medicos_not_authenticated(db, client):
    resp = client.get('/medicos/')
    assert resp.status_code == 401


def test_list_medicos_authenticated(db, client, auth_token):
    resp = client.get('/medicos/', **auth_token)
    assert resp.status_code == 200


def test_list_medicos(db, client, auth_token, medicos):
    resp = client.get('/medicos/', **auth_token)
    body = resp.json()
    assert body.get('count') == 4


def test_list_medicos_search(db, client, auth_token, medicos):
    resp = client.get('/medicos/?search=chopper', **auth_token)
    body = resp.json()
    assert body.get('results')[0].get('nome') == 'Tony Tony Chopper'


def test_list_medicos_especialidade(db, client, auth_token, medicos):
    cardiologia = medicos[0].get("especialidade").id
    resp = client.get(f'/medicos/?especialidade={cardiologia}', **auth_token)
    body = resp.json()
    assert body.get('count') == 2


def test_list_medicos_especialidades(db, client, auth_token, medicos):
    cardiologia = medicos[0].get("especialidade").id
    clinico_geral = medicos[1].get("especialidade").id
    resp = client.get(f'/medicos/?especialidade={cardiologia}&medico={clinico_geral}', **auth_token)
    body = resp.json()
    assert body.get('count') == 2
