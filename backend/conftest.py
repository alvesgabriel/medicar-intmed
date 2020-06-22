from datetime import datetime, timedelta

import pytest
from django.urls import reverse

from backend.atendimento.models import Agenda, Consulta, Especialidade, Medico


@pytest.fixture
def hoje():
    return datetime.now()


@pytest.fixture
def amanha(hoje):
    return (hoje + timedelta(days=1)).strftime("%Y-%m-%d")


@pytest.fixture
def dez_dias(hoje):
    return (hoje + timedelta(days=10)).strftime("%Y-%m-%d")


@pytest.fixture
def trinta_dias(hoje):
    return (hoje + timedelta(days=30)).strftime("%Y-%m-%d")


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
        {"nome": "Oncologia"},
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
        },
        {
            "crm": 4846,
            "nome": "James Wilson",
            "especialidade": Especialidade.objects.get(pk=especialidades[4].get('id')),
        }
    ]
    for medico in medicos:
        novo_medico = Medico.objects.create(**medico)
        medico.update({'id': novo_medico.id})
    return medicos


@pytest.fixture
def agendas(db, medicos, amanha, trinta_dias):
    agendas = [
        {
            "medico": Medico.objects.get(pk=medicos[2].get('id')),
            "dia": amanha,
            "horarios": [
                Consulta(horario='14:00', dia=f"{amanha} 14:00"),
                Consulta(horario='14:15', dia=f"{amanha} 14:15"),
                Consulta(horario='16:00', dia=f"{amanha} 16:00"),
            ]
        },
        {
            "medico": Medico.objects.get(pk=medicos[1].get('id')),
            "dia": trinta_dias,
            "horarios": [
                Consulta(horario='08:00', dia=f"{trinta_dias} 08:00"),
                Consulta(horario='08:30', dia=f"{trinta_dias} 08:30"),
                Consulta(horario='09:00', dia=f"{trinta_dias} 09:00"),
                Consulta(horario='09:30', dia=f"{trinta_dias} 09:30"),
                Consulta(horario='14:00', dia=f"{trinta_dias} 14:00")
            ]
        },
        {
            "medico": Medico.objects.get(pk=medicos[3].get('id')),
            "dia": trinta_dias,
            "horarios": [
                Consulta(horario='08:00', dia=f"{trinta_dias} 08:00"),
                Consulta(horario='08:30', dia=f"{trinta_dias} 08:30"),
                Consulta(horario='09:00', dia=f"{trinta_dias} 09:00"),
                Consulta(horario='09:30', dia=f"{trinta_dias} 09:30"),
                Consulta(horario='14:00', dia=f"{trinta_dias} 14:00"),
            ]
        }
    ]
    for agenda in agendas:
        horarios = agenda.pop('horarios')
        nova_agenda = Agenda.objects.create(**agenda)
        agenda.update({'id': nova_agenda.id})
        for horario in horarios:
            horario.agenda = nova_agenda
        Consulta.objects.bulk_create(horarios)
        agenda.update({'horarios': horarios})
    return agendas


@pytest.fixture
def add_consulta(db, client, auth_token, agendas):
    agenda = agendas[0]
    data = {
        'agenda_id': agenda.get('id'),
        'horario': agenda.get('horarios')[0].horario,
    }
    resp = client.post('/consultas/', data=data, **auth_token)
    return resp.json()
