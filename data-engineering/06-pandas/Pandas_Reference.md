# 🐼 Pandas Reference — Fundamentals of Data Manipulation

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> ⚠️ **Fix applied:** The source notebook had an unterminated JSON string and a
> missing newline in the IT-department filter cell. The notebook companion was
> repaired and validated as valid JSON.
>
> 📖 Source: *Data Preprocessing & Visualization (Pandas)* course material (Rowad Misr Al-Raqmeya).

---

## 📑 Table of Contents
1. [What is Pandas?](#1-what-is-pandas)
2. [Pandas Core Data Structures (Series & DataFrame)](#2-pandas-core-data-structures-series--dataframe)
3. [Inspecting Data (head, info, describe)](#3-inspecting-data-head-info-describe)
4. [Selecting & Filtering Data (loc & Boolean Indexing)](#4-selecting--filtering-data-loc--boolean-indexing)
5. [Modifying Data (Columns, Vectorization & Drop)](#5-modifying-data-columns-vectorization--drop)
6. [Handling Missing Data (isnull, fillna, dropna)](#6-handling-missing-data-isnull-fillna-dropna)
7. [Grouping & Aggregations (groupby & value_counts)](#7-grouping--aggregations-groupby--value_counts)
8. [Applying Functions (apply)](#8-applying-functions-apply)
9. [Datetime Operations (to_datetime)](#9-datetime-operations-to_datetime)
10. [Exporting Data (to_csv)](#10-exporting-data-to_csv)

---

## 1) What is Pandas?

**Pandas** is an open-source data manipulation and analysis library built on top of **NumPy**. It provides high-performance, easy-to-use data structures (`Series` and `DataFrame`) designed for structured tabular data.

### Key Capabilities for Data Engineers
* **Automatic Label Alignment**: Computes arithmetic across datasets aligned by index/label.
* **Robust Missing Data Handling**: Detects, fills, or drops missing entries (`NaN`/`None`).
* **Groupby Engine**: High-speed split-apply-combine aggregations.
* **Multi-Format I/O**: Direct connection to CSV, Parquet, Excel, and SQL databases.

```python
import pandas as pd
```

---

## 2) Pandas Core Data Structures

### A) Pandas Series (1D)
A one-dimensional labeled array capable of holding any data type (similar to a database column).

```python
series = pd.Series([10, 20, 30, 40, 50])
print(series)
```

### B) Pandas DataFrame (2D)
A two-dimensional labeled tabular data structure with rows and columns.

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
```

---

## 3) Inspecting Data

```python
# 1. View first 5 rows
print(df.head())

# 2. Summary of columns, non-null counts, and dtypes
print(df.info())

# 3. Descriptive statistics for numerical columns
print(df.describe())
```

---

## 4) Selecting & Filtering Data

### Column Selection
```python
# Select single column (returns Series)
names = df['Name']

# Select multiple columns (returns DataFrame)
subset = df[['Name', 'City']]
```

### Label-Based Indexing with `.loc[]`
```python
# Select rows 0 to 1 and columns 'Name' & 'City'
selected_data = df.loc[0:1, ['Name', 'City']]
```

### Boolean Conditional Filtering
```python
# Filter employees older than 30
older_than_30 = df[df['Age'] > 30]

# Multi-condition filtering
it_dept = df[(df['Age'] > 25) & (df['City'] == 'New York')]
```

---

## 5) Modifying Data

### Adding & Updating Columns
```python
# Add new column
df['Salary'] = [70000, 80000, 90000]

# Vectorized update (add 1 year to Age)
df['Age'] = df['Age'] + 1
```

### Dropping Columns
```python
# Drop 'City' column (axis=1 specifies columns)
df_clean = df.drop('City', axis=1)
```

---

## 6) Handling Missing Data

```python
import numpy as np

df_nan = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6]
})

# 1. Detect missing values (returns boolean mask)
print(df_nan.isnull())

# 2. Fill missing values with a default (e.g. 0)
filled_df = df_nan.fillna(0)

# 3. Drop rows containing any missing value
cleaned_df = df_nan.dropna()
```

---

## 7) Grouping & Aggregations

```python
emp_data = {
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance'],
    'Salary': [50000, 60000, 45000, 80000, 85000]
}
emp_df = pd.DataFrame(emp_data)

# Group by department and compute mean salary
avg_salary_by_dept = emp_df.groupby('Department')['Salary'].mean()

# Count occurrences of unique values
dept_counts = emp_df['Department'].value_counts()
```

---

## 8) Applying Functions (`apply`)

The `.apply()` method executes a function across each element in a Series or row/column in a DataFrame.

```python
def double_salary(x):
    return x * 2

emp_df['Double_Salary'] = emp_df['Salary'].apply(double_salary)

# Or using lambda function
emp_df['Raised_Salary'] = emp_df['Salary'].apply(lambda x: x * 1.05)
```

---

## 9) Datetime Operations

```python
dates_df = pd.DataFrame({
    'Employee': ['John', 'Jane', 'Alice'],
    'Joining_Date': ['2020-05-21', '2019-06-12', '2021-01-04']
})

# Convert string column to Datetime
dates_df['Joining_Date'] = pd.to_datetime(dates_df['Joining_Date'])

# Filter employees who joined after Jan 1, 2020
recent_joins = dates_df[dates_df['Joining_Date'] > '2020-01-01']
```

---

## 10) Exporting Data

```python
# Save DataFrame to CSV without row index
recent_joins.to_csv('recent_joins.csv', index=False)
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
