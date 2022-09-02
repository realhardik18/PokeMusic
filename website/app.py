from logging import exception
from flask import Flask, render_template
import random
from getDataFromCustomApi import getPokemonData, getTrackids
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
    return render_template('data.html', name=name, gif=gif, hp=hp, att=att, deff=deff, spatt=spatt, spdef=spdef, speed=speed)

# MAKE AN ALGO TO GET SONGS RELATED TO POKEMON
# MAYBE LIKE 10
# THEN DISPLAY IT
