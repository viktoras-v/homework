

class Employee():
    def __init__(self, name: str, employee_id: int, salary: float):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, team: str):
        super().__init__(name, employee_id, salary)
        self.team = team

    def get_position(self) -> str:
        return "Manager"

class Engineer(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, seniority: str):
        super().__init__(name, employee_id, salary)
        self.seniority = seniority

    def get_position(self) -> str:
        return "Engineer"

class Intern(Employee):
    def __init__(self, name: str, employee_id: int, salary: float, age: str):
        super().__init__(name, employee_id, salary)
        self.age = age

    def get_role(self) -> str:
        return "Intern"

Jonas = Intern("Jonas", 50000, 25000, 21)

print(Jonas.name)
print(Jonas.get_role())
print(Jonas.employee_id)
print(Jonas.salary)
print(Jonas.age)



