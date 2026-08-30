# 📘 NumPy Reference — A Beginner-Friendly Guide

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute to this reference (ML / Data Science / Data Analysis topics only)? Reach out using the contact info above.

---

## 📑 Table of Contents
1. [Introduction](#1-introduction)
2. [Creating Arrays](#2-creating-arrays)
3. [Array Attributes](#3-array-attributes)
4. [Reshaping](#4-reshaping)
5. [Indexing & Slicing](#5-indexing--slicing)
6. [Arithmetic & Broadcasting](#6-arithmetic--broadcasting)
7. [Concatenate & Split](#7-concatenate--split)
8. [Aggregations](#8-aggregations)
9. [Linear Algebra](#9-linear-algebra)
10. [Sorting](#10-sorting)
11. [Extra Useful Functions](#11-extra-useful-functions)
12. [Saving & Loading Arrays](#12-saving--loading-arrays)
13. [Performance Notes](#13-performance-notes)

---

## 1) Introduction

**NumPy** = Numerical Python. It's the fundamental package for scientific computing, and anyone working in Data Science / ML needs to be comfortable with it.

**Why NumPy specifically?**
- **Broadcasting**: perform arithmetic between arrays of different shapes without writing manual loops.
- **Mathematical functions**: a huge library of ready-made, optimized functions.
- **Integration**: it's the foundation for libraries like Pandas, Scikit-learn, TensorFlow, and PyTorch.
- **N-Dimensional arrays**: represent data with any number of dimensions (1D, 2D, 3D...).
- **Much faster than plain Python lists** — it's implemented in C, and its data lives in one contiguous block of memory instead of being scattered around like a regular list.

```python
import numpy as np
```

---

## 2) Creating Arrays

### 1D array
```python
v1 = np.array([1, 2, 3, 4, 5, 6])
print(type(v1))      # <class 'numpy.ndarray'>
print(v1.shape)        # (6,)

v2 = np.array([1, 2, 3, 4, 5, 6])
v3 = v1 + v2             # element-wise addition
print(v3)                 # [2 4 6 8 10 12]
```

### 2D array (matrix)
Think of it like an Excel sheet: rows and columns.
```python
m = np.array([
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11],
    [12, 13, 14]
])
print(m.shape)   # (4, 3) -> (rows, columns)
```

### 3D array
Think of it as "a stack of 2D matrices" — for example, a color image is 3D: (height, width, channels).
```python
m3d = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[1, 2, 3, 4], [5, 6, 7, 8]]
])
print(m3d.shape)  # (2, 2, 4) -> (no. of matrices, rows, columns)
```

### 4D array
If 3D is a stack of matrices, 4D is a stack of 3D blocks — used, for example, to represent a batch of images in deep learning: (batch, channels, height, width).
```python
v4d = np.array([
    [
        [[1, 2, 3, 4], [5, 6, 7, 8]],
        [[1, 2, 3, 4], [5, 6, 7, 8]]
    ],
    [
        [[11, 22, 33, 44], [55, 66, 77, 88]],
        [[12, 23, 34, 45], [56, 67, 78, 89]]
    ]
])
print(v4d.shape)  # (2, 2, 2, 4)
```

### Ready-made creation functions
```python
# Array of zeros, shape (2,3,4)
zero_arrays = np.zeros((2, 3, 4))

# Array of ones, same idea
ones_arrays = np.ones((2, 3, 4))

# Like Python's range(), but returns a real array
ndarange = np.arange(10)   # [0 1 2 3 4 5 6 7 8 9]

# linspace(start, end, count) -> distributes "count" values evenly
# between start and end (both endpoints included)
space = np.linspace(0, 2, 10)

# Random floats between 0 and 1, shape (3,3)
random_array = np.random.rand(3, 3)

# Random integers between 1 and 10 (10 not included), shape (2,2)
random_integers = np.random.randint(1, 10, (2, 2))

# Fix the random seed so results are reproducible every run
# (important in experiments / ML)
np.random.seed(42)
```

> ⚠️ **`range()` vs `np.arange()`**: Python's built-in `range` is "lazy" — it doesn't actually allocate the numbers, so its size stays small even for huge ranges. `np.arange()` actually materializes the numbers in memory, so its size grows for real:
> ```python
> import sys
> print(sys.getsizeof(range(100000000)))     # small and constant
> print(sys.getsizeof(np.arange(100000000)))  # actually large
> ```

---

## 3) Array Attributes

```python
v6 = np.array([1, 2, 3, 4, 5, 6])

print(v6.dtype)   # data type (int64, float64, ...)
print(v6.shape)    # dimensions
print(v6.ndim)      # number of dimensions (1, 2, 3...)
print(v6.size)       # total number of elements
```

---

## 4) Reshaping

```python
v6 = np.array([1, 2, 3, 4, 5, 6])

print(v6.reshape(3, 2))
print(v6.reshape(2, 3))

# -1 means "figure out this dimension automatically"
print(v6.reshape(-1, 1))   # one column, rows computed automatically
```

### `flatten()` vs `ravel()`
Both collapse a matrix into a 1D array:
```python
m = np.array([[1, 2], [3, 4]])

f = m.flatten()   # returns a COPY — editing it never affects the original
r = m.ravel()      # usually returns a VIEW — editing it can affect the original (faster)
```
> 💡 Rule of thumb: `flatten()` is safer, `ravel()` is faster when you don't need an independent copy.

---

## 5) Indexing & Slicing

> Note: just like regular Python, indexing starts at **0**, and a slice (like `2:5`) **excludes** the end index.

### 1D
```python
v1d = np.array([1, 2, 3, 4, 5, 6])
print(v1d[2])      # element at index 2 -> 3
print(v1d[2:5])      # index 2 up to 4 -> [3 4 5]
```

### 2D
Syntax: `array[row, column]`
```python
v2d = np.array([
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11],
    [12, 13, 14]
])
print(v2d[3, 2])   # row 3, column 2 -> 14
```

### 3D / 4D
```python
v3d = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[1, 2, 3, 4], [5, 6, 7, 8]]
])
# (which matrix, which row, all columns)
print(v3d[0, 0, :])   # [1 2 3 4]

# same idea in 4D
print(v4d[1, 1, 1, :])
```

### Boolean Indexing (filtering by a condition)
One of the most important tools in data cleaning:
```python
arr = np.array([10, 15, 20, 25, 30])
mask = arr > 18
print(arr[mask])           # [20 25 30]
print(arr[arr % 2 == 0])    # even numbers only -> [10 20 30]
```

### Fancy Indexing (selecting elements by position)
```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])   # [10 30 50] -> elements at positions 0, 2, 4
```

---

## 6) Arithmetic & Broadcasting

**Broadcasting** is NumPy's way of making arrays of different shapes "fit" together in arithmetic operations, without you writing a loop yourself.

```python
v = np.array([1, 2, 3, 4, 5, 6])
print(v * 6)     # each element x 6 -> [6 12 18 24 30 36]
print(v + 6)      # each element + 6

# Broadcasting between a matrix and a vector
m = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(m + row)
# [[11 22 33]
#  [14 25 36]]
# NumPy automatically "repeats" row across every row of m.
```

### Matrix Multiplication
> ⚠️ `*` means element-wise multiplication (each element with its counterpart), **not** true matrix multiplication. Use `np.dot()` or `@` for that.
```python
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[0, 0, 1], [3, 2, 0], [0, 1, 0]])

print(np.dot(m1, m2))
print(m1 @ m2)   # same result, shorter/modern syntax
```

---

## 7) Concatenate & Split

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenate (join end to end)
print(np.concatenate([a, b]))        # [1 2 3 4 5 6]

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print(np.vstack([m1, m2]))   # stack on top of each other (adds rows)
print(np.hstack([m1, m2]))    # stack side by side (adds columns)

# Split into 3 equal parts
arr = np.arange(9)
print(np.split(arr, 3))   # [array([0,1,2]), array([3,4,5]), array([6,7,8])]
```

---

## 8) Aggregations

```python
v = np.array([1, 2, 3, 4, 5, 6])

print(np.mean(v))          # arithmetic mean
print(np.sum(v))            # sum
print(np.max(v))             # max value
print(np.min(v))              # min value
print(np.std(v))               # standard deviation

# Variance: by default divided by n, not n-1.
# For the "sample variance" (divided by n-1), pass ddof=1
print(np.var(v, ddof=1))
```

### The `axis` parameter (essential in data analysis)
When working with a matrix, you need to specify whether an operation runs down the rows or across the columns:
```python
m = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(m))            # sum of all elements -> 21
print(np.sum(m, axis=0))     # sum of each column -> [5 7 9]
print(np.sum(m, axis=1))      # sum of each row -> [6 15]
```
> 💡 Easy rule to remember: `axis=0` means "move down the rows", `axis=1` means "move across the columns".

---

## 9) Linear Algebra

```python
# Diagonal matrix
diagonal_matrix = np.diag([1, 2, 3, 4, 5, 6])

# Identity matrix
Identity_matrix = np.eye(4)

# Upper triangular matrix
upper_Triangular = np.array([
    [1, 2, 3],
    [0, 5, 6],
    [0, 0, 9]
])

# Transpose (swap rows and columns) — two equivalent ways
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(np.transpose(matrix))
print(matrix.T)

# Trace: sum of the main diagonal
print(upper_Triangular.trace())

# Determinant — linalg = Linear Algebra
print(np.linalg.det(upper_Triangular))

# Inverse — only exists for square, non-singular matrices
print(np.linalg.inv(upper_Triangular))

# Rank
print(np.linalg.matrix_rank(upper_Triangular))
```

---

## 10) Sorting

```python
arr = np.array([5, 2, 8, 1, 9])

print(np.sort(arr))       # ascending order -> [1 2 5 8 9]
print(np.argsort(arr))     # positions that would sort it -> [3 1 0 2 4]

# Sort a matrix by a specific column (very common in data cleaning)
m = np.array([[3, 1], [1, 2], [2, 0]])
print(m[m[:, 0].argsort()])   # sorts rows by the values in column 0
```

---

## 11) Extra Useful Functions

```python
arr = np.array([1, 2, 2, 3, 3, 3, 4])

print(np.unique(arr))              # unique values, no duplicates -> [1 2 3 4]

# np.where: a per-element ternary-like condition
print(np.where(arr > 2, "high", "low"))

print(np.clip(arr, 2, 3))          # clamp values between 2 and 3

print(np.cumsum(arr))              # cumulative sum -> [1 3 5 8 11 14 18]
```

---

## 12) Saving & Loading Arrays

Very useful for saving the result of some data processing and reusing it later without recomputing:
```python
arr = np.array([1, 2, 3, 4, 5])

np.save("my_array.npy", arr)        # save in NumPy's own format (fast, exact)
loaded = np.load("my_array.npy")

np.savetxt("my_array.csv", arr, delimiter=",")   # save as plain CSV (openable in Excel)
loaded_csv = np.loadtxt("my_array.csv", delimiter=",")
```

---

## 13) Performance Notes

- **Vectorization**: always prefer direct NumPy operations (like `v * 6`) over a manual `for` loop — the speed difference is huge on large data.
- **Copy vs View**: some operations (like basic slicing) return a "view", not an independent copy — editing that slice can affect the original. Use `.copy()` when you need a fully independent copy:
  ```python
  a = np.array([1, 2, 3])
  b = a[0:2]          # view -> linked to a
  c = a[0:2].copy()    # copy -> fully independent
  ```
- **dtype**: keep an eye on the array's data type; convert it with `.astype()`:
  ```python
  arr = np.array([1, 2, 3])
  print(arr.astype(float))   # [1. 2. 3.]
  ```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
