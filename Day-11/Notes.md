What is a Dictionary?

A dictionary stores data in key : value pairs.

Creating a Dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

Accessing Values
student["name"]

Modifying Dictionary
student["age"] = 21

Adding New Key
student["city"] = "Delhi"

Looping Through Dictionary
for key, value in student.items():
    print(key, value)
