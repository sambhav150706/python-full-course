# Day 03 – Input & Output in Python

## Output in Python
Python uses the `print()` function to display output on the screen.

### Example:
```python
print("Hello World")
print(10)
print(10 + 20)
Printing Multiple Values
Python can print multiple values together.

python
Copy code
name = "Sambhav"
age = 20
print(name, age)
Input in Python
Python uses the input() function to take input from the user.

python
Copy code
name = input("Enter your name: ")
print(name)
Important Rule
⚠️ Input taken using input() is always of type string.

python
Copy code
age = input("Enter your age: ")
print(age + 5)   # This will give an error
Type Conversion
To perform calculations, convert input to required data type.

Common conversions:
python
Copy code
int()
float()
str()
Example:
python
Copy code
age = int(input("Enter your age: "))
print(age + 5)
Practice Example
python
Copy code
name = input("Enter your name: ")
college = input("Enter your college: ")
print("My name is", name, "and I study at", college)
Summary
print() → displays output

input() → takes user input

Input is always a string

Use type conversion when needed

