# =============================================================================
# 🚀 Advanced Pandas — Runnable Python Script
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import pandas as pd
import numpy as np
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def main():
    print("[+] Executing Advanced Pandas Reference Script...\n")

    # 1. Concatenation
    print("--- 1. DataFrame Concatenation ---")
    df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
    df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})
    concat_df = pd.concat([df1, df2], ignore_index=True)
    print(concat_df, "\n")

    # 2. Merging Datasets
    print("--- 2. Relational Merge (left_on & right_on) ---")
    df_emp = pd.DataFrame({'emp_id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie'], 'dept_id': [10, 20, 10]})
    df_dept = pd.DataFrame({'department_id': [10, 20, 30], 'dept_name': ['IT', 'HR', 'Finance']})
    merged_df = pd.merge(df_emp, df_dept, left_on='dept_id', right_on='department_id', how='inner')
    print(merged_df, "\n")

    # 3. Transform & Filter
    print("--- 3. GroupBy Transform & Filter ---")
    df_sales = pd.DataFrame({
        'Store': ['A', 'A', 'B', 'B', 'A'],
        'Sales': [100, 200, 150, 300, 120]
    })
    df_sales['Centered_Sales'] = df_sales.groupby('Store')['Sales'].transform(lambda x: x - x.mean())
    print("Transformed DataFrame:\n", df_sales)
    
    filtered_stores = df_sales.groupby('Store').filter(lambda x: x['Sales'].sum() > 400)
    print("Filtered Stores (Total Sales > 400):\n", filtered_stores, "\n")

    # 4. Pivot Tables
    print("--- 4. Multi-Dimensional Pivot Tables ---")
    df_titanic = pd.DataFrame({
        'Sex': ['female', 'female', 'male', 'male', 'female'],
        'Class': ['First', 'Second', 'First', 'Third', 'First'],
        'Fare': [100.0, 50.0, 110.0, 20.0, 120.0],
        'Embarked': ['Southampton', 'Cherbourg', 'Southampton', 'Southampton', 'Cherbourg']
    })
    pivot = df_titanic.pivot_table(values='Fare', index=['Sex', 'Class'], columns='Embarked', aggfunc='mean', fill_value=0)
    print(pivot, "\n")

    # 5. Time Series Resampling
    print("--- 5. Time Series Resampling ---")
    dates = pd.date_range('2023-01-01', periods=60, freq='D')
    time_df = pd.DataFrame({'Revenue': np.random.randint(100, 500, size=60)}, index=dates)
    monthly_rev = time_df.resample('ME').sum()
    print(monthly_rev, "\n")

    print("[SUCCESS] Advanced Pandas Reference Script Executed Successfully!")

if __name__ == "__main__":
    main()
