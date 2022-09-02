from pydoc import cli
from creds import CLIENT_ID, CLIENT_SECRET
import spotipy as sp
from dataExtractor import returnAllStats

creds = sp.oauth2.SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
client = sp.client.Spotify(client_credentials_manager=creds)


def returnSongs(id):
    # reference https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations
    artists = '0k17h0D3J5VfsdmQ1iZtE9,5WUlDfRSoLAfcVSX1WnrxN,2JY5qzEozvTdogkDTkkOMf,6eUKZXaKkcviH0Ku9w2n3V,7MSUfLeTdDEoZiJPDSBXgi'
    generes = 'rock,chill,ambient,children,pop'
    tracks = '6mFkJmJqdDVQ1REhVfGgd1,2J2Z1SkXYghSajLibnQHOa,4wNM9vSBzotBHn0R0fTkY5,3rmo8F54jFF8OgYsqTxm5d,1vgSaC0BPlL6LEm4Xsx59J'
    artists, generes, tracks = artists.split(
        ','), generes.split(','), tracks.split(',')
    recomendations = client.recommendations(
        seed_artists=artists, seed_genres=generes, seed_tracks=tracks, limit=10)
    return recomendations
    # work on bugs
    # possiblly enter value as a list and try]
    # work on calcultation for other variables
