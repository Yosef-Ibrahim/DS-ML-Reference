# 📊 Data Visualization with Matplotlib & Seaborn — EDA & Visual Analytics Reference

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Data Preprocessing & Visualization (Matplotlib & Seaborn)* course material (Rowad Misr Al-Raqmeya).

---

## 📑 Table of Contents
1. [Introduction to Matplotlib](#1-introduction-to-matplotlib)
2. [Basic Matplotlib Plot Types (Line, Scatter, Bar, Histogram)](#2-basic-matplotlib-plot-types)
3. [Figure Layouts & Subplots](#3-figure-layouts--subplots)
4. [Outlier Detection Strategies](#4-outlier-detection-strategies)
5. [Introduction to Seaborn](#5-introduction-to-seaborn)
6. [Categorical & Distribution Plots in Seaborn](#6-categorical--distribution-plots-in-seaborn)
7. [Relationship & Trend Plots (lmplot, pairplot, jointplot)](#7-relationship--trend-plots)
8. [Correlation Heatmaps](#8-correlation-heatmaps)

---

## 1) Introduction to Matplotlib

**Matplotlib** is the core 2D plotting engine in Python scientific stack. It provides a MATLAB-like procedural interface via `matplotlib.pyplot` and an object-oriented API (`fig, ax = plt.subplots()`).

```python
import matplotlib
matplotlib.use('Agg') # Headless backend for automated pipelines & servers
import matplotlib.pyplot as plt
import numpy as np
```

---

## 2) Basic Matplotlib Plot Types

### A) Line Plot
Used for tracking continuous changes or trends over time.
```python
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='blue', marker='o', linestyle='-', label='Prime Growth')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.savefig('line_plot.png')
plt.close()
```

### B) Scatter Plot
Visualizes bivariate relationships between two numeric features.
```python
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color='darkorange')
plt.title("Scatter Plot")
plt.savefig('scatter_plot.png')
plt.close()
```

### C) Bar Chart & Histogram
* **Bar Chart**: Categorical frequency comparison.
* **Histogram**: Binned frequency distribution of a continuous variable.

```python
# Bar Chart
plt.bar(['A', 'B', 'C', 'D'], [4, 7, 1, 8], color='teal')
plt.close()

# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data, bins=5, color='green', edgecolor='black')
plt.close()
```

---

## 3) Figure Layouts & Subplots

Grid arrangements allow comparing multiple charts in a single exported figure.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
axes[0].set_title('Quadratic Trend')

axes[1].plot([1, 2, 3, 4], [1, 2, 3, 4], 'g-')
axes[1].set_title('Linear Trend')

plt.tight_layout()
plt.savefig('subplots.png')
plt.close()
```

---

## 4) Outlier Detection Strategies

Outliers significantly distort statistical summary metrics (`mean`, `std`) and machine learning models. Visual techniques provide immediate diagnostic feedback:

| Visual Technique | How Outliers Appear |
|---|---|
| **Box Plot** | Points positioned beyond the $1.5 \times \text{IQR}$ whiskers |
| **Scatter Plot** | Data points isolated far outside the primary data cluster |
| **Histogram** | Isolated, low-frequency bars separated by empty bins |
| **KDE Plot** | Irregular secondary bumps outside the main probability peak |

---

## 5) Introduction to Seaborn

**Seaborn** is built directly on top of Matplotlib and integrates seamlessly with Pandas DataFrames. It automatically handles categorical aggregation, error bars, and color palettes.

```python
import seaborn as sns
sns.set_theme(style="whitegrid")
```

---

## 6) Categorical & Distribution Plots in Seaborn

```python
import pandas as pd

df_tips = pd.DataFrame({
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88],
    'tip': [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12],
    'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sun'],
    'sex': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male']
})

# 1. Distribution Plot with Kernel Density Estimate (KDE)
sns.histplot(df_tips['total_bill'], kde=True, bins=10)
plt.close()

# 2. Box Plot & Violin Plot
sns.boxplot(x='day', y='total_bill', data=df_tips)
plt.close()

sns.violinplot(x='day', y='total_bill', data=df_tips)
plt.close()
```

---

## 7) Relationship & Trend Plots

### Linear Regression Trend (`sns.lmplot`)
```python
sns.lmplot(x='total_bill', y='tip', data=df_tips)
plt.savefig('lmplot.png')
plt.close()
```

### Pairwise Scatter Matrix (`sns.pairplot`)
Generates pairwise scatter plots for all numerical columns and histograms on the diagonal.
```python
sns.pairplot(df_tips)
plt.savefig('pairplot.png')
plt.close()
```

---

## 8) Correlation Heatmaps

Visualizes correlation matrices to detect multicollinearity in data engineering and feature selection pipelines.

```python
# Compute Pearson Correlation Matrix
corr_matrix = df_tips[['total_bill', 'tip']].corr()

# Draw Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Feature Correlation Matrix")
plt.savefig('heatmap.png')
plt.close()
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
