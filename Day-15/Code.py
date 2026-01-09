try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

finally:
    print("Execution completed")
