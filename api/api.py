import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
from dataExtractor import returnAllStats
from songRecomendationSystem import returnSongIDS
app = Flask(__name__)
api = Api(app)


class PokemonDataAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args')
        data = dict(parser.parse_args())
        responseData = returnAllStats(data['id'])
        return responseData


class PokemonSongsRecomendationAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args')
        data = dict(parser.parse_args())
        songs = returnSongIDS(data['id'])
        return songs


api.add_resource(PokemonDataAPI, '/data', endpoint='pokemon')
api.add_resource(PokemonSongsRecomendationAPI, '/songs', endpoint='songs')
