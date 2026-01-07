🧠 NOTES (Day-14 for GitHub)
What is File Handling?

File handling allows Python programs to read and write data to files stored on disk.

File Modes

r → Read

w → Write (creates new file or overwrites)

a → Append

r+ → Read and write

Opening a File
file = open("data.txt", "r")

Writing to a File
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

Reading from a File
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

Appending Data
file = open("data.txt", "a")
file.write("\nNew Line")
file.close()

Best Practice

Always close the file after use to save memory.
