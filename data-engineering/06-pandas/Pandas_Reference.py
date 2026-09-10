# =============================================================================
# 🐼 Pandas Reference — Runnable Python Script
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import pandas as pd
import numpy as np
import sys

# Ensure UTF-8 output encoding for Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def main():
    print("[+] Executing Pandas Fundamentals Reference Script...\n")

    # 1. Create DataFrame
    print("--- 1. Creating DataFrame & Inspection ---")
    data = {
        'ID': [1, 2, 3, 4, 5],
        'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice White', 'Charlie Brown'],
        'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing'],
        'Age': [28, 34, 45, 29, 32],
        'Salary': [50000, 75000, 85000, 72000, 68000],
        'Joining_Date': ['2020-05-21', '2019-06-12', '2018-07-15', '2021-01-04', '2019-11-30']
    }
    df = pd.DataFrame(data)
    print(df.head(), "\n")

    # 2. Filtering
    print("--- 2. Filtering Employees (Department == 'IT') ---")
    it_employees = df[df['Department'] == 'IT']
    print(it_employees, "\n")

    # 3. Modifying & Vectorized Calculations
    print("--- 3. Salary Raise Calculation (5% Raise) ---")
    df['Salary_After_Raise'] = df['Salary'] * 1.05
    print(df[['Name', 'Salary', 'Salary_After_Raise']], "\n")

    # 4. Groupby Aggregation
    print("--- 4. Average Salary by Department ---")
    avg_salary = df.groupby('Department')['Salary'].mean().reset_index()
    print(avg_salary, "\n")

    # 5. Missing Data Operations
    print("--- 5. Handling Missing Data ---")
    df_nan = pd.DataFrame({
        'A': [1.0, 2.0, np.nan],
        'B': [4.0, np.nan, 6.0]
    })
    print("Original NaN DataFrame:\n", df_nan)
    print("Filled NaN (fillna(0)):\n", df_nan.fillna(0), "\n")

    # 6. Datetime Operations
    print("--- 6. Datetime Filtering (Joined After 2020-01-01) ---")
    df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])
    recent_joins = df[df['Joining_Date'] > '2020-01-01']
    print(recent_joins[['Name', 'Department', 'Joining_Date']], "\n")

    print("[SUCCESS] Pandas Reference Script Executed Successfully!")

if __name__ == "__main__":
    main()
