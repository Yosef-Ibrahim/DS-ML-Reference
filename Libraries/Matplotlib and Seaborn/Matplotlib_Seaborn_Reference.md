# 📊 Matplotlib & Seaborn Reference — A Beginner-Friendly Guide

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute to this reference (ML / Data Science / Data Analysis topics only)? Reach out using the contact info above.
>
> 📁 This reference uses `employees.csv` (included in this folder) starting from section 7.

---

## 📑 Table of Contents
1. [Introduction](#1-introduction)
2. [Line Plot](#2-line-plot)
3. [Scatter Plot](#3-scatter-plot)
4. [Bar Plot](#4-bar-plot)
5. [Histograms & Random Data](#5-histograms--random-data)
6. [Multiple Plots in One Figure](#6-multiple-plots-in-one-figure)
7. [Loading Real Data & Working with Dates](#7-loading-real-data--working-with-dates)
8. [GroupBy + Trend Line](#8-groupby--trend-line)
9. [Modifying Data with iloc](#9-modifying-data-with-iloc)
10. [Distribution Plots (Seaborn)](#10-distribution-plots-seaborn)
11. [Categorical Counts](#11-categorical-counts)
12. [Correlation Heatmap](#12-correlation-heatmap)
13. [Pie Chart](#13-pie-chart)
14. [Saving Plots](#14-saving-plots)

---

## 1) Introduction

**Matplotlib** is the foundational plotting library in Python — it gives you full, low-level control over every part of a chart (axes, ticks, colors, layout...).

**Seaborn** is built **on top of** Matplotlib. It's higher-level and made for statistical plots: it understands pandas DataFrames directly (you pass column names instead of raw lists), and it comes with better default styling out of the box.

> 💡 **Rule of thumb:** reach for Matplotlib when you need precise, custom control or a chart type Seaborn doesn't cover. Reach for Seaborn when you're exploring a DataFrame and want good-looking statistical plots fast.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random
```

---

## 2) Line Plot

```python
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 8, 16, 32, 64]
```

**Matplotlib:**
```python
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
```

**Seaborn** (works with raw lists too):
```python
sns.lineplot(x=x, y=y)
plt.title("Line Plot (Seaborn)")   # unlike Matplotlib's plt.title(), Seaborn
                                     # functions don't set the title themselves —
                                     # you still call plt.title() afterward
plt.show()
```

**Seaborn** — the more common way: from a DataFrame, by column name:
```python
data = {
    "ahmed": [1, 2, 3, 4, 5, 6],
    "Mahmoud": [2, 3, 4, 5, 6, 7]
}
df = pd.DataFrame(data)

sns.lineplot(data=df, x="ahmed", y="Mahmoud")
plt.show()
```

---

## 3) Scatter Plot

```python
height = [160, 165, 170, 175, 180]
weight = [60, 65, 70, 75, 80]
```

**Matplotlib:**
```python
plt.scatter(height, weight)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
```

**Seaborn** (from a DataFrame):
```python
sns.scatterplot(data=df, x="ahmed", y="Mahmoud")
plt.show()
```

---

## 4) Bar Plot

```python
courses = ["Ml", "Ty", "Ry", "Ss", "Yes"]
students = [30, 40, 50, 60, 70]

plt.bar(courses, students)
plt.title("Bar Plot")
plt.xlabel("Course")
plt.ylabel("Students")
plt.show()
```

---

## 5) Histograms & Random Data

`np.random.normal(loc, scale, size)`:
- `loc` = mean of the distribution
- `scale` = standard deviation (SD)
- `size` = number of observations to generate

```python
sales = [random.randint(0, 100) for i in range(100)]
new_sales = np.random.normal(loc=100, scale=1, size=100)

plt.hist(new_sales, bins=20)
plt.title("Histogram of Sales")
plt.xlabel("Sales")
plt.ylabel("Count")
plt.show()
```

---

## 6) Multiple Plots in One Figure

`subplot(rows, columns, position)` lets you place several charts side by side in the same figure.

```python
plt.figure(figsize=(20, 5))

plt.subplot(1, 2, 1)
plt.hist(sales, bins=20)
plt.title("Histogram of Sales")
plt.xlabel("Sales")
plt.ylabel("Count")

plt.subplot(1, 2, 2)
plt.bar(courses, students)
plt.title("Bar Plot")
plt.xlabel("Course")
plt.ylabel("Students")

plt.show()
```

---

## 7) Loading Real Data & Working with Dates

```python
df = pd.read_csv("employees.csv")
print(df.head())
print(df.info())
```

> ⚠️ Convert the join-date column to a real datetime type **first** — the `.dt` accessor (used below to pull out the year) only works on a datetime column, not on plain text.

```python
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
df["year_Joining_Date"] = df["Joining_Date"].dt.year
```

---

## 8) GroupBy + Trend Line

Combine pandas' `groupby` with a Seaborn line plot to show a trend over time — here, average salary per joining year.

```python
year_stats = df.groupby("year_Joining_Date")["Salary"].mean().reset_index()

sns.lineplot(data=year_stats, x="year_Joining_Date", y="Salary")
plt.title("Average Salary by Joining Year")
plt.show()
```

---

## 9) Modifying Data with iloc

A quick reminder that `.iloc` lets you edit a single cell by its (row, column) position — useful for fixing a bad data point by hand.

```python
df.iloc[0, 3] = 28   # sets column index 3 ("Age") of row 0 to 28
```

---

## 10) Distribution Plots (Seaborn)

```python
sns.boxplot(data=df, y="Age")        # shows median, quartiles, and outliers
plt.title("Age Distribution — Boxplot")
plt.show()

sns.kdeplot(data=df, x="Age")         # smooth estimated distribution curve
plt.title("Age Distribution — KDE")
plt.show()

sns.violinplot(data=df, y="Age")       # combines a boxplot with a KDE shape
plt.title("Age Distribution — Violin Plot")
plt.show()

sns.histplot(data=df, x="Age", kde=True)  # histogram + KDE curve overlaid
plt.title("Age Distribution — Histogram + KDE")
plt.show()
```

---

## 11) Categorical Counts

`countplot` counts how many rows fall into each category automatically:
```python
sns.countplot(data=df, x="Department")
plt.title("Employees per Department")
plt.show()
```

If you already have the counts as a column (e.g. from `value_counts()`), use `barplot` instead of `countplot`:
```python
dept_counts = df["Department"].value_counts().reset_index()
dept_counts.columns = ["Department", "count"]   # name the columns explicitly for clarity

sns.barplot(data=dept_counts, x="Department", y="count")
plt.title("Employees per Department (Barplot)")
plt.show()
```

---

## 12) Correlation Heatmap

```python
corr_matrix = df.corr(numeric_only=True)
```

> ⚠️ Correlation values range from **-1 to 1**, so the color scale must match: `vmin=-1, vmax=1` (not `vmin=1` — that collapses the color scale to a single value and makes the heatmap meaningless).

```python
sns.heatmap(data=corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
```

A strong negative correlation here (e.g. between Age and year_Joining_Date) makes sense: older employees tend to have joined in earlier years.
```python
plt.scatter(df["Age"], df["year_Joining_Date"])
plt.xlabel("Age")
plt.ylabel("Year Joined")
plt.show()
```

---

## 13) Pie Chart

```python
dpt_info = df["Department"].value_counts().reset_index()
dpt_info.columns = ["Department", "count"]

plt.pie(dpt_info["count"], labels=dpt_info["Department"], autopct="%1.1f%%")
plt.title("Department Share")
plt.show()
```

---

## 14) Saving Plots

`savefig()` saves whatever was plotted before it — call it **before** `plt.show()`, since `show()` can clear the current figure on some setups.

```python
plt.bar(courses, students)
plt.title("Bar Plot")
plt.savefig("bar_plot.png", dpi=300, bbox_inches="tight")
plt.show()
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
