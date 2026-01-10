class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)


s1 = Student("Rahul", 1, 85)
s2 = Student("Neha", 2, 92)

s1.display()
print("-----")
s2.display()
