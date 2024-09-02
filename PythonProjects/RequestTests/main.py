import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5bef63d3349b1d452d97118fba72c080'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
    }

body_post = {
    "name": "Пусечка",
    "photo_id": 11
}

body_put = {
    "pokemon_id": "45596",
    "name": "Лапулечка",
    "photo_id": 11
}

body_pokeball = {
    "pokemon_id": "45596"
}


response_post = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_post)
print (response_post.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print (response_put.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print (response_pokeball.text)
