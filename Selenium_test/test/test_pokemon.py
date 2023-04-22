import requests
import pytest

def test_status_code():
    token = "19abc49a742406ed9cdeb924814d44fa"
    
response = requests.post('https://pokemonbattle.me:9104/pokemons' headers= trainer_token : {token}, json={
    "name": "Бумер",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
assert response.status_code == 201