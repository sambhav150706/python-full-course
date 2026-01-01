# Day 09 - Lists in Python
# Author: CodeWithSambhav
'''
# -------------------------
# Example 1: Creating a list
# -------------------------
numbers = [10, 20, 30, 40, 50]
print(numbers)

'''
'''
# -------------------------
# Example 2: Accessing elements
# -------------------------
numbers=[10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-5])
'''
'''
# -------------------------
# Example 3: Modifying list
# -------------------------
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print("Updated list:", numbers)

'''
'''
# -------------------------
# Example 4: List methods
# -------------------------
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(2, 15)
numbers.remove(40)
print("After operations:", numbers)
'''
'''
# -------------------------
# Example 5: Loop through list
# -------------------------
numbers = [10, 20, 30, 40, 50]
print("List elements:")
for num in numbers:
    print(num)
'''
# -------------------------
# Example 6: User input list
# -------------------------
items = []
n = int(input("How many items you want to add: "))

for i in range(n):
    value = int(input("Enter item: "))
    items.append(value)

print("Your list:", items)
