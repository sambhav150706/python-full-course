📘 NOTES (Day-16)
Class Syntax
class Student:
    pass

Creating Object
s1 = Student()

Class with Method
class Student:
    def greet(self):
        print("Hello Student")

Constructor (init)
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

Access Object Data
s1 = Student("Aman", 101)
print(s1.name)
print(s1.roll)

Key Points

self → current object

init → constructor
