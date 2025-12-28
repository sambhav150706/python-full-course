# Day 05 – if-else Statements in Python

## if Statement
Executes code only when condition is True.

```python
if condition:
    statement
Example:

python
Copy code
age = 20
if age > 18:
    print("Adult")
if-else Statement
python
Copy code
if condition:
    statement
else:
    statement
Example:

python
Copy code
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
if-elif-else Statement
Used for multiple conditions.

python
Copy code
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
Important Notes
Indentation is mandatory

Conditions return True or False

Use comparison operators

Summary
if → checks condition

else → runs when if is False

elif → checks multiple conditions

python
Copy code

---

## 💻 `if_else.py`

```python
# Voting eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Even or Odd
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
