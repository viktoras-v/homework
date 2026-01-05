import math


import math

class Shape:
    def area(self, area):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius ** 2 * math.pi








#class Animal:
 #   def speak(self):
  #      print("I don't know what to speak")

#class Cat(Animal):
 #   def speak(self):
  #      print("meow")

#class Dog(Animal):
 #   def speak(self):
  #      print("woof")

#Garfield = Cat()
#Bruno = Dog()

#Garfield.speak()
#Bruno.speak()