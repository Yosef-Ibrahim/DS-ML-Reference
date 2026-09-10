# Model checking and hyperparameter search

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

Cross-validation repeatedly fits training folds and scores held-out folds. Use
grouped or temporal splitters when random K-fold would leak entities or time.
GridSearchCV evaluates a declared parameter grid; keep preprocessing inside the
searched Pipeline so each fold learns independently. Source mapping is
`Codes/3.1_Model_Check` and `Codes/3.2_Grid_Search`. The source's undefined
`SelectedModel`, `X`, and `y` are supplied in
`examples/python/05_model_selection_and_persistence.py`.

## What cross-validation estimates

In K-fold cross-validation, each fold trains on roughly `K−1` partitions and scores
the remaining partition. The mean summarizes expected performance under the chosen
sampling scheme and the spread shows sensitivity to the partition. Stratification
preserves class proportions; `GroupKFold` prevents entities crossing folds; a
time-series splitter preserves chronology. Choosing a random splitter for grouped or
temporal data creates optimistic leakage.

## Search workflow

1. Keep a final test set aside and choose a primary metric.
2. Put every learned preprocessing step and estimator in one `Pipeline`.
3. Declare a small, interpretable grid or distribution; include the model baseline.
4. Run `GridSearchCV`/`RandomizedSearchCV` on training data with the deployment-shaped
   splitter and inspect `cv_results_`.
5. Check the selected model for instability, calibration, and subgroup errors.
6. Freeze hyperparameters and threshold policy, refit as documented, and evaluate
   once on the untouched test set.

Search scores are not independent test scores. A large grid can overfit the folds,
and a tiny data set may need nested cross-validation or repeated folds to estimate
selection uncertainty. Do not tune a threshold on the same final test labels used
to claim performance.

## ⚠️ Correction notes and source map

The original `3.1_Model_Check` and `3.2_Grid_Search` fragments use undefined
`SelectedModel`, `X`, and `y`; the runnable
`examples/python/05_model_selection_and_persistence.py` supplies them. The
preprocessor belongs inside the searched pipeline so each fold learns statistics
from its training rows only. Record `random_state`, splitter, scoring name, grid,
and package versions for reproducibility.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
