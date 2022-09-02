import pandas as pd
import json


def getPokemonData(id):
    df = pd.read_csv('api\data\pokemon_stats.csv')
    df = df.drop(axis=1, labels='effort')
    return df.loc[df['pokemon_id'] == int(id)]
    # return df.head()


def returnAllStats(id):
    PossibleStats = ["HP", "Attack", "Defense", "Special Attack",
                     "Special Defense", "Speed", "accuracy", "evasion"]
    # stat id is the index of the stat +1
    data = dict()
    stats = getPokemonData(id).values
    for stat in stats:
        data[PossibleStats[int(list(stat)[1]-1)]] = list(stat)[-1]
    return data


# print(returnAllStats(1))
