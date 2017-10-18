from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.product import ProductController, ProductDetailController

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(ProductController, '/products')
api.add_resource(ProductDetailController, '/product/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)