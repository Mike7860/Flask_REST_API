from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from app import get_timestamp

db = SQLAlchemy()


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


class AddressModel(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    postal_code = db.Column(db.String(80))
    value = db.Column(db.String(80))
    #price = db.Column(db.Integer())
    created = get_timestamp()

    def __init__(self, name, address, city, state, postal_code, value, created):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.value = value
        #price = db.Column(db.Integer())
        self.created = created

    def json(self):
        return {"name": self.name, "address": self.address, "city": self.city, "state": self.state, "postal_code": self.postal_code, "value": self.value, "created": self.created}