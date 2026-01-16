class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)
        print("Grade:", self.grade())
        print("-" * 20)


students = []
while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter name: ")
            roll = int(input("Enter roll: "))
            marks = int(input("Enter marks: "))
            students.append(Student(name, roll, marks))
            print("Student added successfully!")

        elif choice == 2:
            if not students:
                print("No students available")
            else:
                for s in students:
                    s.display()

        elif choice == 3:
            roll = int(input("Enter roll to search: "))
            found = False
            for s in students:
                if s.roll == roll:
                    s.display()
                    found = True
                    break
            if not found:
                print("Student not found")

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid input")
