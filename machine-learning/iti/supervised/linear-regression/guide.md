# Linear regression

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

For features `x`, linear regression predicts `ŷ = β₀ + xᵀβ` and ordinary least squares
minimizes `SSE = Σ(yᵢ − ŷᵢ)²`. `MSE = SSE/n`, `RMSE = √MSE`, and
`R² = 1 − SSE/SST`. Check linear form, independent errors, stable variance, and
collinearity; inspect residuals and error by subgroup. Report MAE, RMSE, and R²
together and compare with a baseline. `examples/python/02_linear_regression.py`
uses a StandardScaler/Ridge pipeline, correcting the obsolete source `normalize=True`.
Source mapping: `Codes/2.1_Linear_Regression`, and the one-/multiple-variable
regression PPTX files.

## Interpretation and assumptions

With an intercept, `β_j` is the expected change in the prediction for a one-unit
increase in feature `j` while the other included features stay fixed. This
interpretation depends on units and on the feature representation; standardized
coefficients are not in the original business units. Correlated features make
individual coefficients unstable even when predictions remain useful.

Ordinary least squares is most transparent when the conditional mean is
approximately linear, residuals are independent, and variance is reasonably stable.
Normal residuals are useful for some classical intervals but are not a requirement
for producing predictions. Plot residuals against fitted values and time, inspect
high-leverage observations, and compare error across meaningful groups.

## Practical workflow

1. Define the numeric target and a baseline that predicts the training mean.
2. Split before imputation, scaling, feature selection, or target transformations.
3. Fit a `LinearRegression` baseline, then compare Ridge or Lasso when features are
   numerous or collinear.
4. Report MAE, RMSE, and `R²` on the same held-out rows; include target units.
5. Inspect residual plots and the largest absolute errors, not only the aggregate.
6. Use cross-validation to select regularization, then fit the chosen pipeline and
   evaluate the test set once.

Ridge minimizes `SSE + α||β||²`; Lasso minimizes `SSE + α||β||₁`. Increasing `α`
shrinks coefficients and can reduce variance, but it does not repair leakage or
omitted-variable bias. `R²` can be negative on held-out data when a model is worse
than the mean baseline, and it should not be compared across different targets
without context.

## ⚠️ Correction notes and source map

The source `normalize=True` argument in older scikit-learn examples is obsolete.
Scale explicitly in a pipeline when using Ridge/Lasso; do not scale the target unless
you also define how to invert predictions. The complete companion is
`examples/python/02_linear_regression.py` and its notebook. It supplies data and
splits that the fragments in `2.1_Linear_Regression` leave implicit. See also
`Lec2 Linear regression with one variable.pptx` and `Lec3 linear regression with
multiple vars.pptx` in `iti/reference/source-materials/`.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
