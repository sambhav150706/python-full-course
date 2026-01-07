# Day 14 - File Handling in Python
# Author: CodeWithSambhav

# -------------------------
# Write to a file
# -------------------------
file = open("demo.txt", "w")
file.write("Welcome to Python File Handling\n")
file.write("This is Day-14\n")
file.close()

print("Data written successfully")

# -------------------------
# Read from a file
# -------------------------
file = open("demo.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()

# -------------------------
# Append to a file
# -------------------------
file = open("demo.txt", "a")
file.write("Appending new line\n")
file.close()

print("Data appended successfully")

# -------------------------
# Read line by line
# -------------------------
file = open("demo.txt", "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())
file.close()
