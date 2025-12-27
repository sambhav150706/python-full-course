“Operators are the brain of Python logic — master this to master coding.”

# Day 04 – Operators in Python

## Arithmetic Operators
Used for mathematical calculations.

| Operator | Meaning |
|--------|---------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulus |
| ** | Power |
| // | Floor Division |

Example:
```python
a = 10
b = 3
print(a + b)

Comparison Operators

Return True or False.

Operator	Meaning
==	Equal
!=	Not Equal
>	Greater
<	Less
>=	Greater or Equal
<=	Less or Equal
Logical Operators
Operator	Meaning
and	Both conditions true
or	One condition true
not	Reverse result

Example:

x = 10
print(x > 5 and x < 20)

Summary

Operators perform calculations and comparisons

They return numeric or boolean results

Foundation for decision making


---

## 💻 `operators.py`

```python
a = 10
b = 3

# Arithmetic
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# Comparison
print(a > b)
print(a == b)

# Logical
x = 10
print(x > 5 and x < 20)
