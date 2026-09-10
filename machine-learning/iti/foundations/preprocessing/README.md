# Preprocessing guide

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

Parse types explicitly, quantify missingness, remove duplicates only when they are
truly duplicate observations, and investigate outliers with domain context. Feature
selection may be filter, wrapper, or embedded; selection must be fitted inside
cross-validation. Scaling helps distance-, gradient-, and regularization-based
models, while trees usually do not require it. Use stratified, grouped, or temporal
splits when the deployment setting requires them.

## Transformation order

Begin with a schema and a split, then assign each column a role. Numeric values can
be imputed and optionally scaled; categorical values can be imputed and encoded;
free-text, IDs, and target-derived columns need a deliberate policy. Fit every
learned operation on `X_train` only and apply the frozen operation to validation,
test, and future data. A `ColumnTransformer` makes this contract explicit for mixed
tables.

Feature selection is a modeling decision. Filter methods rank a feature without an
estimator (for example, correlation or mutual information); wrapper methods search
subsets using a model; embedded methods select during fitting (for example, L1
regularization or tree importance). Use a pipeline so selection is repeated inside
each cross-validation fold. A feature that predicts the target after the event is
leakage, even if it is statistically useful.

## Step-by-step checklist

1. Profile missingness, duplicates, impossible ranges, and category spelling.
2. Decide whether an outlier is an error, a rare valid case, or a regime change.
3. Split using the deployment unit (row, group, or time).
4. Fit imputers, encoders, scalers, and selectors on training rows.
5. Inspect the transformed feature count and sparsity; keep feature names when useful.
6. Refit only through the pipeline during validation and persist the fitted pipeline.

Standardization uses `z=(x-μ_train)/σ_train`; guard against zero variance. Min–max
scaling uses training extrema and can be distorted by extreme values. Robust scaling
uses median and interquartile range but does not fix contaminated labels. Trees are
scale-insensitive in split selection, whereas k-nearest neighbors, SVMs, neural
networks, and regularized linear models usually are not.

## ⚠️ Correction notes and source map

The numbered lessons `1.2 Data Cleaning`, `1.4_Feature_Selection`,
`1.5_Data_Scaling`, and `1.6_Data_Split` are preserved under the matching
subdirectories. Their short fragments may fit transformations before a demonstrated
split or use pre-existing variables; the safe rule here is split first and pipeline
the operation. The complete companion is
`examples/python/01_end_to_end_workflow.py`. Never treat deletion of an outlier or
duplicate as universally correct; document the reason and its effect on the target.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
