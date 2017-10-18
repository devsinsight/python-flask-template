from flask import json
from flask_restful import Resource

class Product(Resource):
    
    def get(self):
        car1 = Car('Big Foot', 2017)
        car2 = Car('Audi', 2017)
        car3 = Car('Mercedes Benz', 2017)

        cars = list([car1, car2, car3])
        return json.dumps([ car.__dict__ for car in cars ])

class ProductDetail(Resource):

    def get(self, id):
        return 'the id is {}'.format(id)

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
