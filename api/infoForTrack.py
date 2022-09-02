from creds import CLIENT_ID, CLIENT_SECRET
import spotipy as sp

creds = sp.oauth2.SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
client = sp.client.Spotify(client_credentials_manager=creds)


def returnSongData(id):
    return client.track(track_id=id)
