import pytest

from backend.atendimento.models import Especialidade


@pytest.mark.parametrize(
    'especialidade',
    [
        {"nome": "Pediatria"},
        {"nome": "Ginecologia"},
        {"nome": "Cardiologia"},
        {"nome": "Clínico Geral"},
    ]
)
def test_add_especialidade(db, especialidade):
    nova_especialidade = Especialidade.objects.create(**especialidade)
    assert nova_especialidade.id is not None


def test_list_especialiades_not_authenticated(db, client):
    resp = client.get('/especialidades/')
    assert resp.status_code == 401


def test_list_especialiades_authenticated(db, client, auth_token):
    resp = client.get('/especialidades/', **auth_token)
    assert resp.status_code == 200


def test_list_especialiades_search(db, client, auth_token, especialidades):
    resp = client.get('/especialidades/?search=logia', **auth_token)
    body = resp.json()
    assert body.get('count') == 2
