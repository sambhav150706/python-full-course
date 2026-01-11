📘 NOTES (Day-17)
1️⃣ Single Inheritance
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    pass

2️⃣ Using Parent Method
obj = Child()
obj.show()

3️⃣ Method Overriding
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

4️⃣ Polymorphism Example
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()

🔑 Key Points

Inheritance uses parent-child relationship

Polymorphism = same method, different output
