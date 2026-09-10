# Logistic regression

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

Binary logistic regression uses `p(y=1|x) = σ(β₀+xᵀβ)` with
`σ(z)=1/(1+e^-z)` and log loss `−[y log p+(1−y)log(1−p)]`. A 0.5 threshold is a
decision policy, not a law. Report TP/TN/FP/FN, precision, recall, specificity,
F1, ROC-AUC, and PR-AUC when positives are rare; calibrate probabilities when risk
estimates drive decisions. `examples/python/03_logistic_regression.py` is complete.
Source mapping: `Codes/2.2_Logistic_Regression`, `Lec4 logistic regression.pptx`,
and the source file retained as `Confution Matrix.pptx`. Scale features and set
adequate `max_iter`, correcting fragile old solver snippets.

## From score to decision

The linear score `z=β₀+xᵀβ` becomes a probability through
`σ(z)=1/(1+e^{-z})`. Training commonly minimizes mean binary cross-entropy, which
penalizes confident wrong predictions. The sign and size of `β_j` describe a change
in log-odds, not a fixed probability change; the probability effect depends on the
starting score and the other features.

Choose a threshold on validation data using the application cost. At threshold `t`,
predict positive when `p≥t`; `t=0.5` is only a default. Lowering `t` usually increases
recall and false positives. Report the threshold, positive label, and confusion
matrix:

| actual / predicted | negative | positive |
|---|---:|---:|
| negative | TN | FP |
| positive | FN | TP |

Precision is `TP/(TP+FP)`, recall is `TP/(TP+FN)`, specificity is `TN/(TN+FP)`,
and `F1=2PR/(P+R)`. ROC-AUC ranks scores over thresholds; PR-AUC is often more
informative when positives are rare. A calibrated probability can support expected
cost decisions, but a good AUC does not guarantee calibration.

## Step-by-step practice

1. Stratify a train/test split and inspect the positive rate.
2. Scale numeric features inside a pipeline and set a sufficient `max_iter`.
3. Use cross-validation on training rows to compare regularization and class weights.
4. Inspect threshold curves, calibration, and subgroup confusion matrices.
5. Pick the policy on validation data, lock it, and score the test set once.

## ⚠️ Correction notes and source map

The complete companion is `examples/python/03_logistic_regression.py` and
`examples/notebooks/03_logistic_regression.ipynb`; source fragments in
`2.2_Logistic_Regression` may omit the split and imports. Compare with
`Lec4 logistic regression.pptx` and `Confution Matrix.pptx` (the original filename
spelling is retained). Do not call accuracy sufficient for an imbalanced target,
and do not use test labels repeatedly to tune `t`, class weights, or features.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
