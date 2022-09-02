from urllib import response
import requests


def getTrackids(pokemon_id):
    response = requests.get(
        f'https://pokemusic-api.herokuapp.com/songs?id={pokemon_id}')
    return response.json()


def getPokemonData(pokemon_id):
    response = requests.get(
        f'https://pokemusic-api.herokuapp.com/data?id={pokemon_id}')
    return response.json()


# print(getPokemonData(pokemon_id=1))
