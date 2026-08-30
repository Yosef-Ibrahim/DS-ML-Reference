"""
NumPy Reference — Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email : youssefibrahimelisely@gmail.com
Phone : 01119834356

Want to contribute an idea, fix, or new example (ML / Data Science / Data
Analysis topics only)? Reach out on the contact info above.
"""

import numpy as np

# =========================================================
# 1) INTRODUCTION
# =========================================================
# NumPy = Numerical Python. It is the fundamental package for
# scientific computing in Python.
#
# Key features:
# - Broadcasting: operate on arrays of different shapes without writing loops
# - A huge library of optimized mathematical functions
# - Tight integration with libraries like Pandas, Scikit-learn, TensorFlow
# - N-Dimensional arrays (1D, 2D, 3D, ...)
# - Much faster than plain Python lists because it's implemented in C and
#   stores data in one contiguous block of memory instead of scattered objects


# =========================================================
# 2) CREATING ARRAYS
# =========================================================

# ---- 1D array ----
v1 = np.array([1, 2, 3, 4, 5, 6])
print(type(v1))     # <class 'numpy.ndarray'>
print(v1.shape)      # (6,)

v2 = np.array([1, 2, 3, 4, 5, 6])
v3 = v1 + v2          # element-wise addition
print(v3)             # [2 4 6 8 10 12]

# ---- 2D array (matrix) ----
# Think of it like an Excel sheet: rows and columns.
m = np.array([
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11],
    [12, 13, 14]
])
print(m.shape)  # (4, 3) -> (rows, columns)

# ---- 3D array ----
# Think of it as "a stack of 2D matrices" — e.g. a color image is 3D:
# (height, width, channels).
m3d = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[1, 2, 3, 4], [5, 6, 7, 8]]
])
print(m3d.shape)  # (2, 2, 4) -> (no. of matrices, rows, columns)

# ---- 4D array ----
# If 3D is a stack of matrices, 4D is a stack of 3D blocks — used, for
# example, to represent a batch of images in deep learning:
# (batch, channels, height, width).
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

# ---- Ready-made creation functions ----
zero_arrays = np.zeros((2, 3, 4))     # array of zeros, shape (2,3,4)
ones_arrays = np.ones((2, 3, 4))       # array of ones, shape (2,3,4)

ndarange = np.arange(10)               # like Python's range(), but a real array
print(ndarange)                        # [0 1 2 3 4 5 6 7 8 9]

# range() vs np.arange():
# range() is "lazy" in plain Python — it doesn't actually allocate the
# numbers, so its size stays small even for huge ranges. np.arange()
# actually creates the numbers in memory, so its size grows with the count.
import sys
r1 = range(10)
r2 = range(10000000)
ar1 = np.arange(10)
ar2 = np.arange(100000000)
print(sys.getsizeof(r1))
print(sys.getsizeof(r2))
print(sys.getsizeof(ar1))
print(sys.getsizeof(ar2))

# linspace(start, end, count): distributes "count" values evenly between
# start and end (both endpoints included).
space = np.linspace(0, 2, 10)
print(space)

# Random arrays
random_array = np.random.rand(3, 3)          # floats between 0 and 1, shape (3,3)
random_integers = np.random.randint(1, 10, (2, 2))  # ints in [1,10), shape (2,2)

# Fix the random seed so results are reproducible every run — important in
# experiments and ML.
np.random.seed(42)


# =========================================================
# 3) ARRAY ATTRIBUTES
# =========================================================
v6 = np.array([1, 2, 3, 4, 5, 6])
print(v6.dtype)   # data type (int64, float64, ...)
print(v6.shape)    # dimensions
print(v6.ndim)      # number of dimensions (1, 2, 3, ...)
print(v6.size)       # total number of elements


# =========================================================
# 4) RESHAPING
# =========================================================
print(v6.reshape(3, 2))
print(v6.reshape(2, 3))

# -1 means "figure out this dimension automatically"
print(v6.reshape(-1, 1))   # one column, rows computed automatically

# flatten() vs ravel(): both collapse an array to 1D.
m = np.array([[1, 2], [3, 4]])
f = m.flatten()   # returns a COPY — editing it never affects the original
r = m.ravel()      # usually returns a VIEW — editing it can affect the original (faster)
# Rule of thumb: flatten() is safer, ravel() is faster when you don't need
# an independent copy.


# =========================================================
# 5) INDEXING & SLICING
# =========================================================
# Note: indexing starts at 0, and slices (e.g. 2:5) exclude the end index.

# ---- 1D ----
v1d = np.array([1, 2, 3, 4, 5, 6])
print(v1d[2])       # element at index 2 -> 3
print(v1d[2:5])       # index 2 up to 4 -> [3 4 5]

# ---- 2D: array[row, column] ----
v2d = np.array([
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11],
    [12, 13, 14]
])
print(v2d[3, 2])   # row 3, column 2 -> 14

# ---- 3D / 4D ----
v3d = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[1, 2, 3, 4], [5, 6, 7, 8]]
])
print(v3d[0, 0, :])   # (matrix 0, row 0, all columns) -> [1 2 3 4]
print(v4d[1, 1, 1, :])  # same idea in 4D

