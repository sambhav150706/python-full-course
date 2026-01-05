🧠 NOTES (Day-13 for GitHub)
Important Dictionary Methods

keys() – returns all keys

values() – returns all values

items() – returns key-value pairs

get() – safely get value

update() – update dictionary

pop() – remove item

Example
student = {"name": "Aman", "age": 21}
student.get("name")

Nested Dictionary

A dictionary inside another dictionary.

Example:

students = {
    1: {"name": "Aman", "marks": 80},
    2: {"name": "Riya", "marks": 85}
}


Access:

students[1]["name"]
