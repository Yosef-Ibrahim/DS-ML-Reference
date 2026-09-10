# Statistics Reference for Data Science

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

> Source map: all eleven original lessons are preserved in [`pdfs/`](./pdfs/).
> The guide moves from describing a dataset to measuring relationships and
> fitting a regression line.

## Source-by-source map

| Source | Coverage |
|---|---|
| [`01-introduction.pdf`](./pdfs/01-introduction.pdf) | Contingency tables, frequencies, marginal/conditional proportions, percentages, and introductory scatterplots. |
| [`02-graphs.pdf`](./pdfs/02-graphs.pdf) | Variable types plus pie, bar, dot, histogram, and box plots; mean, median, mode, and normal shape. |
| [`03-interquartile-range.pdf`](./pdfs/03-interquartile-range.pdf) | Range, quartiles, percentiles, boxplot anatomy, IQR, and 1.5-IQR fences. |
| [`04-variance-and-standard-deviation.pdf`](./pdfs/04-variance-and-standard-deviation.pdf) | Sample variance and standard deviation with worked values. |
| [`05-z-scores.pdf`](./pdfs/05-z-scores.pdf) | Standardization, normal curves, empirical-rule regions, and percentile interpretation. |
| [`06-correlation.pdf`](./pdfs/06-correlation.pdf) | Scatterplot direction/strength and the warning that correlation is not causation. |
| [`07-pearson-correlation.pdf`](./pdfs/07-pearson-correlation.pdf) | Pearson `r`, its `[-1,1]` range, standardized-value formula, and a strong-positive example. |
| [`08-regression-line.pdf`](./pdfs/08-regression-line.pdf) | `y=a+bx`, residuals, and least-squares minimization. |
| [`09-regression-analysis.pdf`](./pdfs/09-regression-analysis.pdf) | Building equations, predictions, residual comparison, slope, and intercept interpretation. |
| [`10-best-fitting-regression.pdf`](./pdfs/10-best-fitting-regression.pdf) | Extended ordinary-least-squares lesson with candidate lines, residuals, and predictions. |
| [`11-regression-example.pdf`](./pdfs/11-regression-example.pdf) | End-to-end data table, scatterplot, correlation, least-squares line, predictions, and residuals. |

## 1. Describing data

Statistics begins by identifying the population, sample, variables, units, and
measurement scale. A mean is sensitive to extreme values; a median is more
robust. Always report the unit and the number of observations.

Choose a graph based on the question:

| Question | Useful display |
|---|---|
| How are numeric values distributed? | Histogram, density curve, box plot |
| How do categories compare? | Bar chart with counts or rates |
| How do two numeric variables move together? | Scatter plot |
| How does a measure change over time? | Line chart |

## 2. Quartiles and IQR

The median splits ordered data into two halves. `Q1` is the lower quartile and
`Q3` is the upper quartile. The interquartile range is:

```text
IQR = Q3 - Q1
lower fence = Q1 - 1.5*IQR
upper fence = Q3 + 1.5*IQR
```

Values outside the fences are candidates for investigation, not automatic
errors. An unusual but valid transaction should not be deleted just because it
is statistically uncommon.

## 3. Variance and standard deviation

Population variance is `σ² = Σ(xi-μ)² / N`. Sample variance commonly uses
`s² = Σ(xi-x̄)² / (n-1)` to correct finite-sample bias. Standard deviation is
the square root of variance and therefore has the same unit as the data.

⚠️ **Correction:** Mixing the population denominator `N` and the sample
denominator `n-1` in one analysis makes comparisons misleading. Choose the
definition according to whether the data is the complete population or a sample.

The source filenames contain spelling corrections: `InterQualtile` is
**interquartile** and `Varience` is **variance**. The slides also alternate
sample and population symbols; this guide states the denominator explicitly.

## 4. Z-scores

```text
z = (x - mean) / standard_deviation
```

A z-score measures distance from the mean in standard-deviation units. It is
useful for comparing variables on different scales, but it is not automatically
normally distributed and should not be treated as an outlier verdict without
context.

## 5. Correlation

Covariance describes joint movement but depends on units. Pearson correlation
standardizes covariance:

```text
r = cov(X,Y) / (sx * sy)
```

`r` lies between -1 and 1. A value near 1 indicates a strong positive linear
association; near -1 indicates a negative linear association; near zero means
little *linear* association. Nonlinear relationships can still have a Pearson
value near zero.

⚠️ **Correction:** Correlation is not causation. Confounding, selection bias,
reverse causality, and common time trends can all create an association.

## 6. Regression line

Simple linear regression models:

```text
y_hat = b0 + b1*x
b1 = Σ((xi-x̄)(yi-ȳ)) / Σ((xi-x̄)²)
b0 = ȳ - b1*x̄
```

The slope is the expected change in the response for one unit of the predictor
under the model. The intercept is mathematically required but may not have a
meaningful real-world interpretation when zero is outside the observed range.

## 7. Regression analysis and diagnostics

Residuals are `ei = yi - y_hat_i`. Inspect residual plots for non-linearity,
unequal variance, influential observations, and time dependence. Useful metrics
include MAE, MSE, RMSE, and `R²`; no single metric replaces a diagnostic plot.

For multiple regression, adding predictors can increase training `R²` even when
they do not generalize. Use a held-out test set or cross-validation, and avoid
including features that would only become available after the prediction time.

The three regression decks overlap intentionally: file 8 introduces the line,
file 9 develops the calculations, file 10 expands least squares, and file 11
walks through a complete example. Read them in that order rather than treating
the repetition as new formulas.

## 8. How this supports machine learning

- IQR and z-scores support anomaly investigation and feature cleaning.
- Standardization helps distance-based models, PCA, and gradient optimization.
- Correlation is an exploratory clue, not a feature-selection guarantee.
- Regression is both a statistical model and a supervised-learning baseline.
- Graphs reveal leakage, non-linearity, imbalance, and heteroscedasticity.

## 9. Practical checklist

1. Define the population, sample, unit, and prediction question.
2. Plot before calculating a single summary.
3. Report sample size, center, spread, and missingness.
4. Investigate outliers instead of deleting them blindly.
5. Check whether correlation is linear and whether a confounder is plausible.
6. Split data by time or entity when random splitting would leak information.
7. Validate residuals and generalization, not only training fit.

The companion [`statistics_examples.py`](./statistics_examples.py) computes
quartiles/IQR, sample standard deviation, z-scores, Pearson correlation, and a
least-squares line without external data or third-party packages. The notebook
[`statistics_examples.ipynb`](./statistics_examples.ipynb) provides the same
reproducible calculations as cells.

## 📬 Contributing

Have an addition, correction, or idea for this guide (ML / Data Science / Data
Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
