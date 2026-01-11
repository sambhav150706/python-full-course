# Inheritance example
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)


s1 = Student("Amit", 101)
s1.display()

print("------")

# Polymorphism example
class Car:
    def start(self):
        print("Car starts")

class Bike:
    def start(self):
        print("Bike starts")

for vehicle in (Car(), Bike()):
    vehicle.start()
