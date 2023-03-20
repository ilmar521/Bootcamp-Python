import requests
import json


def get_all_pokemon(current_page):
    params = {}
    params["limit"] = 12
    params["offset"] = (current_page - 1) * 12
    response = requests.get('https://pokeapi.co/api/v2/pokemon/', params=params)
    if response.status_code == 200:
        data = response.json()
        return_data = []
        for poke in data['results']:
            response_poke = requests.get(poke['url'])
            return_data.append({'name': response_poke.json()['species']['name'], 'img': response_poke.json()['sprites']['front_default']})
        return {'success': True, 'data': return_data}
    return {'success': False}



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


get_all_pokemon(2)

