from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# MAKE AN ALGO TO GET SONGS RELATED TO POKEMON
# MAYBE LIKE 10
# THEN DISPLAY IT
