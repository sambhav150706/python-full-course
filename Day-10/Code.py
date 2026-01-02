# Day 10 - Tuples and Sets in Python
# Author: CodeWithSambhav

# -------------------------
# Tuple Examples
# -------------------------
fruits = ("apple", "banana", "mango")
print("Tuple:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Tuple cannot be changed
#fruits[0] = "orange"  # This will cause an error

'''
# -------------------------
# Set Examples
# -------------------------
numbers = {1, 2, 3, 4, 4, 5}
print("\nSet:", numbers)  # duplicates removed automatically

numbers.add(6)
numbers.remove(2)
print("Updated Set:", numbers)

'''
'''
# -------------------------
# Set Operations
# -------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))


# -------------------------
# User Input Set
# -------------------------
user_set = set()
n = int(input("\nHow many numbers you want to add: "))

for i in range(n):
    val = int(input("Enter number: "))
    user_set.add(val)

print("Your unique numbers:", user_set)
'''
