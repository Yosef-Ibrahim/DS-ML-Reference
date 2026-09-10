# 🧪 MLflow Workshops — Experiment Tracking, Models, and Promotion

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *MLflow workshops* course material (Rowad Misr Al-Raqmeya).
>
> 📌 *Format Note:* The companion `.py` and `.ipynb` files use only Python's standard library, so they execute without an MLflow installation or credentials. Production notes show where the real MLflow client fits.

---

## 📑 Table of Contents
1. [Why MLflow](#1-why-mlflow)
2. [The MLflow Object Model](#2-the-mlflow-object-model)
3. [Workshop 1: Reproducible Tracking](#3-workshop-1-reproducible-tracking)
4. [Workshop 2: Model Packaging](#4-workshop-2-model-packaging)
5. [Workshop 3: Promotion and Serving](#5-workshop-3-promotion-and-serving)
6. [Production Checklist](#6-production-checklist)

---

## 1) Why MLflow

An experiment is not reproducible when only the final score is saved. A useful record connects the **code version**, **data version**, **parameters**, **metrics**, **artifacts**, and **model signature**. MLflow supplies common APIs and a tracking server; the local companion demonstrates the same record shape with JSON.

Tracking solves four recurring problems:

1. Comparing runs without copying notebook cells.
2. Finding the exact parameters behind a result.
3. Storing a model with its input/output contract.
4. Promoting a tested artifact through environments with an audit trail.

---

## 2) The MLflow Object Model

| Object | Meaning | Examples |
|---|---|---|
| Experiment | Logical collection of related runs | `customer_churn` |
| Run | One execution of training/evaluation | parameters, metrics, tags |
| Parameter | Input chosen before or during training | `learning_rate=0.1` |
| Metric | Numeric result, often tracked over steps | `validation_rmse=2.4` |
| Artifact | File produced by a run | model, plot, report |
| Model signature | Input/output schema | columns and types |
| Registered model | Named versioned model in a registry | `fraud_model` v3 |

Use parameters for configuration, metrics for measured outcomes, and artifacts for files. Do not place large datasets or credentials in tags or parameters.

---

## 3) Workshop 1: Reproducible Tracking

### A minimal run contract

```python
with mlflow.start_run() as run:
    mlflow.log_params({"seed": 7, "regularization": 0.1})
    mlflow.log_metrics({"validation_accuracy": 0.92})
    mlflow.set_tags({"data_version": "orders-2026-09-10", "team": "analytics"})
    mlflow.log_artifact("model.json")
```

Before logging, define:

1. A stable experiment name.
2. A run name that explains the trial.
3. A seed and environment lock.
4. A data snapshot or immutable table version.
5. A primary metric and whether higher or lower is better.

The local companion writes one JSON document per run to a temporary directory, calculates a deterministic linear-model example, and prints the run summary. It is intentionally not a replacement for a tracking server.

### Comparing runs

Compare runs on the same evaluation split and metric definition. Filter by tags such as data version and code revision before ranking. A higher score from a different split is not evidence of a better model.

---

## 4) Workshop 2: Model Packaging

An MLflow model is more than a serialized estimator:

* **Flavor:** How the model is loaded (for example, scikit-learn or Python).
* **Artifacts:** Serialized model and supporting files.
* **Signature:** Expected columns, types, and outputs.
* **Input example:** A small valid request for testing.
* **Environment:** Python and dependency requirements.

A signature catches interface errors before deployment:

```text
input:  age: integer, income: double, country: string
output: probability: double
```

Avoid embedding environment-specific paths. Package preprocessing with the model or version it separately and ensure training and serving use the same feature transformations.

---

## 5) Workshop 3: Promotion and Serving

A registry separates **training** from **promotion**. A safe lifecycle is:

```text
candidate -> validation -> staging -> approval -> production -> archived
```

Promotion gates should include:

1. Schema and signature compatibility.
2. Evaluation on a fixed holdout set.
3. Bias, drift, and data-quality checks appropriate to the use case.
4. Latency and resource limits.
5. Rollback to the previous production version.

For a real MLflow deployment, configure the tracking URI explicitly, store artifacts in durable controlled storage, restrict registry permissions, and never use a local filesystem backend as the shared production system. A serving endpoint should validate input, emit request/model version metadata, and avoid logging sensitive feature values.

---

## 6) Production Checklist

- [ ] Every run records code, data, environment, parameters, and metrics.
- [ ] Metric definitions and evaluation splits are versioned.
- [ ] Artifacts are immutable and access-controlled.
- [ ] Model signatures are tested with valid and invalid requests.
- [ ] Registry transitions require an accountable approval.
- [ ] Production inference logs model version and latency without leaking PII.
- [ ] Drift and quality monitors have thresholds and owners.
- [ ] Rollback and retention policies have been exercised.

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
