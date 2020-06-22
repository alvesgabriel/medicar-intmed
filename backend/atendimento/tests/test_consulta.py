def test_list_consultas_not_authenticated(db, client):
    resp = client.get('/consultas/')
    assert resp.status_code == 401


def test_list_consultas_authenticated(db, client, auth_token):
    resp = client.get('/consultas/', **auth_token)
    assert resp.status_code == 200


def test_add_agendas(db, client, auth_token, agendas):
    agenda = agendas[0]
    data = {
        'agenda_id': agenda.get('id'),
        'horario': agenda.get('horarios')[0].horario,
    }
    resp = client.post('/consultas/', data=data, **auth_token)
    assert resp.status_code == 201

    resp = client.get('/consultas/', **auth_token)
    body = resp.json()
    assert body.get('count') == 1


def test_del_agendas(db, client, auth_token, add_consulta):
    resp = client.delete(f'/consultas/{add_consulta.get("id")}/', **auth_token)
    assert resp.status_code == 204

    resp = client.get('/consultas/', **auth_token)
    body = resp.json()
    assert body.get('count') == 0
