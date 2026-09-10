# Metrics reference

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

Regression: `MAE=(1/n)Σ|y−ŷ|` is target-unit and robust; `MSE=(1/n)Σ(y−ŷ)²`
penalizes large errors; `RMSE=√MSE`; and R² compares against a mean baseline and can
be negative on held-out data. Classification precision is positive-prediction
reliability, recall is positive coverage, and accuracy can mislead with imbalance.
Always state positive class, threshold, and averaging. Source mapping is
`Codes/1.3 Metrics Module` and `Confution Matrix.pptx`. Scikit-learn scorers named
`neg_mean_squared_error` are negated so larger is better: multiply by `-1` before
presenting MSE. Do not call median absolute error “median squared error.”

## Regression measures

For errors `e_i=y_i-\hat y_i`, `MAE=(1/n)Σ|e_i|` is in target units and is less
affected by one very large error. `MSE=(1/n)Σe_i²` emphasizes large errors and
`RMSE=√MSE` returns to target units. `R²=1−SSE/SST` compares with a mean-prediction
baseline; it can be negative on held-out rows and does not mean “percent correct.”
Report at least two measures when the business cost is not fully described, and show
the target scale so a reader can judge practical importance.

## Classification measures

For a declared positive class, precision answers “when we alert, how often are we
right?” and recall answers “how many actual positives did we find?” Specificity
measures negative coverage; balanced accuracy averages recall and specificity. F1 is
the harmonic mean of precision and recall and depends on the selected threshold.
Accuracy can look excellent under imbalance. ROC-AUC evaluates ranking across
thresholds, while PR-AUC focuses on positive retrieval. Always state whether
averaging is binary, macro, weighted, or micro.

## A measurement workflow

1. Define the decision and its cost, including which class is positive.
2. Select metrics before looking at the test score.
3. Compute them on validation folds consistently and include a baseline.
4. Plot residuals or threshold curves; check calibration if probabilities drive risk.
5. Report confidence intervals or repeated-fold variation where feasible.
6. Lock the metric and threshold policy before the final test evaluation.

## ⚠️ Correction notes and source map

This expands `evaluation/metrics/1.3 Metrics Module` and `Confution Matrix.pptx`.
Scikit-learn's `neg_mean_squared_error` follows its “higher is better” scorer API;
negate it before explaining MSE. The source phrase “median squared error” is
incorrect: use median absolute error when that is the intended robust statistic.
`examples/python/02_linear_regression.py` and `03_logistic_regression.py` show the
corrected measures on complete, reproducible inputs.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
