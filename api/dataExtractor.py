from urllib import response
import pandas as pd
import json
import requests


def getPokemonData(id):
    df = pd.read_csv('data\pokemon_stats.csv')
    df = df.drop(axis=1, labels='effort')
    return df.loc[df['pokemon_id'] == int(id)]
    # return df.head()


def returnAllStats(id):
    PossibleStats = ["HP", "Attack", "Defense", "Special Attack",
                     "Special Defense", "Speed", "accuracy", "evasion"]
    # stat id is the index of the stat +1
    data = dict()
    data['name'] = getNameOfPokemonFromID(id)
    data['GIF'] = getGIFOfPokemonFromID(id)
    stats = getPokemonData(id).values
    for stat in stats:
        data[PossibleStats[int(list(stat)[1]-1)]] = str(list(stat)[-1])
    return data


def getNameOfPokemonFromID(id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(id)}')
    return response.json()['forms'][0]['name']


def getGIFOfPokemonFromID(id):
    return f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/{id}.gif'


# print(returnAllStats(90))
# print(getNameOfPokemonFromID(10))


# print(getGIFOfPokemonFromID(2))
