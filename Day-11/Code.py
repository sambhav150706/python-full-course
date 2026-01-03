# Day 11 - Dictionaries in Python
# Author: CodeWithSambhav

# -------------------------
# Example 1: Create dictionary
# -------------------------
student = {
    "name": "Aman",
    "age": 21,
    "course": "Python"
}

print(student)
'''
# -------------------------
# Example 2: Access values
# -------------------------
print("Name:", student["name"])
print("Course:", student["course"])
'''
'''
# -------------------------
# Example 3: Modify value
# -------------------------
student["age"] = 22
student["name"] = "Sambhav"
print("Updated age:", student["age"])
print("Updated name:", student["name"])
'''
'''
# -------------------------
# Example 4: Add new key
# -------------------------
student["city"] = "Delhi"
print(student)
'''
'''
# -------------------------
# Example 5: Loop through dictionary
# -------------------------
print("Student Details:")
for key, value in student.items():
    print(key, ":", value)
'''
# -------------------------
# Example 6: Dictionary with user input
# -------------------------
person = {}

person["name"] = input("Enter name: ")
person["age"] = int(input("Enter age: "))
person["skill"] = input("Enter skill: ")

print("Person Info:", person)
