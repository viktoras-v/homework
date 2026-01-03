class Car:
    def __init__(self, brand, model, year):
       self.brand = brand
       self.model = model
       self.year = year
    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"
    def __repr__(self):
        return f"{self.brand} {self.model} {self.year}"
car1=Car("Audi", "100", 1989)
car2=Car("Audi", "A4", 2006)

print(car1.__str__())
print(car2.__repr__())