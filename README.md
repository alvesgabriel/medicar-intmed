# medicar-intmed
Desafio técnico do IntMed

[![Build Status](https://travis-ci.com/alvesgabriel/medicar-intmed.svg?branch=master)](https://travis-ci.com/alvesgabriel/medicar-intmed)
[![Python 3](https://pyup.io/repos/github/alvesgabriel/medicar-intmed/python-3-shield.svg)](https://pyup.io/repos/github/alvesgabriel/medicar-intmed/)
[![Updates](https://pyup.io/repos/github/alvesgabriel/medicar-intmed/shield.svg)](https://pyup.io/repos/github/alvesgabriel/medicar-intmed/)


* [Configurar Backend](#configurar-backend)
    * [Instalar Pipenv](#instalar-pipenv)
    * [Instalar dependências de Backend](#instalar-dependências-de-backend)
    * [Copiar arquivo de configuração](#copiar-arquivo-de-configuração)
    * [Criar banco de dados](#criar-banco-de-dados)
    * [Fazer migração](#fazer-migração)
    * [Executar Backend](#executar-backend)
* [Configurar Frontend](#configurar-frontend)
    * [Instalar ng CLI](#instalar-ng-cli)
    * [Instalar dependências de Frontend](#instalar-dependências-de-frontend)
    * [Executar Frontend](#executar-frontend)


---------------------
## Configurar Backend

### Instalar Pipenv
    pip install pipenv

### Instalar dependências de Backend
    pipenv sync -d


### Copiar arquivo de configuração
    cp contrib/env-sample .env

### Criar banco de dados
    psql -c "CREATE DATABASE testdb;" -U postgres

### Fazer migração
    pipenv run python manage.py migrate --noinput

### Executar Backend
    pipenv run python manage.py runserver 8080



----------------------
## Configurar Frontend


### Instalar ng CLI
    npm install -g ng-cli

### Instalar dependências de Frontend
    npm install

### Executar Frontend
    ng serve --port 8100 -o