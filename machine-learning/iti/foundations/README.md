# Foundations

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

## Learning objectives

Represent observations as a feature matrix `X` and target `y`; inspect types, missing
values, duplicates, ranges, and class balance; and apply transformations only after
the training split. The complete workflow is:

`question → data contract → exploration → split → train-only preprocessing → model → evaluation → artifact`.

For a vector `x`, standardization is `z = (x - μ_train) / σ_train`; min–max scaling is
`x' = (x - min_train) / (max_train - min_train)`. Statistics are learned on training
data only.

`data-loading/` maps to `Codes/1.1 Data`; the preprocessing subdirectories map to
`Codes/1.2` and `Codes/1.4`–`1.6`. Source fragments assume variables already exist.
Split first, fit transformers only on `X_train`, and transform validation/test with
the fitted transformer. Never fit imputation, scaling, or selection on the full data.

## A repeatable foundations workflow

1. **Write a data contract.** Name each column, its type and unit, whether it is
   available at prediction time, and the permitted target values.
2. **Inspect before changing.** Check `shape`, dtypes, null counts, duplicate keys,
   ranges, label balance, and a few raw rows. A surprising value is a question, not
   an automatic outlier.
3. **Define the split.** Hold out validation/test rows before learning imputation,
   category vocabularies, scale parameters, or feature-selection thresholds.
4. **Transform by column role.** Numeric columns may be imputed and scaled; categorical
   columns may be imputed and one-hot encoded; identifiers are usually excluded.
5. **Recheck invariants.** Confirm row counts, feature names, finite values, and target
   alignment after every transformation.

## Concepts to carry forward

The matrix notation `X ∈ R^(n×p)` means that rows are observations and columns are
features; it does not imply that every column is numeric or independent. A training
statistic such as `μ_train` is an estimate, not a property of the whole population.
For sparse one-hot matrices, centering can destroy sparsity, so choose a scaler and
model that respect the representation. Scaling is essential for distances and many
gradient methods, but it does not make a biased sample representative.

## Practical checks and caveats

Use a grouped split when the same patient, customer, or device appears repeatedly;
otherwise the model can memorize an identity. For time data, never let a future row
influence a past prediction. Treat missingness as potentially informative, but do not
invent a meaning for a missing value without domain evidence. Keep a transformation
report (fit rows, columns removed, imputation policy, and random seed) beside the
model so another learner can reproduce it.

## ⚠️ Correction notes

The short numbered fragments may assume that arrays, fitted transformers, or imports
already exist. They are lesson excerpts rather than complete programs. In
particular, fitting imputation, scaling, or feature selection before the split leaks
information from held-out rows; use the train-only workflow above and the runnable
example instead.

## Source map

Read [`data-loading/guide.md`](data-loading/guide.md) with `1.1 Data`, then compare
the cleaning, selection, scaling, and split subdirectories with `1.2 Data Cleaning`,
`1.4_Feature_Selection`, `1.5_Data_Scaling`, and `1.6_Data_Split`. The corrected
end-to-end example is `examples/python/01_end_to_end_workflow.py`; the numbered
files may omit imports and variable definitions.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
