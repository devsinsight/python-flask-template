from flask import Flask
from flask_restful import Api
from resources.product import Product, ProductDetail

app = Flask(__name__)
api = Api(app)

api.add_resource(Product, '/products')
api.add_resource(ProductDetail, '/product/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)