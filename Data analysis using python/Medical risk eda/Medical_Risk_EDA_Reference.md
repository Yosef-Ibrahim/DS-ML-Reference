# 🩺 Medical Risk Factors — Exploratory Data Analysis (EDA)

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis topics only)? Reach out using the contact info above.
>
> 📁 This project uses `medical_data.csv` (included in this folder).

---

## 📑 Table of Contents
1. [About This Dataset](#1-about-this-dataset)
2. [Loading & Peeking at the Data](#2-loading--peeking-at-the-data)
3. [Initial Inspection](#3-initial-inspection)
4. [Univariate Analysis — Numeric](#4-univariate-analysis--numeric-distributions)
5. [Univariate Analysis — Categorical](#5-univariate-analysis--categorical-distributions)
6. [Bivariate Analysis — Numeric vs Numeric](#6-bivariate-analysis--numeric-vs-numeric)
7. [Bivariate Analysis — Numeric vs Categorical](#7-bivariate-analysis--numeric-vs-categorical)
8. [Adding More Dimensions to a Scatter Plot](#8-adding-more-dimensions-to-a-scatter-plot)
9. [Cat & Rel Facets](#9-cat--rel-facets)
10. [Categorical vs Categorical](#10-categorical-vs-categorical)
11. [Correlation Matrix](#11-correlation-matrix)
12. [Multivariate Wrap-Up (pairplot)](#12-multivariate-wrap-up-pairplot)

---

## 1) About This Dataset

`medical_data.csv` is a patient-level clinical dataset: **1000 patients**, each with:
- **Demographics**: age, gender, region
- **Lifestyle factors**: smoker, exercise_minutes_per_week
- **Vitals/labs**: bmi, systolic_bp, diastolic_bp, cholesterol, glucose
- **Outcomes**: disease_risk, readmitted_30_days, hospital_visits_last_year, medication_adherence

**What could this represent in real life?** This is exactly the shape of data a hospital or health-insurance analytics team would use to study risk factors — e.g. *"does smoking or low exercise correlate with higher blood pressure or disease risk?"*, or *"which patient profile is most likely to be readmitted within 30 days?"*. That second question is a natural stepping stone toward a **machine-learning classification project** — but this notebook stops at the analysis stage: understanding the data and the relationships in it, before any modeling.

**The 10 steps this kind of EDA typically follows:**
1. Load the data and peek at it (head, sample)
2. Confirm shape, columns, index
3. Inspect dtypes/info/memory, fix parsing issues
4. Run `describe()` (+ custom percentiles) on numeric columns
5. Check for duplicates and missing values
6. Univariate analysis — look at each column on its own
7. Bivariate analysis — look at pairs of columns
8. Categorical vs categorical analysis
9. Multivariate analysis — 3+ variables at once (facets, pairplots)
10. Correlation analysis — which numeric variables move together

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 2) Loading & Peeking at the Data

```python
df = pd.read_csv('medical_data.csv')

print(df.head())
print(df.tail())
print(df.head(50))

# .sample() returns random rows — a less biased peek than head()/tail(),
# since head/tail can hide patterns that only show up further into the file
print(df.sample(7))
```

---

## 3) Initial Inspection

```python
print(df.info())                       # dtypes, non-null counts, memory usage
print(df.duplicated().sum().item())     # how many fully duplicated rows exist
print(df.describe().transpose())         # summary stats, transposed so each row = one column
print(df.columns.tolist())                # quick list of every column name
```

---

## 4) Univariate Analysis — Numeric Distributions

**A roughly uniform / well-behaved distribution: age**
```python
sns.histplot(x='age', data=df, bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

sns.kdeplot(x='age', data=df)
plt.show()
```

**A distribution with outliers: bmi**
```python
sns.histplot(x='bmi', data=df, bins=30, kde=True)
plt.title("BMI Distribution")
plt.show()

sns.kdeplot(x='bmi', data=df)
plt.show()
```

A boxplot makes outliers explicit as individual points beyond the whiskers:
```python
sns.boxplot(x='bmi', data=df)
plt.show()

sns.boxplot(x='age', data=df)
plt.show()
```

`violinplot` (distribution shape) + `pointplot` (mean marker) together:
```python
sns.violinplot(data=df, x='bmi')
sns.pointplot(data=df, x='bmi', estimator='mean', color='red', marker='d')
plt.show()
```

---

## 5) Univariate Analysis — Categorical Distributions

```python
sns.countplot(data=df, x='gender')
plt.show()
```

> ⚠️ **Fixed:** the original notebook plotted `x='diastolic_bp'` (a continuous numeric column) with `order=['low','medium','high']` — that combination doesn't make sense for a countplot. The column that actually holds Low/Medium/High categories is `disease_risk`:
```python
sns.countplot(data=df, x='disease_risk', order=['Low', 'Medium', 'High'])
plt.show()
```

Pie chart of a `value_counts()` result:
```python
smokern = df['smoker'].value_counts().reset_index()
plt.pie(smokern['count'], labels=smokern['smoker'], autopct='%1.1f%%', shadow=True,
        wedgeprops={'edgecolor': 'black'})
plt.show()

disease_risk_counts_df = df['disease_risk'].value_counts().reset_index()
plt.pie(
    disease_risk_counts_df['count'],
    labels=disease_risk_counts_df['disease_risk'],
    colors=['#42ddf5', '#dd42f5', '#918f0c'],
    autopct='%1.2f%%',
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)
plt.show()
```

---

## 6) Bivariate Analysis — Numeric vs Numeric

Tools for two numeric columns: scatter plot, line plot, bar plot, box plot, hexbin plot.
```python
sns.scatterplot(data=df, x='age', y='systolic_bp', alpha=0.4)
plt.show()

print(df.corr(numeric_only=True))
```

`regplot` = scatterplot + a fitted regression line, to visualize the trend:
```python
sns.regplot(
    data=df,
    x='age',
    y='systolic_bp',
    scatter_kws={'alpha': 0.5, 'color': '#000000'},
    line_kws={'color': '#ff0000'}
)
plt.show()
```

---

## 7) Bivariate Analysis — Numeric vs Categorical

```python
sns.boxplot(data=df, x='gender', y='bmi')
plt.title("BMI Distribution")
plt.show()

sns.violinplot(data=df, x='gender', y='bmi')
sns.pointplot(data=df, x='gender', y='bmi', estimator='mean', color='red', marker='d')
plt.show()

sns.barplot(data=df, x='smoker', y='exercise_minutes_per_week', estimator='mean', color='red')
plt.title("Average Weekly Exercise by Smoking Status")
plt.show()
```

---

## 8) Adding More Dimensions to a Scatter Plot

`hue`: color points by a category
```python
sns.scatterplot(data=df, x='age', y='systolic_bp', hue='gender')
plt.show()
```

`style` + `hue` together, with a custom marker per category:

> ⚠️ **Fixed:** marker dict keys must match the data's actual category text exactly — the data has `"Male"`/`"Female"` (capitalized), so the dict keys must be capitalized too, not `"male"`/`"female"`.
```python
sns.scatterplot(
    data=df,
    x='age',
    y='systolic_bp',
    alpha=0.4,
    style='gender',
    hue='gender',
    markers={'Male': 's', 'Female': 'o'}
)
plt.show()
```

`size`: scale each point by a third numeric variable:
```python
plt.figure(figsize=(15, 10))
sns.scatterplot(
    data=df, x='age', y='systolic_bp',
    size='hospital_visits_last_year',
    style='gender',
    hue='gender',
    markers={'Male': 's', 'Female': 'o'}
)
plt.show()
```

```python
sns.boxplot(data=df, x='gender', y='bmi', hue='smoker')
plt.show()

sns.violinplot(data=df, x='gender', y='bmi', hue='smoker')
sns.pointplot(data=df, color='red', x='gender', y='bmi')
plt.show()
```

---

## 9) Cat & Rel Facets

Relationship between two numbers, split across panels:
```python
sns.relplot(data=df, x='age', y='systolic_bp', col='gender', hue='smoker', size='hospital_visits_last_year')
plt.show()

sns.catplot(
    data=df,
    x='age',
    y='smoker',
    hue='bmi',
    col='gender',
    row='region',
    kind='violin'
)
plt.show()
```

---

## 10) Categorical vs Categorical

```python
ct = pd.crosstab(df['gender'], df['smoker'])   # crosstab returns a DataFrame

ct.plot(kind='bar')
plt.title('Proportion of Smokers by Gender')
plt.show()

sns.heatmap(ct, annot=True, fmt='d', cmap='YlGnBu')
plt.show()

sns.countplot(data=df, x='gender', hue='smoker')
plt.show()
```

`multiple='stack'`: raw counts stacked on top of each other.
`multiple='fill'`: same data, but as a proportion (each bar sums to 1) — easier to compare shares across categories of different sizes.
```python
sns.histplot(data=df, x='gender', hue='smoker', multiple='stack', discrete=True)
plt.show()

sns.histplot(data=df, x='gender', hue='smoker', multiple='fill', discrete=True)
plt.show()
```

---

## 11) Correlation Matrix

```python
corr = df.corr(numeric_only=True)

plt.figure(figsize=(15, 10))
sns.heatmap(corr, annot=True, fmt='.2f', vmin=0, vmax=1, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
```

---

## 12) Multivariate Wrap-Up (pairplot)

A pairplot draws every pairwise scatterplot between the chosen numeric columns at once, plus a distribution on the diagonal — a fast way to scan for relationships across many variables in one figure. Coloring by `disease_risk` shows whether any of these health metrics visibly separate low/medium/high-risk patients.

```python
numeric_cols = [
    'age',
    'bmi',
    'systolic_bp',
    'diastolic_bp',
    'exercise_minutes_per_week'
]

sns.pairplot(df[numeric_cols + ['disease_risk']], hue='disease_risk', diag_kind='kde')
plt.show()
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
