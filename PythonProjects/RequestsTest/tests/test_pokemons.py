import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = 'f9aa8535162ed78b7993a7a52ec47867'
header = {'Content-Type' : 'application/json', 'trainer_token' : token }
trainer_id = 34057

def test_status_code():
    response = requests.get(url = f'{url}/trainers/')
    assert response.status_code == 200

def test_trainer_id():
    response = requests.get(url = f'{url}/trainers/' , params = {'trainer_id' : trainer_id})
    assert response.json()["data"][0]["id"] == "34057"