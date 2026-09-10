# 🚀 Advanced Pandas — High-Performance Data Engineering Techniques

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Advanced Pandas Techniques for Data Engineers* course material (Rowad Misr Al-Raqmeya). Builds directly on [`../06-pandas/Pandas_Reference.md`](../06-pandas/Pandas_Reference.md).

---

## 📑 Table of Contents
1. [DataFrame Concatenation (pd.concat)](#1-dataframe-concatenation-pdconcat)
2. [Merging & Joining Datasets (pd.merge)](#2-merging--joining-datasets-pdmerge)
3. [Split-Apply-Combine & Advanced GroupBy](#3-split-apply-combine--advanced-groupby)
4. [Group-Level Transformations & Filters (agg, filter, transform)](#4-group-level-transformations--filters-agg-filter-transform)
5. [Multi-Dimensional Pivot Tables (pivot_table)](#5-multi-dimensional-pivot-tables-pivot_table)
6. [Time Series Data in Pandas (Timestamp, DatetimeIndex, Resampling)](#6-time-series-data-in-pandas)

---

## 1) DataFrame Concatenation (`pd.concat`)

Concatenation combines DataFrames along an axis (rows `axis=0` or columns `axis=1`).

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

# 1. Simple Concatenation
result = pd.concat([df1, df2])

# 2. Resetting Index (ignore_index=True)
result_clean = pd.concat([df1, df2], ignore_index=True)

# 3. Adding MultiIndex Keys
hierarchical = pd.concat([df1, df2], keys=['Source1', 'Source2'])
```

> ⚠️ **Note on `.append()` Deprecation**: `df.append()` is deprecated in modern Pandas versions. Always use `pd.concat([df1, df2], ignore_index=True)` instead.

---

## 2) Merging & Joining Datasets (`pd.merge`)

Pandas provides relational join capabilities similar to SQL databases:
* **One-to-One**: Merging on unique keys.
* **Many-to-One**: Merging lookup tables into transactional tables.
* **Many-to-Many**: Merging tables with duplicate key entries on both sides.

### Key Merge Parameters
```python
df_emp = pd.DataFrame({'emp_id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'dept_id': [10, 20, 10]})
df_dept = pd.DataFrame({'department_id': [10, 20, 30], 'dept_name': ['IT', 'HR', 'Finance']})

# Merge with differing key column names and suffixes for overlap
merged = pd.merge(
    df_emp, 
    df_dept, 
    left_on='dept_id', 
    right_on='department_id', 
    how='inner',
    suffixes=('_emp', '_dept')
)
```

---

## 3) Split-Apply-Combine & Advanced GroupBy

```python
df_sales = pd.DataFrame({
    'Store': ['A', 'A', 'B', 'B', 'A'],
    'Category': ['Tech', 'Furniture', 'Tech', 'Furniture', 'Tech'],
    'Sales': [100, 200, 150, 300, 120]
})

# Iterating over groups
for (store, category), group in df_sales.groupby(['Store', 'Category']):
    print(f"Store: {store}, Category: {category}, Total Rows: {len(group)}")
```

---

## 4) Group-Level Transformations & Filters

### A) `.aggregate()` (`.agg()`)
Applies multiple aggregation functions across grouped data simultaneously:
```python
agg_result = df_sales.groupby('Store')['Sales'].agg(['min', 'mean', 'max', 'std'])
```

### B) `.filter()`
Drops entire groups that do not satisfy a group-level boolean predicate:
```python
# Keep only stores where total sales exceed 350
high_performing_stores = df_sales.groupby('Store').filter(lambda x: x['Sales'].sum() > 350)
```

### C) `.transform()`
Performs group-wise calculations while preserving the exact original shape of the DataFrame (useful for normalizing values against group statistics):
```python
# Subtract group mean from each sale item
df_sales['Sales_Centered'] = df_sales.groupby('Store')['Sales'].transform(lambda x: x - x.mean())
```

---

## 5) Multi-Dimensional Pivot Tables

Pivot tables summarize tabular data by reshaping columns into multi-dimensional indexes and headers.

```python
df_titanic = pd.DataFrame({
    'Sex': ['female', 'female', 'male', 'male', 'female'],
    'Class': ['First', 'Second', 'First', 'Third', 'First'],
    'Fare': [100.0, 50.0, 110.0, 20.0, 120.0],
    'Embarked': ['Southampton', 'Cherbourg', 'Southampton', 'Southampton', 'Cherbourg']
})

pivot = df_titanic.pivot_table(
    values='Fare',
    index=['Sex', 'Class'],
    columns='Embarked',
    aggfunc='mean',
    fill_value=0,
    margins=True # Adds row and column totals ('All')
)
```

---

## 6) Time Series Data in Pandas

Pandas provides rich datetime data structures (`pd.Timestamp`, `pd.DatetimeIndex`, `pd.Period`, `pd.Timedelta`).

### Generating Date Ranges & Frequencies
```python
# Daily sequence
daily_range = pd.date_range('2023-01-01', periods=5, freq='D')

# Business month-end sequence
monthly_range = pd.date_range('2023-01-01', periods=6, freq='BM')
```

### Time-Indexed Resampling
```python
time_df = pd.DataFrame({
    'Value': np.random.randn(100)
}, index=pd.date_range('2023-01-01', periods=100, freq='D'))

# Resample daily data to Monthly Average
monthly_summary = time_df.resample('M').mean()
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
