def test_list_agendas_not_authenticated(db, client):
    resp = client.get('/agendas/')
    assert resp.status_code == 401


def test_list_agendas_authenticated(db, client, auth_token):
    resp = client.get('/agendas/', **auth_token)
    assert resp.status_code == 200


def test_list_agendas(db, client, auth_token, agendas):
    resp = client.get('/agendas/', **auth_token)
    body = resp.json()
    assert body.get('count') == 3


def test_list_agendas_medico(db, client, auth_token, agendas):
    chopper = agendas[0].get("medico").id
    resp = client.get(f'/agendas/?medico={chopper}', **auth_token)
    body = resp.json()
    assert body.get('results')[0].get('medico').get('nome') == 'Tony Tony Chopper'
    assert body.get('count') == 1


def test_list_agendas_medicos(db, client, auth_token, agendas):
    chopper = agendas[0].get("medico").id
    house = agendas[1].get("medico").id
    resp = client.get(f'/agendas/?medico={chopper}&medico={house}', **auth_token)
    body = resp.json()
    assert body.get('count') == 2


def test_list_agendas_especialidade(db, client, auth_token, agendas):
    cardiologia = agendas[0].get("medico").especialidade.id
    resp = client.get(f'/agendas/?especialidade={cardiologia}', **auth_token)
    body = resp.json()
    assert body.get('count') == 1


def test_list_agendas_especialidades(db, client, auth_token, agendas):
    cardiologia = agendas[0].get("medico").especialidade.id
    oncologia = agendas[2].get("medico").especialidade.id
    resp = client.get(f'/agendas/?especialidade={cardiologia}&especialidade={oncologia}', **auth_token)
    body = resp.json()
    assert body.get('count') == 2


def test_list_agendas_intervalo_data(db, client, auth_token, agendas, amanha, dez_dias):
    resp = client.get(f'/agendas/?data_inicio={amanha}&data_final={dez_dias}', **auth_token)
    body = resp.json()
    assert body.get('count') == 1
