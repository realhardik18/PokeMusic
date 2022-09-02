import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
from dataExtractor import returnAllStats
app = Flask(__name__)
api = Api(app)


class PokemonDataAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args')
        data = dict(parser.parse_args())
        responseData = returnAllStats(data['id'])
        print(responseData)
        return responseData


api.add_resource(PokemonDataAPI, '/pokemon', endpoint='pokemon')
app.run(debug=True)
