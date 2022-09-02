from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random')
def random():
    return render_template('data.html')

# MAKE AN ALGO TO GET SONGS RELATED TO POKEMON
# MAYBE LIKE 10
# THEN DISPLAY IT
