import unittest
import math


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


# Tests
class TestShapes(unittest.TestCase):

    def setUp(self):
        # Objects for tests
        self.rect1 = Rectangle(5, 5)
        self.rect2 = Rectangle(2, 8)
        self.circle1 = Circle(5)
        self.circle2 = Circle(0)

    def tearDown(self):
        # Remove objects
        del self.rect1
        del self.rect2
        del self.circle1
        del self.circle2

    # Tests for rectangle
    def test_rectangle_area(self):
        self.assertEqual(self.rect1.area(), 25)
        self.assertEqual(self.rect2.area(), 16)
        self.assertGreater(self.rect1.area(), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(self.rect1.perimeter(), 20)
        self.assertEqual(self.rect2.perimeter(), 20)
        self.assertIsInstance(self.rect1.perimeter(), int)

    # Tests for cycles
    def test_circle_area(self):
        self.assertAlmostEqual(self.circle1.area(), math.pi * 25)
        self.assertEqual(self.circle2.area(), 0)
        self.assertGreaterEqual(self.circle1.area(), 0)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(self.circle1.perimeter(), 2 * math.pi * 5)
        self.assertEqual(self.circle2.perimeter(), 0)
        self.assertIsInstance(self.circle1.perimeter(), float)

    

if __name__ == "__main__":
    unittest.main()
