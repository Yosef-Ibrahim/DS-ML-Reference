# 🐼 Pandas Reference — A Beginner-Friendly Guide

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute to this reference (ML / Data Science / Data Analysis topics only)? Reach out using the contact info above.

---

## 📑 Table of Contents
1. [Introduction](#1-introduction)
2. [Series](#2-series)
3. [Creating a DataFrame](#3-creating-a-dataframe)
4. [Exploring a DataFrame](#4-exploring-a-dataframe)
5. [Selecting Data](#5-selecting-data)
6. [Boolean Indexing / Masks](#6-boolean-indexing--masks)
7. [loc & iloc](#7-loc--iloc)
8. [Adding & Modifying Columns](#8-adding--modifying-columns)
9. [Dropping Columns](#9-dropping-columns)
10. [Missing Data (NaN / NaT / NA)](#10-missing-data-nan--nat--na)
11. [GroupBy & Aggregation](#11-groupby--aggregation)
12. [Apply (custom transformations)](#12-apply-custom-transformations)
13. [Loading Data](#13-loading-data)
14. [Working with Dates](#14-working-with-dates)
15. [Sorting a DataFrame](#15-sorting-a-dataframe)
16. [Saving Data](#16-saving-data)

---

## 1) Introduction

**Pandas** is the go-to library for working with tabular (table-like) data in Python — it's built on top of NumPy and is the backbone of almost every data analysis workflow.

The two core data structures:
- **Series** — a single labeled column of data (1D)
- **DataFrame** — a full table made of multiple Series sharing the same row labels (2D — rows and columns, like an Excel sheet)

```python
import pandas as pd
```

---

## 2) Series

```python
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
x = pd.Series([1, 2, 3, 4], index=['d', 'b', 'c', 'a'])
```

**Important concept:** pandas aligns operations by **index label**, not by position. Even though `s` and `x` were created with values in a different order, addition matches each label to its counterpart:
```python
print(s + x)
# a    5   (s['a']=1 + x['a']=4)
# b    4   (s['b']=2 + x['b']=2)
# c    6   (s['c']=3 + x['c']=3)
# d    5   (s['d']=4 + x['d']=1)

print(s.shape)   # (4,) -> same shape idea as NumPy
```

---

## 3) Creating a DataFrame

```python
data = {
    "Name": ["Youssef", "Mohamed", "Ahmed", "Ali", "Sara", "Mona", "Omar", "Mariam"],
    "Age": [22, 25, 30, 21, 28, 24, 27, 23],
    "City": ["Elmarg", "Ainshams", "Nasr City", "Maadi", "Giza", "Zamalek", "Dokki", "Heliopolis"],
    "No Of children": [1, 5, 4, 3, 2, 5, 3, 90]   # 90 is intentionally unrealistic — see describe() below
}

df = pd.DataFrame(data)
print(df)
```

---

## 4) Exploring a DataFrame

```python
print(df.head(3))      # first 3 rows
print(df.tail(3))       # last 3 rows
print(df.sample(4))      # 4 random rows — a quick, unbiased peek at your data
print(df.info())          # column names, dtypes, non-null counts, memory usage
print(df.describe())       # summary stats for numeric columns (count, mean, std, min, max, quartiles)

# describe() with custom percentiles instead of the default 25/50/75
desc = df.describe(percentiles=[0.05, 0.95, 0.65])

# describe() for text/object columns instead of numeric ones
print(df.describe(include='str'))   # count, unique, top (most frequent), freq
```

> 💡 **Tip:** `describe()` is also a quick way to spot outliers. Notice the huge jump between the 75th percentile and the max in `"No Of children"` — a max of 90 next to a much smaller mean is a classic outlier signal worth investigating before you trust the data.

Series-level statistics:
```python
print(df["Age"].var())          # variance divided by n (population)
print(df["Age"].var(ddof=1))     # variance divided by n-1 (sample)
```

---

## 5) Selecting Data

```python
print(type(s))    # pandas.core.series.Series
print(type(df))    # pandas.core.frame.DataFrame

display(df)   # in Jupyter, renders a formatted table (nicer than print() there)

print(type(df["Name"]))            # single column with [] -> Series
print(type(df[["Name", "Age"]]))    # list of columns with [[ ]] -> DataFrame (even for one column!)
```

---

## 6) Boolean Indexing / Masks

```python
print(df["Age"] > 23)   # returns a boolean Series — True/False per row

# Using the boolean Series to filter the DataFrame ("boolean mask")
print(df[df["Age"] > 23])
```

Combining multiple conditions: use `&` for AND, `|` for OR — and always wrap each condition in parentheses (Python's operator precedence requires it here, unlike plain `and`/`or`).
```python
print(df[(df["Age"] > 23) & (df["No Of children"] < 25)])
print(df[(df["Age"] > 23) | (df["No Of children"] < 25)])
```

---

## 7) loc & iloc

- **`.loc`** → **label**-based selection: `df.loc[rows, columns]`
- **`.iloc`** → **position**-based selection: `df.iloc[from:to]` (like list slicing)

```python
print(df.loc[df["Age"] > 23])                       # loc also accepts a boolean mask
print(df.loc[[0, 3, 2, 4, 5], ["Name", "Age"]])       # specific rows + specific columns by label
print(df.iloc[:, 0:3])                                 # all rows, columns at positions 0,1,2
```

---

## 8) Adding & Modifying Columns

```python
data = {
    "Name": ["Ali", "Sami", "Youssef"],
    "Salary": [2000, 3000, 4000]
}
new_df = pd.DataFrame(data)

new_df["Gender"] = ["Male", "Female", "Other"]     # add a new column from a list
new_df["Annual_salary"] = new_df["Salary"] * 12     # add a new column computed from another column
```

---

## 9) Dropping Columns

`axis=1` means "a column" (`axis=0` would mean "a row"). `inplace=True` applies the change directly to `df` instead of returning a new DataFrame. Without `inplace`, the drop is temporary — `df` stays unchanged unless you reassign it (`df = df.drop(...)`). With `inplace=True`, the change is permanent on `df` itself.
```python
df.drop("No Of children", axis=1, inplace=True)
```

---

## 10) Missing Data (NaN / NaT / NA)

- **NaN** → "Not a Number" (missing numeric value)
- **NaT** → "Not a Time" (missing datetime value)
- **NA** → "Not Available" (general missing value, pandas' newer unified marker)

```python
data = {
    "Name": ["Ali", "Sami", "Youssef"],
    "Salary": [None, 3000, None]
}
new_df = pd.DataFrame(data)
new_df["Gender"] = [None, "Male", "Male"]
new_df["Annual_Salary"] = new_df["Salary"] * 12

print(new_df.isna())                                     # True/False grid showing where values are missing
print(new_df.isna().sum())                                 # count of missing values per column
print(new_df.isna().sum().sort_values(ascending=False))     # same, sorted from most to least missing

print(new_df["Gender"].fillna("Male"))                             # fill missing values in one column (returns a copy)
new_df.fillna({"Gender": "Male"}, inplace=True)                     # fill missing values per-column, in place
print(new_df.dropna())                                                 # drop any row with at least one missing value
print(new_df.drop(columns=["Annual_Salary"]))                           # drop a column by name (alternative to axis=1)
```

---

## 11) GroupBy & Aggregation

```python
df = pd.DataFrame({
    "Department": ["HR", "IT", "HR", "IT"],
    "Salary": [50000, 60000, 45000, 80000]
})

grouped = df.groupby("Department").mean()
print(grouped)
#              Salary
# Department
# HR          47500.0
# IT          70000.0
```

`reset_index()` turns the grouped label (`"Department"`) back into a normal column instead of it being the DataFrame's index — handy before saving or merging the result with other data.
```python
grouped = df.groupby("Department").mean().reset_index()
print(grouped)
#   Department   Salary
# 0         HR  47500.0
# 1         IT  70000.0
```

---

## 12) Apply (custom transformations)

```python
def double_salary(x):
    return x * 2

# apply() runs a function across every value in a column (or row, with axis=1)
df["Double_Salary"] = df["Salary"].apply(lambda x: x * 2)   # a lambda works too, for short logic
```

---

## 13) Loading Data

Reading a CSV file into a DataFrame — the single most common way a data analysis actually starts:
```python
df = pd.read_csv("data.csv")
```

Useful `read_csv` parameters:
```python
df = pd.read_csv("data.csv", sep=",")                  # sep: the delimiter (";", "\t" for tab-separated files, etc.)
df = pd.read_csv("data.csv", header=0)                    # header: which row holds the column names (0 = first row)
df = pd.read_csv("data.csv", index_col=0)                   # index_col: use a column as the row index instead of 0,1,2...
df = pd.read_csv("data.csv", usecols=["Name", "Age"])         # usecols: load only specific columns (saves memory)
df = pd.read_csv("data.csv", nrows=100)                         # nrows: load only the first N rows (great for a quick peek at huge files)
```

Other common formats:
```python
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")   # requires openpyxl installed
df = pd.read_json("data.json")
df = pd.read_sql("SELECT * FROM table_name", connection)  # from a database connection (e.g. SQLAlchemy)
```

---

## 14) Working with Dates

Dates loaded from a file/dict usually come in as plain text (strings). Convert the column to a real datetime type first:
```python
dates_df = pd.DataFrame({
    "Name": ["Ali", "Sami", "Youssef"],
    "JoinDate": ["2024-01-15", "2023-06-20", "2022-11-05"]
})

dates_df["JoinDate"] = pd.to_datetime(dates_df["JoinDate"])
```

Once it's a datetime column, the `.dt` accessor unlocks date-based fields:
```python
dates_df["Month"] = dates_df["JoinDate"].dt.month        # 1-12
dates_df["Year"] = dates_df["JoinDate"].dt.year            # e.g. 2024
dates_df["DayName"] = dates_df["JoinDate"].dt.day_name()     # e.g. "Monday"
```

---

## 15) Sorting a DataFrame

`sort_values`: sort rows by the values in one or more columns.
```python
sorted_df = df.sort_values("Salary")                     # ascending by default
sorted_df = df.sort_values("Salary", ascending=False)      # descending
sorted_df = df.sort_values(["Department", "Salary"])        # sort by Department first, then Salary within each group
```

`sort_index`: sort rows by their index labels instead of a column's values.
```python
sorted_by_index = df.sort_index()
```

---

## 16) Saving Data

`to_csv`: save a DataFrame back to a CSV file. `index=False` is important — without it, pandas writes the DataFrame's row index as an extra unnamed column in the file, which you usually don't want.
```python
df.to_csv("output.csv", index=False)
```

Other common save formats:
```python
df.to_excel("output.xlsx", index=False, sheet_name="Sheet1")   # requires openpyxl installed
df.to_json("output.json", orient="records")                       # orient="records" -> a list of {column: value} dicts, the most common shape
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
