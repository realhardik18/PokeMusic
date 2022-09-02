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
        min_liveness, max_liveness = 0.97, 1.0
        return [min_liveness, max_liveness]
    else:
        min_liveness = hp/136
        if min_liveness >= 0.5:
            max_liveness = min_liveness
            min_liveness = 0.5
        elif min_liveness <= 0.5:
            max_liveness = 0.5
        return [round(min_liveness, 2), round(max_liveness, 2)]


def returnSongs(id):
    # reference https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
    generes = ["rock", "chill", 'classical', 'edm']
    recomendations = client.recommendations(seed_genres=generes, limit=10)
    return recomendations['tracks'][0]

    # work on bugs
    # possiblly enter value as a list and try]
    # work on calcultation for other variables
print(defineLiveness(321))
