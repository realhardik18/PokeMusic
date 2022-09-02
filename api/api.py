from flask import Flask
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)


class PokemonDataAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, location='args')
        data = dict(parser.parse_args())
        value = None  # work on giving back data
        response_dict = {'estimated ads': value}
        return response_dict


api.add_resource(PokemonDataAPI, '/pokemon', endpoint='pokemon')
app.run(debug=True)
