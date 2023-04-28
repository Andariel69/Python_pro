import requests

#create_account
response = requests.post('https://pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": 'AnyToken',
    "email": "443332@.ru",
    "password": "Iloveqa1"
})

print (response.status_code)

#variables
token = 'AnyToken'
URL = "https://pokemonbattle.me:9104/"
num = f'мой токен это {token}'


#trainer_activation_email
response_activation = requests.post(f'{URL}trainers/confirm_email', json={
    "trainer_token": token
})

print (response_activation.text)

#create_pokemon
response_create_pokemon = requests.post(f'{URL}pokemons', headers={'trainer_token' : token}, json={
    "name": "Булька",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print (response_create_pokemon.text)

#get_pokemons
response = requests.get(f'{URL}pokemons', params={"trainer_id" : 4095})
print (response_create_pokemon.text)

#add_pokemon_in_pokeball
response_add_pokeball = requests.post(f'{URL}trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": "9402"
})

print (response_add_pokeball.text)

#change_name_pokemon
response_change_name = requests.put(f'{URL}pokemons', headers={"trainer_token" : token}, json={
    "pokemon_id": "9402",
    "name": "Miu",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print (response_change_name.text)

#kill_pokemon
response_kill_pokemon = requests.post(f'{URL}pokemons/kill', headers={"trainer_token" : token}, json={
    "pokemon_id": "9404"
})

