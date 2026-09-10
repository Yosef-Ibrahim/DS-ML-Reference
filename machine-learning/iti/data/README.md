# Datasets

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

`raw/` contains `houses.csv`, `satf.csv`, `heart.csv`, `Dataset_spine.csv`, and
`train.csv`, copied from source lessons with names and bytes preserved. Inspect
columns, provenance, and licensing before redistribution. Examples use deterministic
built-in data where possible so they do not depend on a working directory.

## Dataset inventory and first pass

Use `houses.csv` and `satf.csv` for regression-oriented inspection, `heart.csv` for
classification practice, `Dataset_spine.csv` for the neural-network lesson, and
`train.csv` as the retained source training table. The filenames preserve the source
material; they do not guarantee a complete data dictionary. Before modeling, print
the shape, columns, dtypes, null counts, duplicate keys, target candidates, and
representative values, then record the file hash or acquisition date.

## Safe handling

Keep `raw/` immutable. Create a documented working copy and never overwrite source
values to “fix” a parsing problem. Parse dates and numeric separators explicitly,
check units and category spelling, and distinguish a missing measurement from a
zero. Remove an identifier from model features only after retaining it for grouping
or audit. Confirm that any target or post-outcome field is unavailable at prediction
time.

Use a deployment-shaped split before fitting imputation, encoding, scaling, feature
selection, or dimensionality reduction. If a CSV contains repeated people, sites, or
time periods, use a group or chronological split. For redistribution, inspect
licensing and remove personal or sensitive data; source provenance is not permission
to publish.

## Source map and caveats

The five files are copied to `data/raw/` from the lesson materials referenced by
`iti/reference/SOURCE_INDEX.md`. `Dataset_spine.csv` is associated with
`supervised/neural-networks/2.3_NN`, while the compact runnable examples prefer
deterministic scikit-learn data. ⚠️ Do not infer a target or scientific meaning from
a filename alone, and do not report a model score until the schema and label
semantics have been verified.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
