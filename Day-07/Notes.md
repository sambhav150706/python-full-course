 Day 07 – break, continue, and pass in Python

## break Statement
Used to exit the loop immediately.

Example:
```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
continue Statement
Skips the current iteration and continues the loop.

Example:

python
Copy code
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
pass Statement
Used as a placeholder where a statement is required.

Example:

python
Copy code
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
Key Differences
break → exits loop

continue → skips iteration

pass → does nothing

Summary
Loop control statements help manage loop flow efficiently.

yaml
Copy code

---

## 💻 `loop_control.py`

```python
# Day 07 - break, continue, pass

# break example
for i in range(1, 11):
    if i == 6:
        break
    print(i)

print("Loop stopped")

# continue example
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# pass example
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
