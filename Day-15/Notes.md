📘 NOTES (Day-15)
1️⃣ Basic try-except
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Error occurred")

2️⃣ Handling Specific Errors
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

3️⃣ Multiple except
try:
    a = int("abc")
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Zero division error")

4️⃣ else Block
try:
    print("No error")
except:
    print("Error")
else:
    print("Executed successfully")

5️⃣ finally Block
try:
    print(10 / 2)
except:
    print("Error")
finally:
    print("Program ended")
