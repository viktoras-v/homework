import math
import pytest

# Classes
class Shape:
    def area(self):
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
        return 2 * math.pi * self.radius

# Fixtures for objects
@pytest.fixture
def rectangles():
    rect1 = Rectangle(5, 5)
    rect2 = Rectangle(2, 8)
    return rect1, rect2

@pytest.fixture
def circles():
    circle1 = Circle(5)
    circle2 = Circle(0)
    return circle1, circle2

# Tests for rectangles
def test_rectangle_area(rectangles):
    rect1, rect2 = rectangles
    assert rect1.area() == 25
    assert rect2.area() == 16
    assert rect1.area() > 0

def test_rectangle_perimeter(rectangles):
    rect1, rect2 = rectangles
    assert rect1.perimeter() == 20
    assert rect2.perimeter() == 20
    assert isinstance(rect1.perimeter(), int)

# Tests for circles
def test_circle_area(circles):
    circle1, circle2 = circles
    assert math.isclose(circle1.area(), math.pi * 25)
    assert circle2.area() == 0
    assert circle1.area() >= 0

def test_circle_perimeter(circles):
    circle1, circle2 = circles
    assert math.isclose(circle1.perimeter(), 2 * math.pi * 5)
    assert circle2.perimeter() == 0
    assert isinstance(circle1.perimeter(), float)

