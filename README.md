# PokeMusic
This is a project made under 24 hours for the boot.dev hackathon! I mainly used python to build this.
# what does it do?
PokeMusic uses the PokeApi and the SpotifyApi to find the the songs a specific pokemon would listen to. These songs are based off the stats of a particular pokemon.
# how does it work?
to get the songs, i first made a custom api to make it easier for me to retrive the data. this data is generated via an algorithm which i wrote. it calculates the energy,tempo,liveness and danceability of a song with the help of the stats of the pokemon.
now after getting this information, i used the recomendations endpoint on the spotify api to get 10 tracks which satisfy these parameters!
all this information is displayed on the main website. the website uses flask as a framework and bootstrap for the frontend. both the custom api and the website are hosted via heroku
# running it locally(1/2)
since i did not want users to go through the hassle of generating spotify credentials to get the api working, i hosted the api!
the api has the following endpoints:
- https://pokemusic-api.herokuapp.com/data?id={pokemon-id-from-pokeapi} [returns the stats of the specified pokemon]
 https://pokemusic-api.herokuapp.com/songs?id={pokemon-id-from-pokeapi} [returns the songs the specified pokemon would listen to]
# running it locally(2/2)
you can run the flask site locally on your pc! follow these instructions to do it!
- first clone the repo using `git clone https://github.com/realhardik18/PokeMusic.git`
- now navigate to the [website](https://github.com/realhardik18/PokeMusic/tree/main/website) folder
- now run `pip install -r requirements.txt` to install the required modules
- and finnaly run `wsgi.py` to host the website on localhost! 

# category
senior(i've been coding for almost 2 years now!)
