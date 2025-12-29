# Day 06 – Loops in Python

## What is a Loop?
A loop is used to repeat a block of code multiple times.

---

## for Loop
Used when number of iterations is known.

Syntax:
```python
for variable in range(start, stop):
    code
Example:

python
Copy code
for i in range(5):
    print("Hello")
while Loop
Used when condition decides repetition.

Syntax:

python
Copy code
while condition:
    code
Example:

python
Copy code
i = 1
while i <= 5:
    print(i)
    i += 1
Important Points
range() controls repetition

Update variable in while loop

Avoid infinite loops

Summary
for loop → fixed repetitions

while loop → condition based

python
Copy code

---

## 💻 `loops.py`

```python
# Day 06 - Loops in Python

# for loop example
for i in range(1, 6):
    print("Python", i)

# printing numbers 1 to 10
for i in range(1, 11):
    print(i)

# while loop example
i = 1
while i <= 5:
    print("Hello")
    i += 1

# sum of first 5 numbers
sum = 0
i = 1
while i <= 5:
    sum += i
    i += 1

print("Sum is:", sum)
