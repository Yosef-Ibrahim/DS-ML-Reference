# Data loading and inspection

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

The copied `1.1 Data` files demonstrate scikit-learn datasets. A dataset is commonly
`X ∈ R^(n×p)` and `y ∈ R^n`. Print shape, feature names, target names, dtypes, class
counts, and a small sample before modeling. `examples/python/01_end_to_end_workflow.py`
and `examples/notebooks/01_data_loading.ipynb` provide a complete Iris workflow;
the numbered source snippets remain preserved beside this guide.

## What “loading” includes

Loading is more than calling `read_csv`. Establish where the bytes came from, which
row is an observation, what the target means, and whether a column is known at
prediction time. For a scikit-learn bundle, inspect `data`, `target`,
`feature_names`, and `target_names`; for a CSV, inspect headers, delimiter, encoding,
units, and an explicit target column. Keep raw values immutable and create a
working copy for cleaning.

## Step-by-step audit

1. Locate the file relative to the project, not the current shell directory.
2. Load with an explicit parser configuration and parse dates deliberately.
3. Print shape, `head`, dtypes, null counts, unique counts, and descriptive ranges.
4. Check that the target is present, aligned with features, and not accidentally
   included in `X`.
5. Record class counts or target quantiles and inspect representative rows.
6. Save the schema and provenance before applying any transformation.

For a classification target with counts `n_k`, the empirical class proportion is
`n_k / n`. A large imbalance is not itself an error, but it changes baseline metrics,
split strategy, and threshold decisions. For regression, examine units and the range
of `y`; a model can have a small average error while failing at an important extreme.

## Practical use and caveats

Use deterministic built-in datasets when teaching APIs, and use the copied CSVs in
`iti/data/raw/` when practicing provenance and schema checks. Do not silently coerce
non-numeric text to zero. Do not drop rows merely because a parser reports nulls:
first determine whether the missingness is a data-collection event. If a CSV has a
date or entity key, preserve it for splitting even if it is not a model feature.

## ⚠️ Correction notes

- The source snippets assume that `X` and `y` already exist; they are not standalone
  loaders.
- A feature name list is metadata, not proof that columns have the expected order.
- Inspecting the test set is acceptable for a final audit, but using its statistics to
  choose preprocessing or a model leaks information.

## Source mapping

This guide expands `foundations/data-loading/1.1 Data` and the original `Codes/1.1
Data` lesson. Compare it with `examples/python/01_end_to_end_workflow.py` and
`examples/notebooks/01_data_loading.ipynb`; those companions define every object and
show an Iris load-to-inspection sequence.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
