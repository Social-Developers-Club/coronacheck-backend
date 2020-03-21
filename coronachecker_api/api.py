from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
URLS = {1 : 'Testurl'}

class CoronaChecker(Resource):
    def get(self):
        return {'score': '50%', 'geo-location': "-122.41942,37.77493"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("URL")
        args = parser.parse_args()
        url_id = int(max(URLS.keys())+1)
        url_id = '%i' % url_id
        URLS[url_id] = {"URL": args["URL"]}

        return URLS[url_id]


api.add_resource(CoronaChecker, '/URL/')

if __name__ == '__main__':
    app.run(debug=True)