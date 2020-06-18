import pytest
from django.urls import reverse

from backend.atendimento.models import Especialidade, Medico


@pytest.fixture
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


@pytest.fixture
def auth_token(db, client, logged_user):
    resp = client.post(reverse('login_token'), logged_user)
    token = {
        'HTTP_AUTHORIZATION': f'Token {resp.json().get("token")}'
    }
    return token


@pytest.fixture
def especialidades(db):
    especialidades = [
        {"nome": "Pediatria"},
        {"nome": "Ginecologia"},
        {"nome": "Cardiologia"},
        {"nome": "Clínico Geral"},
    ]
    for especialidade in especialidades:
        nova_especialidade = Especialidade.objects.create(**especialidade)
        especialidade.update({'id': nova_especialidade.id})
    return especialidades


@pytest.fixture
def medicos(db, especialidades):
    medicos = [
        {
            "crm": 3711,
            "nome": "Drauzio Varella",
            "especialidade": Especialidade.objects.get(pk=especialidades[2].get('id')),
        },
        {
            "crm": 2544,
            "nome": "Gregory House",
            "especialidade": Especialidade.objects.get(pk=especialidades[3].get('id')),
        },
        {
            "crm": 3087,
            "nome": "Tony Tony Chopper",
            "especialidade": Especialidade.objects.get(pk=especialidades[2].get('id')),
        }
    ]
    for medico in medicos:
        novo_medico = Medico.objects.create(**medico)
        medico.update({'id': novo_medico.id})
    return medicos