# ---- Boolean indexing (filtering by condition) ----
# One of the most-used tools in data cleaning.
arr = np.array([10, 15, 20, 25, 30])
mask = arr > 18
print(arr[mask])           # [20 25 30]
print(arr[arr % 2 == 0])    # even numbers only -> [10 20 30]

# ---- Fancy indexing (select elements by their positions) ----
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])   # [10 30 50] -> elements at positions 0, 2, 4


# =========================================================
# 6) ARITHMETIC & BROADCASTING
# =========================================================
# Broadcasting: NumPy's way of making arrays of different shapes "fit"
# together in arithmetic operations without you writing a loop yourself.
v = np.array([1, 2, 3, 4, 5, 6])
print(v * 6)      # each element x 6 -> [6 12 18 24 30 36]
print(v + 6)       # each element + 6

# Broadcasting between a matrix and a vector
m = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(m + row)
# [[11 22 33]
#  [14 25 36]]
# NumPy automatically "repeats" row across every row of m.

# Matrix multiplication
# Careful: * means element-wise multiplication (each element by its
# counterpart), NOT true matrix multiplication. Use np.dot() or @ for that.
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[0, 0, 1], [3, 2, 0], [0, 1, 0]])
print(np.dot(m1, m2))
print(m1 @ m2)   # same result, shorter/modern syntax


# =========================================================
# 7) CONCATENATE & SPLIT
# =========================================================
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate([a, b]))    # [1 2 3 4 5 6]

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.vstack([m1, m2]))   # stack on top of each other (adds rows)
print(np.hstack([m1, m2]))    # stack side by side (adds columns)

arr = np.arange(9)
print(np.split(arr, 3))   # split into 3 equal parts


# =========================================================
# 8) AGGREGATIONS
# =========================================================
v = np.array([1, 2, 3, 4, 5, 6])
print(np.mean(v))    # arithmetic mean
print(np.sum(v))      # sum of all elements
print(np.max(v))       # max value
print(np.min(v))        # min value
print(np.std(v))         # standard deviation

# Variance: by default divided by n, not n-1. For the "sample variance"
# (divided by n-1) pass ddof=1.
print(np.var(v, ddof=1))

# The axis parameter (essential in data analysis): decide whether an
# operation runs down the rows or across the columns.
m = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(m))            # sum of all elements -> 21
print(np.sum(m, axis=0))     # sum of each column -> [5 7 9]
print(np.sum(m, axis=1))      # sum of each row -> [6 15]
# Easy rule to remember: axis=0 -> "move down the rows",
#                          axis=1 -> "move across the columns"


# =========================================================
# 9) LINEAR ALGEBRA
# =========================================================
diagonal_matrix = np.diag([1, 2, 3, 4, 5, 6])   # diagonal matrix
Identity_matrix = np.eye(4)                       # identity matrix

upper_Triangular = np.array([
    [1, 2, 3],
    [0, 5, 6],
    [0, 0, 9]
])

# Transpose (swap rows and columns) — two equivalent ways
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(np.transpose(matrix))
print(matrix.T)

print(upper_Triangular.trace())              # sum of the main diagonal
print(np.linalg.det(upper_Triangular))        # determinant (linalg = linear algebra)
print(np.linalg.inv(upper_Triangular))         # inverse (square, non-singular matrices only)
print(np.linalg.matrix_rank(upper_Triangular))  # rank


# =========================================================
# 10) SORTING
# =========================================================
arr = np.array([5, 2, 8, 1, 9])
print(np.sort(arr))       # ascending order -> [1 2 5 8 9]
print(np.argsort(arr))     # positions that would sort the array -> [3 1 0 2 4]

# Sort a matrix by a specific column (very common in data cleaning)
m = np.array([[3, 1], [1, 2], [2, 0]])
print(m[m[:, 0].argsort()])   # sorts rows by the values in column 0


# =========================================================
# 11) EXTRA USEFUL FUNCTIONS
# =========================================================
arr = np.array([1, 2, 2, 3, 3, 3, 4])
print(np.unique(arr))                 # unique values, no duplicates -> [1 2 3 4]
print(np.where(arr > 2, "high", "low"))  # a ternary-like condition per element
print(np.clip(arr, 2, 3))              # clamp values between 2 and 3
print(np.cumsum(arr))                   # cumulative sum -> [1 3 5 8 11 14 18]


# =========================================================
# 12) SAVING & LOADING ARRAYS
# =========================================================
arr = np.array([1, 2, 3, 4, 5])
np.save("my_array.npy", arr)          # save in NumPy's own format (fast, exact)
loaded = np.load("my_array.npy")

np.savetxt("my_array.csv", arr, delimiter=",")   # save as plain CSV (openable in Excel)
loaded_csv = np.loadtxt("my_array.csv", delimiter=",")


# =========================================================
# 13) PERFORMANCE NOTES
# =========================================================
# - Vectorization: always prefer direct NumPy operations (e.g. v * 6) over
#   manual for-loops — the speed difference is huge on large data.
# - Copy vs View: some operations (like basic slicing) return a VIEW, not
#   an independent copy — editing the slice can affect the original. Use
#   .copy() when you need full independence:
a = np.array([1, 2, 3])
b = a[0:2]           # view -> linked to a
c = a[0:2].copy()     # copy -> fully independent

# - dtype: keep an eye on the array's data type; convert it with .astype():
arr = np.array([1, 2, 3])
print(arr.astype(float))   # [1. 2. 3.]
