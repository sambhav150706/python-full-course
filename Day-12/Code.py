# Day 12 - Strings in Python
# Author: CodeWithSambhav

# -------------------------
# Example 1: Creating strings
# -------------------------
name = "Python Programming"
print(name)
'''
# -------------------------
# Example 2: Access characters
# -------------------------
print("First character:", name[0])
print("Last character:", name[12])
'''
'''
# -------------------------
# Example 3: String slicing
# -------------------------
print("Sliced string:", name[0:8])
name2=name[0:8]
print(name2)
'''
'''
# -------------------------
# Example 4: String methods
# -------------------------
text = "  hello world  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("world", "python"))
'''
'''
# -------------------------
# Example 5: Split string
# -------------------------
sentence = "Learn Python step by step"
words = sentence.split()
print(words)
'''
# -------------------------
# Example 6: User input string
# -------------------------
user_name = input("Enter your name: ")
print("Welcome", user_name)
