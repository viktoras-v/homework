from turtledemo.planet_and_moon import GravSys


class Animal:
    def speak(self):
        print("I don't know what to speak")

class Cat(Animal):
    def speak(self):
        print("meow")

class Dog(Animal):
    def speak(self):
        print("woof")

Garfield = Cat()
Bruno = Dog()

Garfield.speak()
Bruno.speak()