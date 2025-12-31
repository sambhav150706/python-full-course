# Day 08 - Functions in Python
# Author: CodeWithSambhav
'''
# -------------------------
# Example 1: Simple Function
# -------------------------
def greet():
    print("Hello, Welcome to Python!")

greet()
'''
'''
# -------------------------
# Example 2: Function with parameters
# -------------------------
def add(a, b):
    print("Sum:", a + b)

add(5, 3)
add(10, 20)

'''

# -------------------------
# Example 3: Function with return value
# -------------------------
def square(num):
    return num * num

n=int(input("Enter a number to find its square: "))
print(square(n))


'''
# -------------------------
# Example 4: Function for checking even or odd
# -------------------------
def check_even_odd(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
n=int(input("Enter a number to check even or odd: "))
check_even_odd(n)
'''
'''
# -------------------------
# Example 5: Function using user input
# -------------------------
def multiply(x, y):
    return x * y

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Multiplication:", multiply(a, b))
'''
