import requests
import json


def get_all_pokemon():
    data = {}
    for i in range(150):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
        data[]response.json()

get_all_pokemon()
