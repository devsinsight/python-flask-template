from flask import json, jsonify
from flask_restful import Resource
from models.product import Product

class DataExample:
        def __init__(self):
            self.prod1 = Product(id=1,
                name='Garden Cart',
                code='GDN-0023', 
                release_date='October 15, 2017',
                description='15 gallon capacity rolling',
                price=32.99,
                star_rating=4.2,
                image_url='https://openclipart.org/image/50px/svg_to_png/58471/garden-cart.png&disposition=attachment')
        
            self.prod2 = Product(id=2,
                name='Hammer',
                code='TBX-0048', 
                release_date='October 15, 2017',
                description='Curved claw steel hammer',
                price=55.99,
                star_rating=2.2,
                image_url='https://openclipart.org/image/50px/svg_to_png/73/rejon-Hammer.png&disposition=attachment')

            self.prod3 = Product(id=3,
                name='Leaf Rake',
                code='GDN-0011', 
                release_date='October 15, 2017',
                description='Leaf rake with 48-inch wooden handle',
                price=19.99,
                star_rating=3.2,
                image_url='https://openclipart.org/image/50px/svg_to_png/26215/Anonymous_Leaf_Rake.png&disposition=attachment')               

            self.products = [self.prod1, self.prod2, self.prod3]

class ProductController(Resource, DataExample):

    def get(self):
        return json.dumps([ product.__dict__ for product in self.products ])

class ProductDetailController(Resource, DataExample):

    def get(self, id):
        product = [product for product in self.products if product.id == id][0]
        return json.dumps(product.__dict__)


