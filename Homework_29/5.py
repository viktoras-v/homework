import math

class Shape:
    def area(self, area):
        return 0
    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * math.pi
    def perimeter(self):
        return (self.radius * math.pi * 2)

r1 = Rectangle(5, 5)
print(r1.area())
print(r1.perimeter())

c1 = Circle(5)
print(c1.area())
print(c1.perimeter())   
