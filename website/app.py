from logging import exception
from flask import Flask, render_template
import random
from getDataFromCustomApi import getPokemonData, getTrackData
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random')
def randomTrack():
    try:
        pokemon_id = random.randint(1, 1111)
        name = getPokemonData(pokemon_id=pokemon_id)['name']
        gif = getPokemonData(pokemon_id=pokemon_id)['GIF']
    except Exception as e:
        pokemon_id = 1
        name = getPokemonData(pokemon_id=pokemon_id)['name']
        gif = getPokemonData(pokemon_id=pokemon_id)['GIF']

    hp = getPokemonData(pokemon_id=pokemon_id)['HP']
    att = getPokemonData(pokemon_id=pokemon_id)['Attack']
    deff = getPokemonData(pokemon_id=pokemon_id)['Defense']
    spatt = getPokemonData(pokemon_id=pokemon_id)['Special Attack']
    spdef = getPokemonData(pokemon_id=pokemon_id)['Special Defense']
    speed = getPokemonData(pokemon_id=pokemon_id)['Speed']

    sno = 1
    data = list()
    for track in getTrackData(pokemon_id=pokemon_id):
        track_card_data = dict()
        track_card_data['url_to_artist'] = track['artists'][0]['external_urls']['spotify']
        track_card_data['name_of_artist'] = track['artists'][0]['name']
        track_card_data['name_of_track'] = track['name']
        track_card_data['popularity'] = track['popularity']
        track_card_data['sno'] = str(sno)
        track_card_data['embed_url'] = f"https://open.spotify.com/embed/track/{track['id']}?utm_source=generator"
        data.append(track_card_data)
        sno += 1
    return render_template('data.html', name=name, gif=gif, hp=hp, att=att, deff=deff, spatt=spatt, spdef=spdef, speed=speed, data=data)

# MAKE AN ALGO TO GET SONGS RELATED TO POKEMON
# MAYBE LIKE 10
# THEN DISPLAY IT
