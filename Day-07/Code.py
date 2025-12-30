# Day 07 - break, continue, and pass in Python
# Author: CodeWithSambhav

# ---------------------------
# Example 1: break statement
# ---------------------------
print("Break Example:")
n=int(input("Enter the position you want to break: "))
for i in range(1, 11):
    if i == n:
        break
    print(i)

print("Loop stopped using break\n")


# ---------------------------
# Example 2: continue statement
# ---------------------------
print("Continue Example (skip even numbers):")
for i in range(1, 11):
    if i % 2 == 0:
        print("The number is skipped:", i)
        continue
    print(i)

print()


# ---------------------------
# Example 3: pass statement
# ---------------------------
print("Pass Example:")
for i in range(1, 6):
    if i == 3:
        print(i)
        pass   # placeholder, does nothing
    else:
        i+=1
        print(i)

print()

# ---------------------------
# Example 4: break with user input
# ---------------------------
print("Search Number Example:")
numbers = [10, 20, 30, 40, 50]
search = int(input("Enter number to search: "))

for num in numbers:
    if num == search:
        print("Number found!")
        break
else:
    print("Number not found")


# ---------------------------
# Example 5: continue with list
# ---------------------------
print("\nSkip negative numbers:")
values = [10, -5, 20, -3, 30]

for v in values:
    if v < 0:
        continue
    print(v)
