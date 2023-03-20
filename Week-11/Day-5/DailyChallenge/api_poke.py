import requests
import json


def get_all_pokemon():
    data = []
    for i in range(10):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
        if response.status_code == 200:
            data.append({'name':response.json()['species']['name'], 'img':response.json()['sprites']['front_default']})
    print(data)


def get_pokemon(var):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{var}')
    if response.status_code == 200:
        return {'success': True, 'name': response.json()['species']['name'], 'img': response.json()['sprites']['front_default']}
    return {'success': False}


def get_types_pokemon():
    response = requests.get(f'https://pokeapi.co/api/v2/type/')
    if response.status_code == 200:
        types = response.json()
        return {'success': True, 'types': [type_of_poke for type_of_poke in types["results"]]}
    return {'success': False}


def get_pokemon_by_type(url_type):
    response = requests.get(url_type)
    if response.status_code == 200:
        data = response.json()
        return {'success': True, 'pokes': [poke['pokemon']['name'] for poke in data["pokemon"]]}
    return {'success': False}
