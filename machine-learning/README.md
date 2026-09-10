# Machine Learning Track

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

## Purpose

This is the single entry point for all machine-learning material. It has two
clearly separated curricula:

```text
machine-learning/
├── iti/             # Classical Machine Learning ITI curriculum
│   ├── foundations/
│   ├── supervised/
│   ├── unsupervised/
│   ├── evaluation/
│   ├── projects/
│   ├── examples/
│   ├── data/
│   └── reference/
└── deep-learning/   # ANN and CNN curriculum
    ├── ann/
    ├── cnn/
    └── reference/
```

The supplied source folders were converted into this single public track and
the duplicate root-level copies were removed after the conversion. Preserved
PDFs, slide decks, datasets, notebooks, and source indexes live beside the
normalized guides under `reference/`, `data/`, and the topic directories. This
keeps the repository easy to navigate while retaining source filenames and
credit information.

## Curriculum map

| Stage | Directory | Outcomes | Main source mapping |
|---|---|---|---|
| 1. Foundations | [`iti/foundations/`](./iti/foundations/) | Load, clean, select, scale, and split data without leakage | `Codes/1.1`–`1.6` |
| 2. Supervised learning | [`iti/supervised/`](./iti/supervised/) | Fit and interpret regression, classification, and neural-network models | `Codes/2.1`–`2.3`; regression/classification lectures |
| 3. Evaluation and delivery | [`iti/evaluation/`](./iti/evaluation/) | Choose metrics, cross-validate, tune, pipeline, and persist models | `Codes/1.3`, `3.1`–`3.4`; overfitting/confusion-matrix references |
| 4. Unsupervised learning | [`iti/unsupervised/`](./iti/unsupervised/) | Understand clustering and dimensionality reduction | Corrected roadmap and examples |
| 5. Projects | [`iti/projects/`](./iti/projects/) | Turn a question into a reproducible validated deliverable | `Project General Steps.pdf` |
| 6. Deep Learning | [`deep-learning/`](./deep-learning/) | Learn ANN, CNN, training, regularization, and image workflows | ANN/CNN sessions |

## Run examples

From `machine-learning/iti/`:

```powershell
python examples\python\01_end_to_end_workflow.py
python examples\python\02_linear_regression.py
python examples\python\03_logistic_regression.py
python examples\python\04_unsupervised_basics.py
python examples\python\05_model_selection_and_persistence.py
```

The examples use deterministic scikit-learn data or copied CSVs and require no network
access. Install `numpy`, `pandas`, `scikit-learn`, `joblib`, and `jupyter` to execute
them. Syntax and JSON validation do not execute notebooks.

## How to use this curriculum

Work through the stages in order, but treat the map as a set of experiments rather
than a list of APIs to memorize. For every exercise, write a one-sentence question,
identify the unit of observation, and record the target and the cost of a wrong
prediction. Then make a small, documented split and establish a trivial baseline
(the mean for regression or the majority class for classification). Only after that
should a more complex estimator earn its place.

The normal loop is:

1. **Load and audit:** read the schema, units, missing values, duplicates, and
   target distribution; preserve a copy of the raw data.
2. **Split for the real world:** use stratification for class proportions, groups for
   repeated people/devices, or chronological order for forecasting.
3. **Build a train-only transform:** impute, encode, scale, and select features inside
   a `Pipeline` or `ColumnTransformer`.
4. **Fit and compare:** use a baseline and a small number of justified models; track
   the same metric on the same folds.
5. **Inspect errors:** examine residuals, confusion matrices, calibration, and
   subgroup performance rather than relying on one headline score.
6. **Freeze and communicate:** evaluate the untouched test set once, save the complete
   pipeline, and document assumptions, versions, and limitations.

## Suggested checkpoints

After Foundations, you should be able to explain why fitting a scaler before a split
leaks information. After Supervised learning, explain a coefficient or probability
threshold in the language of the application. After Evaluation, reproduce a selected
model from a clean process and distinguish validation decisions from a final test
estimate. The Unsupervised and Projects stages are intentionally open-ended: success
requires a defensible interpretation and a reproducible report, not a preferred
cluster count.

## Reading source material critically

The numbered directories are preserved teaching evidence, not guaranteed production
code. A snippet that uses `X_train`, `steps`, or `SelectedModel` without defining it
is a fragment to complete, not a command to paste. Prefer the runnable examples when
checking syntax, and use each topic guide's source map to jump back to the original
DOC, PDF, or PPTX. The guides explicitly mark corrections for old scikit-learn
arguments, leakage-prone validation, and sign conventions in scorer names.

## ⚠️ Correction notes

- The numbered snippets sometimes reference undefined objects such as `X_train`,
  `steps`, or `SelectedModel`; use the runnable examples for complete setup.
- Replace obsolete arguments such as `normalize=True` with an explicit pipeline.
- Treat negative `neg_*` scorer values as a scikit-learn convention and convert them
  before presenting a loss to readers.
- Never use a test split as validation while selecting a model or threshold.

## Source and correction policy

`reference/source-materials/` is a byte-for-byte copy of all root PDFs/PPTX and the
supporting DOC/RAR files. `data/raw/` contains the five useful CSV datasets. Topic
guides state source mapping and call out incomplete snippets. In particular, source
snippets use undefined placeholders such as `X_train`, `y_train`, `steps`, and
`SelectedModel`; they are teaching fragments, not standalone programs. Runnable
examples define every object. The deprecated `normalize=True` argument is replaced by
an explicit `StandardScaler` pipeline, and negative scikit-learn loss scores are
converted to positive losses before interpretation.

## Validation

```powershell
python -m compileall -q examples foundations supervised evaluation
python -c "import json, pathlib; [json.load(open(p, encoding='utf-8')) for p in pathlib.Path('examples/notebooks').rglob('*.ipynb')]"
```

---

## 📬 Contributing

Have a correction, exercise, or clearer explanation to contribute?

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
