from flask import json, request
from flask_restful import Resource

class LanguageController(Resource):

    def get(self):
        return json.dumps(['English', 'Spanish', 'Germany', 'Other'])

    