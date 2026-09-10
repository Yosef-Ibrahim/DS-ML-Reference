"""Small standard-library-only examples matching the Linear Algebra guide."""

from math import acos, cos, degrees, pi, sin, sqrt


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def solve_2x2(matrix, rhs):
    (a, b), (c, d) = matrix
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("singular matrix has no unique solution")
    return ((rhs[0] * d - b * rhs[1]) / determinant,
            (a * rhs[1] - rhs[0] * c) / determinant)


u, v = (3, 4), (4, 0)
dot = sum(a * b for a, b in zip(u, v))
angle = degrees(acos(dot / (sqrt(25) * sqrt(16))))
print(f"dot(u, v)={dot}; angle={angle:.1f} degrees")

A, b = ((2, 1), (1, -1)), (7, 1)
x = solve_2x2(A, b)
print("solution to Ax=b:", x)
print("verification:", matvec(A, x))

theta = pi / 2
rotation = ((cos(theta), -sin(theta)), (sin(theta), cos(theta)))
print("90-degree rotation of (1, 0):", matvec(rotation, (1, 0)))
