from pydoc import cli
from creds import CLIENT_ID, CLIENT_SECRET
import spotipy as sp
from dataExtractor import returnAllStats

creds = sp.oauth2.SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
client = sp.client.Spotify(client_credentials_manager=creds)


def defineLiveness(id):
    hp = int(returnAllStats(id=id)['HP'])
    if hp >= 136:
        target_liveness = 0.99
        return target_liveness
    else:
        target_liveness = hp/136
        return round(target_liveness, 2)


def defineTempo(id):
    speed = int(returnAllStats(id=id)['Speed'])
    if speed >= 132:
        target_tempo = 0.99
        return target_tempo
    else:
        target_tempo = speed/132
        return round(target_tempo, 2)


def defineEnergy(id):
    attack = int(returnAllStats(id=id)['Attack'])
    if attack >= 150:
        target_energy = 0.99
        return target_energy
    else:
        target_energy = attack/132
        return round(target_energy, 2)


def returnSongs(id):
    # reference https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
    generes = ["rock", "chill", 'classical', 'edm']

    recomendations = client.recommendations(seed_genres=generes, limit=10)
    return recomendations['tracks'][0]

    # work on bugs
    # possiblly enter value as a list and try]
    # work on calcultation for other variables
print(defineEnergy(200))
