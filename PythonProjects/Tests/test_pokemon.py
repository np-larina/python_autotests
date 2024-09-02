import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5bef63d3349b1d452d97118fba72c080'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
    }
OUERY = {'trainer_id': 5702}


def test_status_code():
    response_get = requests.get(url = f'{URL}/trainers', headers = HEADER)
    assert response_get.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': 5702})  
    assert response_get.json()["data"][0]["trainer_name"] == 'Prosecco killer'
