# =============================================================================
# 📊 Data Visualization with Matplotlib & Seaborn — Headless Python Script
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import matplotlib
matplotlib.use('Agg') # Headless backend for automated pipeline execution

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def main():
    print("[+] Executing Headless Data Visualization Script...\n")

    # Sample Data
    np.random.seed(42)
    df = pd.DataFrame({
        'total_bill': np.random.normal(loc=20, scale=5, size=100),
        'tip': np.random.normal(loc=3, scale=1, size=100),
        'category': np.random.choice(['Group A', 'Group B'], size=100)
    })

    # 1. Matplotlib Subplots
    print("--- 1. Generating Matplotlib Subplots ---")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].scatter(df['total_bill'], df['tip'], color='blue', alpha=0.7)
    axes[0].set_title("Total Bill vs Tip Scatter")
    
    axes[1].hist(df['total_bill'], bins=15, color='green', edgecolor='black')
    axes[1].set_title("Total Bill Distribution")
    plt.tight_layout()
    plt.close()

    # 2. Seaborn Boxplot & Heatmap
    print("--- 2. Generating Seaborn Boxplot & Correlation Heatmap ---")
    sns.set_theme(style="whitegrid")
    
    # Boxplot
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='category', y='total_bill', data=df)
    plt.title("Total Bill Distribution by Category")
    plt.close()

    # Correlation Heatmap
    plt.figure(figsize=(6, 4))
    corr = df[['total_bill', 'tip']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.close()

    print("[SUCCESS] Data Visualization Script Executed & Figures Generated Headlessly!")

if __name__ == "__main__":
    main()
