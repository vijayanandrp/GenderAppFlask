from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from GenderPredictor.lib.gender_predictor import process_name
from flask_cors import CORS, cross_origin
from flask import json

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('name')


def classify_name():
    args = parser.parse_args()
    try:
        name = args['name']
        data = {"name": name, "classified": process_name(name)}
        response = app.response_class(
                response=json.dumps(data),
                status=201,
                mimetype='application/json'
        )
        return response
    except:
        return {"name": "Invalid", "classified": "Unknown"}


class GenderApp(Resource):
    def post(self):
        return classify_name()


api.add_resource(GenderApp, '/gender-app')

if __name__ == '__main__':
    app.run(debug=True)
