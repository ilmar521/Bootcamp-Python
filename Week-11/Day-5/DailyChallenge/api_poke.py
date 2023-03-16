import requests
import json


def get_all_pokemon():
    data = []
    for i in range(10):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
        if response.status_code == 200:
            data.append({'name':response.json()['species']['name'], 'img':response.json()['sprites']['front_default']})
    print(data)

get_all_pokemon()
