import pytest
from django.urls import reverse

from backend.atendimento.models import Especialidade


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


@pytest.fixture()
def auth_token(db, client, logged_user):
    resp = client.post(reverse('login_token'), logged_user)
    token = {
        'HTTP_AUTHORIZATION': f'Token {resp.json().get("token")}'
    }
    return token


@pytest.fixture()
def especialidades(db):
    especialidades = [
        {"nome": "Pediatria"},
        {"nome": "Ginecologia"},
        {"nome": "Cardiologia"},
        {"nome": "Clínico Geral"},
    ]
    for especialidade in especialidades:
        Especialidade.objects.create(**especialidade)
