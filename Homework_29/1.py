class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age


student=Person("Jonas", 22)

print(student.get_name())
print(student.get_age())

student.set_name("Antanas")
student.set_age(23)

print(student.get_name())
print(student.get_age())


