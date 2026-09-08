# 🔎 Essential EDA Methods — A Practical Checklist

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis topics only)? Reach out using the contact info above.
>
> 📖 This is a **methods guide**, not tied to one dataset — it's the checklist to run through at the start of *any* new dataset. For a worked example applying these exact steps to a real dataset, see [`../medical-risk-eda/`](../medical-risk-eda/).

**Goal of EDA:** Quickly understand the structure, quality, and relationships in your dataset to guide cleaning, feature engineering, and modeling.

---

## 1. Quick Peek at the Data
**What:** View a small slice to sanity-check columns and values.
**Typical ops:** `df.head()`, `df.tail()`, `df.sample(k)`
**Why:** Confirms load worked, spots obvious issues (weird encodings, wrong delimiters).

---

## 2. Shape and Index
**What:** Dataset dimensions and indexing.
**Typical ops:** `df.shape`, `df.index`, `df.columns.tolist()`
**Why:** Anchors expectations (rows/columns) and helps plan transformations.

---

## 3. Types and Basic Info
**What:** Column dtypes, non-null counts, memory footprint.
**Typical ops:** `df.info()`, `df.dtypes`, `df.memory_usage(deep=True).sum()`
**Why:** Reveals parsing mistakes (numbers stored as strings), mixed types, and memory risks.

---

## 4. Summary Statistics (Numeric)
**What:** Central tendency and dispersion.
**Typical ops:** `df.describe()` (or `df.describe(percentiles=[...])`)
**Why:** Detects outliers, skew, and scale differences at a glance.

---

## 5. Missing-Values Profile
**What:** Quantity and pattern of missingness.
**Typical ops:**
```python
df.isna().sum().sort_values(ascending=False)
df.isna().mean()
```
**Why:** Guides imputation vs. dropping and flags suspicious columns (mostly null).

---

## 6. Duplicates Check
**What:** Row and key-level duplication.
**Typical ops:**
```python
df.duplicated().sum()
df.drop_duplicates(inplace=True)
```
**Why:** Prevents data leakage and inflated counts.

---

## 7. Cardinality and Categorical Summaries
**What:** Distinct values and frequency distributions.
**Typical ops:**
```python
df.nunique()
df['col'].value_counts(dropna=False).head(20)
```
**Why:** Finds ID-like columns, high-cardinality categoricals, class imbalance.

---

## 8. Correlations (Numeric ↔ Numeric)
**What:** Linear/monotonic relationships between numeric features.
**Typical ops:**
```python
df.corr(numeric_only=True, method='pearson')
```
**Why:** Spots redundant features, multicollinearity risks, and potential signals.

---

## 9. Grouped Aggregations
**What:** Split-apply-combine summaries by category/time.
**Typical ops:**
```python
df.groupby('col').agg({'y':['count','mean','median']}).sort_values(('y','mean'), ascending=False)
```
**Why:** Surfaces segment-level patterns and candidate features.

---

## 10. Outlier Scanning
**What:** Rule-of-thumb detection with IQR/z-scores.
**Typical ops:**
```python
# IQR
q1, q3 = s.quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr

# Z-score
((s - s.mean()) / s.std()).abs() > 3
```
**Why:** Identifies anomalies for capping, investigation, or removal.

---

## Helpful Add-ons
- **Type fixes:**
  `df['col'] = pd.to_numeric(df['col'], errors='coerce')`
  `pd.to_datetime(df['date_col'], errors='coerce')`
- **Categorical hygiene:**
  `str.strip()`, `str.lower()`, mapping rare levels to "Other".
- **Datetime features:**
  `.dt.year`, `.dt.month`, `.dt.dayofweek` for temporal patterns.
- **Target-aware checks:**
  Leakage detection and class balance verification.

---

## Minimal EDA Checklist
1. Load data and **peek** (`head`, `sample`).
2. Confirm **shape, columns, index**.
3. Inspect **dtypes/info/memory**; fix parsing issues.
4. Run **numeric describe** (+ custom percentiles).
5. Profile **missing values** and plan imputation.
6. Count and **remove duplicates** if needed.
7. Examine **cardinality** and **value_counts**.
8. Compute **correlation matrix** for numeric features.
9. Perform **groupby aggregations**.
10. Scan and handle **outliers**.

---

## 📬 Contributing

Have an addition, correction, or idea for this guide (ML / Data Science / Data Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
