import requests


response = requests.post('https://pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": "19abc49a742406ed9cdeb924814d44fa",
    "email": "443332@.ru",
    "password": "Iloveqa1"
})

print (response.status_code)


token = "19abc49a742406ed9cdeb924814d44fa"
URL = "https://pokemonbattle.me:9104/"
num = f'мой токен это {token}'



response_activation = requests.post(f'{URL}trainers/confirm_email', json={
    "trainer_token": token
})

print (response_activation.text)

response_add_pokemon = requests.post(f'{URL}pokemons', headers={'trainer_token' : token}, json={
    "name": "Булька",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print (response_add_pokemon.text)

response = requests.get(f'{URL}pokemons', params={"trainer_id" : 4095})
print (response_add_pokemon.text)



