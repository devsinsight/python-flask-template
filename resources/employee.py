from flask import json, jsonify, request
from flask_restful import Resource
from models.employee import Employee
from repository.employee import EmployeeRepository

class EmployeeController(Resource):
    repository = EmployeeRepository()

    def get(self):
        return json.dumps([ emp.__dict__ for emp in self.repository.get_all() ])

    def post(self):
        get_json = request.get_json()
        employee = Employee(**get_json)
        self.repository.save(employee)
        return json.dumps(employee.__dict__)
    

    
