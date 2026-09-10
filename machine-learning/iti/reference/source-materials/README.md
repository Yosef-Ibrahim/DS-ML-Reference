# Source materials and provenance

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

This directory contains direct copies of all seven root materials: three PDFs
(`Topics.pdf`, `Project General Steps.pdf`, `Overfitting.pdf`) and four PPTX lectures.
Supporting DOC lesson notes and `SkLearn_Codes.rar` are also retained. Do not edit
these copies; make corrections in guides and runnable examples. The normalized code
directories map `1.1` data loading, `1.2` cleaning, `1.3` metrics, `1.4` selection,
`1.5` scaling, `1.6` splitting, `2.1` linear, `2.2` logistic, `2.3` neural networks,
and `3.1`–`3.4` model checking through persistence.

## Reading the preserved files

These files are an immutable provenance layer. Open the PDF/PPTX when you need the
original terminology, diagrams, or lesson order; use the normalized guides for
definitions, current API behavior, and a complete workflow. The `Codes/` documents
and archive are retained to make the mapping auditable, but many snippets assume a
notebook state and should not be run in isolation.

The conceptual sequence is: data and cleaning (`1.1`, `1.2`), metrics (`1.3`),
feature selection/scaling/splitting (`1.4`–`1.6`), supervised estimators (`2.1`–`2.3`),
model checking and search (`3.1`, `3.2`), then pipelines and persistence (`3.3`,
`3.4`). `Topics.pdf` and `Project General Steps.pdf` provide the broad curriculum;
`Overfitting.pdf` supports the bias/variance and regularization discussion.

## ⚠️ Known source limitations

- Snippets may reference variables such as `X_train`, `steps`, or `SelectedModel`
  without defining them.
- Older scikit-learn examples may use removed arguments such as `normalize=True`.
- A notebook's test split may be displayed as validation data, which contaminates
  model selection.
- The original filename `Confution Matrix.pptx` is misspelled but is intentionally
  unchanged for provenance.

Use the corrected examples under `iti/examples/` and the source index for navigation.
Corrections belong in guides and examples; do not modify these source copies.

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
