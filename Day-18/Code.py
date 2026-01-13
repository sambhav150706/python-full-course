# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class
class Student(Person):
    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks

    def display(self):
        super().display()
        print("Roll No:", self.roll)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


# Creating objects
s1 = Student("Rahul", 20, 101, 88)
s2 = Student("Neha", 21, 102, 92)

print("Student 1 Details")
s1.display()
print("\nStudent 2 Details")
s2.display()
