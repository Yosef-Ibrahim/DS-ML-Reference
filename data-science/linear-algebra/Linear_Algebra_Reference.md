# Linear Algebra Reference for Data Science

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

> Source map: the seven original lessons are preserved in [`pdfs/`](./pdfs/).
> This guide reorganizes them into a numbered explanation and adds the
> machine-learning interpretation that is usually missing from slide-only notes.

## Source-by-source map

| Source | Coverage |
|---|---|
| [`01-linear-equations.pdf`](./pdfs/01-linear-equations.pdf) | Slope, point-slope form, and horizontal/vertical lines. |
| [`02-vectors-part-1.pdf`](./pdfs/02-vectors-part-1.pdf) | Vector coordinates, operations, dot product, angles, and scalar projection. |
| [`03-vectors-part-2.pdf`](./pdfs/03-vectors-part-2.pdf) | Linear systems, augmented matrices, and scaling/rotation/reflection/shear transformations. |
| [`04-matrices.pdf`](./pdfs/04-matrices.pdf) | Matrix dimensions, special matrices, transpose, operations, multiplication, and determinants. |
| [`05-solving-linear-equations-matrix-inverse.pdf`](./pdfs/05-solving-linear-equations-matrix-inverse.pdf) | `Ax=b`, Gaussian elimination, row operations, and matrix inverses. |
| [`06-special-cases-linear-systems.pdf`](./pdfs/06-special-cases-linear-systems.pdf) | Consistency, unique/no/infinite solutions, and transformation matrices. |
| [`07-eigenvectors.pdf`](./pdfs/07-eigenvectors.pdf) | Characteristic equations, eigenvalues, eigenvectors, and complex roots. |

The filename of file 3 says vectors, but the deck also introduces systems and
transformations; read it after vector basics. File 4 includes the 2x2
determinant `ad-bc`; its explanations are terse, so use the worked examples
with the formulas below.

## Table of contents

1. [Equations and systems](#1-equations-and-systems)
2. [Vectors](#2-vectors)
3. [Matrices](#3-matrices)
4. [Solving `Ax=b`](#4-solving-axb)
5. [Special cases and rank](#5-special-cases-and-rank)
6. [Eigenvalues and eigenvectors](#6-eigenvalues-and-eigenvectors)
7. [Machine-learning connections](#7-machine-learning-connections)
8. [Numerical safety checklist](#8-numerical-safety-checklist)

## 1. Equations and systems

A linear equation has variables only to the first power. A single equation
describes a line in two dimensions; two independent equations can intersect at
one point. For a system:

```text
a11*x1 + a12*x2 = b1
a21*x1 + a22*x2 = b2
```

the geometric interpretation is more useful than memorizing elimination:
parallel distinct lines have no solution, intersecting lines have one solution,
and coincident lines have infinitely many solutions.

## 2. Vectors

A vector is an ordered magnitude with direction:

```text
x = [x1, x2, ..., xn]^T
```

Important operations:

- Addition is component-wise.
- Scalar multiplication changes magnitude and possibly direction.
- The dot product is `x · y = Σ xi yi`; it measures alignment.
- Euclidean length is `||x||2 = sqrt(x · x)`.
- Cosine similarity is `(x · y)/(||x|| ||y||)` when both vectors are non-zero.
- Scalar projection of `u` onto `v` is `(u · v)/||v||`; the vector projection is
  `((u · v)/(v · v))v`.

In machine learning a row of features is a vector, model weights are a vector,
and a prediction often begins with a dot product.

## 3. Matrices

A matrix is a rectangular arrangement of numbers. If `A` has `m` rows and `n`
columns, it maps an `n`-dimensional vector into an `m`-dimensional vector.

```text
A = [a11 a12]       A*x is a linear transformation
    [a21 a22]
```

Matrix multiplication is valid only when the inner dimensions match. It is
generally not commutative: `AB` and `BA` can have different shapes or values.
The transpose swaps rows and columns. The identity matrix leaves a compatible
vector unchanged.

For `A=[[a,b],[c,d]]`, `det(A)=ad-bc`. If the determinant is nonzero,
`A^-1 = (1/(ad-bc))*[[d,-b],[-c,a]]`; otherwise no inverse exists.

## 4. Solving `Ax=b`

Writing a system as `Ax=b` makes the structure explicit:

- `A` stores coefficients.
- `x` stores unknowns.
- `b` stores observations or targets.

For a square, non-singular matrix, `x=A^-1 b` is mathematically valid. In
production numerical code, do not calculate an explicit inverse just to solve a
system; use a factorization or a solver because it is usually faster and more
stable. Gaussian elimination applies row operations until the solution is
visible.

## 5. Special cases and rank

The determinant is useful for a square matrix, but rank gives the broader
explanation:

| Condition | Meaning |
|---|---|
| `rank(A) = rank([A|b]) = number of variables` | One unique solution |
| `rank(A) = rank([A|b]) < number of variables` | Infinitely many solutions |
| `rank(A) != rank([A|b])` | No solution |

⚠️ **Correction:** A zero determinant is not itself a complete classification of
every system. It says the square coefficient matrix is singular; consistency
still depends on the augmented matrix and the right-hand side.

## 6. Eigenvalues and eigenvectors

An eigenvector keeps its direction under a transformation:

```text
A v = λ v
```

The scalar `λ` is the eigenvalue. Non-zero solutions satisfy:

```text
det(A - λI) = 0
```

Eigenvectors are not unique in scale: if `v` is an eigenvector, any non-zero
multiple of `v` is also one. Repeated eigenvalues may have fewer independent
eigenvectors than their multiplicity, so a matrix is not automatically
diagonalizable.

The source uses inconsistent point/symbol notation in places. This guide uses
`A`, `v`, and `λ` consistently. “Flipping” is called **reflection**, and a
zero determinant is not by itself a solution classification: inspect the
augmented matrix to distinguish no solution from infinitely many solutions.

## 7. Machine-learning connections

1. **Linear regression:** predictions are `Xw + b`; least squares minimizes
   `||Xw-y||²`.
2. **Neural networks:** every dense layer performs a matrix-vector operation
   followed by a non-linear activation.
3. **PCA:** principal directions are eigenvectors of a covariance matrix; the
   largest eigenvalues identify directions with greatest variance.
4. **Embeddings:** vectors allow similarity search, clustering, and distance-based
   models.
5. **Optimization:** gradients are vectors and Hessians are matrices describing
   curvature.

## 8. Numerical safety checklist

- Check dimensions before multiplying.
- Prefer `solve(A, b)` to explicitly computing `inv(A) @ b`.
- Inspect the condition number when a system is nearly singular.
- Treat values close to zero with a tolerance, not exact equality.
- Standardize features when scale differences distort distance or optimization.
- Keep a symbolic/manual derivation for small examples and a numerical test for
  the implementation.

The companion [`linear_algebra_examples.py`](./linear_algebra_examples.py) uses
only Python's standard library to verify a dot product, solve a 2x2 system, and
apply a rotation. The notebook
[`linear_algebra_examples.ipynb`](./linear_algebra_examples.ipynb) presents the
same calculations interactively.

## 📬 Contributing

Have an addition, correction, or idea for this guide (ML / Data Science / Data
Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
