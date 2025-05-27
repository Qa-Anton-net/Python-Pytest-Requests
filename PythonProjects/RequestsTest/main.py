import requests


url = 'https://api.pokemonbattle.ru/v2'
token = 'f9aa8535162ed78b7993a7a52ec47867'
header = {'Content-Type' : 'application/json', 'trainer_token' : token }

body_creat = {
    "name": "Бульбаавр",
    "photo_id": 11
}

body_registration = {
    "trainer_token": "token",
    "email": "andricov90@mail.ru",
    "password": "Legionerka1"
}

body_put = {
    "pokemon_id": "308178",
    "name": "New Name",
    "photo_id": 2
}

pokeboll = {
    "pokemon_id": "308178"
}



'''response = requests. post(url = f'{url}/v2/trainers/reg', headers=header, json=body_registration)
print (response.text)'''

'''response = requests. post(url = f'{url}/pokemons', headers=header, json=body_creat)
print(response.text)'''

'''response = requests. put(url = f'{url}/pokemons', headers=header, json=body_put)
print(response.text)'''

response = requests. post(url = f'{url}/trainers/add_pokeball', headers=header, json=pokeboll)
print(response.text)