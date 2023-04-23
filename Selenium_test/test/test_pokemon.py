import requests
import pytest
import json

def test_status_code():
    token = "19abc49a742406ed9cdeb924814d44fa"
    response = requests.post('https://pokemonbattle.me:9104/pokemons', headers={'trainer_token' : token}, json={
    "name": "Бумер",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
    assert response.status_code == 400


def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 4095})
    response_body = response.text
    js = json.loads(response_body)
    assert js['trainer_name'] == 'Kim'


@pytest.mark.parametrize('key, value', [('trainer_name', 'Kim'), ('city', 'Narita') ])

def test_parts_of_body(key, value):
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 4095})
    # response_body = response.text
    assert response.json()[key] == value
