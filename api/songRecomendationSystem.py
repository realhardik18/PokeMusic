from creds import CLIENT_ID, CLIENT_SECRET
import spotipy as sp
from dataExtractor import returnAllStats
from infoForTrack import returnSongData

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


def defineDanceability(id):
    speed = int(returnAllStats(id=id)['Speed'])
    if speed >= 132:
        target_danceability = 0.99
        return target_danceability
    else:
        target_danceability = speed/132
        return round(target_danceability, 2)


def defineEnergy(id):
    attack = int(returnAllStats(id=id)['Attack'])
    if attack >= 150:
        target_energy = 0.99
        return target_energy
    else:
        target_energy = attack/132
        return round(target_energy, 2)


def returnSongIDS(id):
    # reference https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
    generes = ["rock", "chill", 'classical', 'edm']
    liveness = defineLiveness(id)
    danceability = defineDanceability(id)
    energy = defineEnergy(id)
    recomendations = client.recommendations(
        seed_genres=generes, target_energy=energy, target_liveness=liveness, target_danceability=danceability, limit=10)
    song_data = list()
    for song in recomendations['tracks']:
        song_data.append(returnSongData(song['id']))
    return song_data

    # work on bugs
    # possiblly enter value as a list and try]
    # work on calcultation for other variables
# print(returnSongIDS(25))
