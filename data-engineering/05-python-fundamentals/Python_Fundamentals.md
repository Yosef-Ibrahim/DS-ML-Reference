# 🐍 Python Fundamentals for Data Engineering — Complete Reference

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Class Notes For Python* course material (Rowad Misr Al-Raqmeya). Builds directly on foundational programming principles.

---

## 📑 Table of Contents
1. [Printing & String Formatting](#1-printing--string-formatting)
2. [Variables & Naming Rules](#2-variables--naming-rules)
3. [String Methods & F-Strings](#3-string-methods--f-strings)
4. [Numerical Operations & Data Types](#4-numerical-operations--data-types)
5. [Multiple Assignment & Constants](#5-multiple-assignment--constants)
6. [Python Comments & Docstrings](#6-python-comments--docstrings)
7. [Lists & Array Operations](#7-lists--array-operations)
8. [Adding, Modifying & Removing List Items](#8-adding-modifying--removing-list-items)
9. [Sorting & Ordering Lists](#9-sorting--ordering-lists)
10. [Numerical Lists, Range & Statistics](#10-numerical-lists-range--statistics)
11. [List Comprehensions](#11-list-comprehensions)

---

## 1) Printing & String Formatting

In Python, the `print()` function outputs data to standard output. 

* Single (`'`) and double (`"`) quotes can be used interchangeably for single-line strings.
* Escape characters like `\t` (tab) and `\n` (newline) control text formatting.
* Triple quotes (`'''` or `"""`) preserve multi-line formatting.

```python
print("Hello world!")
print('Hello world!')

# Multi-line string
print("""
Hello world!
My name is Youssef.
I am a Data Engineer.
""")
```

---

## 2) Variables & Naming Rules

Variables are containers for storing data values. Python is dynamically typed — variables are created when assigned and can change type.

```python
x = 5       # int
x = "Sally" # now str
```

### Variable Naming Rules
* Must start with a letter or underscore `_`.
* Cannot start with a number (`2var` is illegal ❌).
* Contains only alphanumeric characters and underscores (`A-z`, `0-9`, `_`).
* Case-sensitive (`age`, `Age`, `AGE` are 3 distinct variables).

> ⚠️ **Common Bug**: Referencing an uninitialized or misspelled variable name causes a runtime `NameError`.

---

## 3) String Methods & F-Strings

### Case Methods & Escaping
```python
name = "youssef"
print(name.upper()) # YOUSSEF
print(name.lower()) # youssef

# Escaping tab and newline
print("Languages:\n\tPython\n\tSQL\n\tPySpark")
```

### F-Strings (Formatted String Literals)
```python
first_name = "Youssef"
last_name = "Ibrahim"
full_name = f"{first_name} {last_name}"
print(full_name) # Youssef Ibrahim
```

---

## 4) Numerical Operations & Data Types

Python handles **Integers** (`int`) and **Floats** (`float`).

```python
print(2 + 3)   # 5 (Addition)
print(2 * 3)   # 6 (Multiplication)
print(2 ** 3)  # 8 (Exponentiation)
print(2 / 3)   # 0.6666666666666666 (Division always produces float)
print(10 // 3) # 3 (Floor Division)
print(10 % 3)  # 1 (Modulo / Remainder)
```

> ⚠️ **Float Precision Note**: Dividing integers in Python 3 always returns a `float` (`4 / 2 -> 2.0`). Adding an integer to a float converts the result to a float (`1 + 2.0 -> 3.0`).

---

## 5) Multiple Assignment & Constants

### Multiple Assignment
Assign multiple variables on a single line:
```python
x, y, z = 10, 20, 30
```

### Constants
Python does not enforce immutable constants at the language level. By convention, uppercase variable names signal that a value should be treated as constant.
```python
MAX_DB_CONNECTIONS = 5000
DEFAULT_TIMEOUT_SECONDS = 30
```

---

## 6) Python Comments & Docstrings

```python
# Single-line comment explaining data pipeline batch size
BATCH_SIZE = 1000

'''
Multi-line block comment:
Used for extensive documentation or temporary module disables.
'''
```

---

## 7) Lists & Array Operations

A **List** is a mutable, ordered collection of items. Lists can contain mixed data types.

```python
names = ['youssef', 'ali', 'ahmed', 'mohamed']

# 0-indexed access
print(names[0])  # 'youssef'

# Negative indexing (-1 returns last element)
print(names[-1]) # 'mohamed'
```

> ⚠️ **IndexError**: Attempting to access an index beyond `len(list) - 1` raises an `IndexError: list index out of range`. Always verify list length or use safe slicing/negative indexing.

---

## 8) Adding, Modifying & Removing List Items

### Modifying Elements
```python
names = ['youssef', 'ali', 'ahmed']
names[0] = 'max'
```

### Adding Elements
* **`.append(item)`**: Appends a single item to the end of the list.
* **`.extend([items])`**: Appends all items from an iterable.
* **`.insert(index, item)`**: Inserts item at specified index.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

# Append
motorcycles.append('ducati')

# Insert at index 0
motorcycles.insert(0, 'bmw')

# Extend
motorcycles.extend(['ktm', 'triumph'])
```

### Removing Elements
* **`del list[index]`**: Deletes item at specific index.
* **`.pop(index=-1)`**: Removes and returns item at index (default last item).
* **`.remove(value)`**: Deletes the first occurrence of a matching value.

```python
items = ['apple', 'banana', 'cherry', 'banana']

del items[0]                 # Removes 'apple'
popped_item = items.pop()    # Removes and returns 'banana'
items.remove('banana')       # Removes first 'banana'
```

---

## 9) Sorting & Ordering Lists

* **`list.sort()`**: Permanent in-place sorting.
* **`sorted(list)`**: Returns a new sorted list (preserves original list).
* **`list.reverse()`**: Reverses order in-place (does NOT sort backward).
* **`len(list)`**: Returns total item count.

```python
numbers = [5, 3, 1, 4, 2]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]

numbers.reverse()
print(numbers) # [5, 4, 3, 2, 1]
```

---

## 10) Numerical Lists, Range & Statistics

The `range(start, stop, step)` function generates sequence generators.

```python
# Generate numbers 1 to 5
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

# Generate even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers) # [2, 4, 6, 8, 10]

# Simple Statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # 0
print(max(digits)) # 9
print(sum(digits)) # 45
```

---

## 11) List Comprehensions

List comprehensions provide a concise syntax for constructing new lists from existing iterables.

```python
# Traditional loop vs List Comprehension
squares = [value**2 for value in range(1, 11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Conditional list comprehension
even_squares = [v**2 for v in range(1, 11) if v % 2 == 0]
print(even_squares) # [4, 16, 36, 64, 100]
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
