from models.employee import Employee

class EmployeeRepository:
    employees = []

    def __init__(self):
        self.id = 1

    def save(self, employee: Employee):
        employee.id = self.id
        self.employees.append(employee)
        self.id += 1

    def get(self, id):
        employee = [emp for emp in self.employees if emp.id == id][0]
        return employee

    def get_all(self):
        return self.employees

    def update(self, employee: Employee):
        pass

    def delete(self, id):
        pass