from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.product import ProductController, ProductDetailController
from resources.employee import EmployeeController
from resources.language import LanguageController

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(ProductController, '/products')
api.add_resource(ProductDetailController, '/product/<int:id>')
api.add_resource(EmployeeController, '/employee')
api.add_resource(LanguageController, '/languages')

if __name__ == '__main__':
    app.run(debug=True)