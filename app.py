from flask import Flask
from flask import jsonify
from flask import request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, AddressModel
import connexion
import json

app = Flask(__name__)
api = Api(app)
# app = connexion.App(__name__, specification_dir='./')
# app.add_api('swagger.yml')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/micha/PycharmProjects/Flask_REST_API/datas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
#migrate = Migrate(app, db)

addresses = [
    {
        "name": "United Center",
        "address": "1901 W Madison St",
        "city": "Chicago",
        "state": "IL",
        "postal_code": "60612",
        "value": "medium",
        "created": "{utc.datetime}"
    },
    {
        "name": "Madison Square Garden",
        "address": "4 Pennsylvania Plaza",
        "city": "New York",
        "state": "NY",
        "postal_code": "10001",
        "value": "low",
        "created": "{utc.datetime}"
    },
    {
        "name": "Staples Center",
        "address": "1111 S Figueroa St",
        "city": "Los Angeles",
        "state": "CA",
        "postal_code": "90015",
        "value": "low",
        "created": "{utc.datetime}"
    },
    {
        "name": "Phoenix Suns Arena",
        "address": "201 E Jefferson St",
        "city": "Phoenix",
        "state": "AZ",
        "postal_code": "85004",
        "value": "high",
        "created": "{utc.datetime}"
    },
    {
        "name": "Fiserv Forum",
        "address": "1111 Vel R. Phillips Ave",
        "city": "Milwaukee",
        "state": "WI",
        "postal_code": "53203",
        "value": "high",
        "created": "{utc.datetime}"
    }
]
#
with open('data.json') as file:
    y = json.load(file)


@app.before_first_request
def create_table():
    db.create_all()


class AddressesList(Resource):
    # @app.route('/', methods=['GET'])
    def get(self):
        addressess = AddressModel.query.all()

        return {'Addresses': list(x.json() for x in addressess)}

    # @app.route('/add', methods=['POST', 'GET'])
    def post(self):
        data = request.get_json()
        new_address = AddressModel(data['name'], data['address'], data['city'], data['state'], data['postal_code'], data['value'], data['created'])
        db.session.add(new_address)
        db.session.commit()
        return new_address.json(), 201
        # return jsonify(addresses)


class AddressesHigh(Resource):
    # @app.route('/', methods=['GET'])
    def get(self):
        addressess = AddressModel.query.filter_by(value="high").all()
        return {'Addresses': list(x.json() for x in addressess)}


api.add_resource(AddressesList, '/')
api.add_resource(AddressesHigh, '/filtered')

if __name__ == '__main__':
    app.run(debug=True)
