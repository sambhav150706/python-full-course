# Day 13 - Dictionary Methods and Nested Dictionaries
# Author: CodeWithSambhav

# -------------------------
# Dictionary Methods
# -------------------------
student = {
    "name": "Aman",
    "age": 21,
    "course": "Python"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("name"))

student.update({"age": 22})
print("Updated:", student)

student.pop("course")
print("After pop:", student)

'''
# -------------------------
# Nested Dictionary
# -------------------------
students = {
    1: {"name": "Aman", "marks": 80},
    2: {"name": "Riya", "marks": 85},
    3: {"name": "Neha", "marks": 90}
}

print("\nStudent Records:")
for key, value in students.items():
    print(key, ":", value)

print("\nAccess single value:")
print(students[2]["name"])
'''
# -------------------------
# User Input Nested Dictionary
# -------------------------
records = {}

n = int(input("\nHow many students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    records[roll] = {
        "name": name,
        "marks": marks
    }

print("\nFinal Records:", records)
