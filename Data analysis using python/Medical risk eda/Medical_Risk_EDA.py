"""
Medical Risk Factors — Exploratory Data Analysis (EDA)
Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email : youssefibrahimelisely@gmail.com
Phone : 01119834356

Want to contribute an idea, fix, or new example (ML / Data Science / Data
Analysis topics only)? Reach out on the contact info above.

Note: this script expects "medical_data.csv" to be in the same folder.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

print(np.__version__)
print(pd.__version__)
print(sns.__version__)
print(matplotlib.get_backend())

# =========================================================
# 1) ABOUT THIS DATASET
# =========================================================
# "medical_data.csv" is a patient-level clinical dataset: 1000 patients,
# each with demographics (age, gender, region), lifestyle factors
# (smoker, exercise_minutes_per_week), vitals/labs (bmi, systolic_bp,
# diastolic_bp, cholesterol, glucose), and outcomes (disease_risk,
# readmitted_30_days, hospital_visits_last_year, medication_adherence).
#
# What could this represent in real life? This is exactly the shape of
# data a hospital or health-insurance analytics team would use to study
# risk factors — e.g. "does smoking or low exercise correlate with
# higher blood pressure or disease risk?", or "which patient profile is
# most likely to be readmitted within 30 days?". That second question
# is a natural stepping stone toward a machine-learning classification
# project — but this notebook stops at the analysis stage: understanding
# the data and the relationships in it, before any modeling.
#
# The 10 steps this kind of EDA typically follows:
#  1. Load the data and peek at it (head, sample)
#  2. Confirm shape, columns, index
#  3. Inspect dtypes/info/memory, fix parsing issues
#  4. Run describe() (+ custom percentiles) on numeric columns
#  5. Check for duplicates and missing values
#  6. Univariate analysis — look at each column on its own
#  7. Bivariate analysis — look at pairs of columns
#  8. Categorical vs categorical analysis
#  9. Multivariate analysis — 3+ variables at once (facets, pairplots)
# 10. Correlation analysis — which numeric variables move together


# =========================================================
# 2) LOADING & PEEKING AT THE DATA
# =========================================================
df = pd.read_csv('medical_data.csv')

print(df.head())
print(df.tail())
print(df.head(50))

# .sample() returns random rows — a less biased peek than head()/tail(),
# since head/tail can hide patterns that only show up further into the file
print(df.sample(7))


# =========================================================
# 3) INITIAL INSPECTION
# =========================================================
print(df.info())                       # dtypes, non-null counts, memory usage
print(df.duplicated().sum().item())     # how many fully duplicated rows exist
print(df.describe().transpose())         # summary stats, transposed so each row = one column (easier to read with many columns)
print(df.columns.tolist())                # quick list of every column name


# =========================================================
# 4) UNIVARIATE ANALYSIS — NUMERIC DISTRIBUTIONS
# =========================================================

# ---- A roughly uniform / well-behaved distribution: age ----
plt.figure()
sns.histplot(x='age', data=df, bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count of age group")
plt.show()

plt.figure()
sns.kdeplot(x='age', data=df)
plt.title("Age Distribution (KDE)")
plt.xlabel("Age")
plt.ylabel("Density")
plt.show()

# ---- A distribution with outliers: bmi ----
plt.figure()
sns.histplot(x='bmi', data=df, bins=30, kde=True)
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Count of bmi group")
plt.show()

plt.figure()
sns.kdeplot(x='bmi', data=df)
plt.title("BMI Distribution (KDE)")
plt.xlabel("BMI")
plt.ylabel("Density")
plt.show()

# A boxplot makes outliers explicit as individual points beyond the whiskers
plt.figure()
sns.boxplot(x='bmi', data=df)
plt.title("BMI — Outlier Check")
plt.show()

plt.figure()
sns.boxplot(x='age', data=df)
plt.title("Age — Outlier Check")
plt.show()

# violinplot (distribution shape) + pointplot (mean marker) together
plt.figure()
sns.violinplot(data=df, x='bmi')
sns.pointplot(data=df, x='bmi', estimator='mean', color='red', marker='d')
plt.title("BMI Distribution with Mean Marker")
plt.show()


# =========================================================
# 5) UNIVARIATE ANALYSIS — CATEGORICAL DISTRIBUTIONS
# =========================================================
plt.figure()
sns.countplot(data=df, x='gender')
plt.title("Patient Count by Gender")
plt.show()

# NOTE (fixed): the original notebook plotted x='diastolic_bp' (a
# continuous numeric column) with order=['low','medium','high'] — that
# combination doesn't make sense for a countplot. The column that
# actually holds Low/Medium/High categories is "disease_risk":
plt.figure()
sns.countplot(data=df, x='disease_risk', order=['Low', 'Medium', 'High'])
plt.title("Patient Count by Disease Risk")
plt.show()

# Pie chart of a value_counts() result
smokern = df['smoker'].value_counts().reset_index()
plt.figure()
plt.pie(smokern['count'], labels=smokern['smoker'], autopct='%1.1f%%', shadow=True,
        wedgeprops={'edgecolor': 'black'})
plt.title("Smoker Share")
plt.show()

disease_risk_counts_df = df['disease_risk'].value_counts().reset_index()
plt.figure()
plt.pie(
    disease_risk_counts_df['count'],
    labels=disease_risk_counts_df['disease_risk'],
    colors=['#42ddf5', '#dd42f5', '#918f0c'],
    autopct='%1.2f%%',
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)
plt.title("Disease Risk Share")
plt.show()


# =========================================================
# 6) BIVARIATE ANALYSIS — NUMERIC vs NUMERIC
# =========================================================
# Tools for two numeric columns: scatter plot, line plot, bar plot, box
# plot, hexbin plot.
plt.figure()
sns.scatterplot(data=df, x='age', y='systolic_bp', alpha=0.4)
plt.title("Age vs Systolic Blood Pressure")
plt.show()

print(df.corr(numeric_only=True))

# regplot = scatterplot + a fitted regression line, to visualize the trend
plt.figure()
sns.regplot(
    data=df,
    x='age',
    y='systolic_bp',
    scatter_kws={'alpha': 0.5, 'color': '#000000'},
    line_kws={'color': '#ff0000'}
)
plt.title("Age vs Systolic BP — with Trend Line")
plt.show()


# =========================================================
# 7) BIVARIATE ANALYSIS — NUMERIC vs CATEGORICAL
# =========================================================
plt.figure()
sns.boxplot(data=df, x='gender', y='bmi')
plt.title("BMI Distribution")
plt.xlabel("Gender")
plt.ylabel("BMI")
plt.show()

plt.figure()
sns.violinplot(data=df, x='gender', y='bmi')
sns.pointplot(data=df, x='gender', y='bmi', estimator='mean', color='red', marker='d')
plt.title("BMI Distribution by Gender (with Mean Marker)")
plt.xlabel("Gender")
plt.ylabel("BMI")
plt.show()

print(df.info())

plt.figure()
sns.barplot(data=df, x='smoker', y='exercise_minutes_per_week', estimator='mean', color='red')
plt.title("Average Weekly Exercise by Smoking Status")
plt.show()


# =========================================================
# 8) ADDING MORE DIMENSIONS TO A SCATTER PLOT
# =========================================================
# hue: color points by a category
plt.figure()
sns.scatterplot(data=df, x='age', y='systolic_bp', hue='gender')
plt.title("Age vs Systolic BP, colored by Gender")
plt.show()

# style + hue together, with a custom marker per category
# NOTE (fixed): marker dict keys must match the data's actual category
# text exactly — the data has "Male"/"Female" (capitalized), so the
# dict keys must be capitalized too, not "male"/"female".
plt.figure()
sns.scatterplot(
    data=df,
    x='age',
    y='systolic_bp',
    alpha=0.4,
    style='gender',
    hue='gender',
    markers={'Male': 's', 'Female': 'o'}
)
plt.title("Age vs Systolic BP, styled by Gender")
plt.show()

print(df['hospital_visits_last_year'].unique())

# size: scale each point by a third numeric variable
plt.figure(figsize=(15, 10))
sns.scatterplot(
    data=df, x='age', y='systolic_bp',
    size='hospital_visits_last_year',
    style='gender',
    hue='gender',
    markers={'Male': 's', 'Female': 'o'}
)
plt.title('Age vs Systolic BP — sized by Hospital Visits, styled by Gender')
plt.show()

plt.figure()
sns.boxplot(data=df, x='gender', y='bmi', hue='smoker')
plt.title("BMI Distribution")
plt.xlabel("Gender")
plt.ylabel("BMI")
plt.show()

plt.figure()
sns.violinplot(data=df, x='gender', y='bmi', hue='smoker')
sns.pointplot(data=df, color='red', x='gender', y='bmi')
plt.title("BMI Distribution")
plt.xlabel("Gender")
plt.ylabel("BMI")
plt.show()


# =========================================================
# 9) CAT & REL FACETS (relationship between two numbers, split across panels)
# =========================================================
plt.figure()
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


# =========================================================
# 10) CATEGORICAL vs CATEGORICAL
# =========================================================
print(type(pd.crosstab(df['gender'], df['smoker'])))   # crosstab returns a DataFrame

ct = pd.crosstab(df['gender'], df['smoker'])

plt.figure()
ct.plot(kind='bar')
plt.title('Proportion of Smokers by Gender')
plt.show()

plt.figure()
sns.heatmap(ct, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Gender vs Smoker — Crosstab Heatmap")
plt.show()

plt.figure()
sns.countplot(data=df, x='gender', hue='smoker')
plt.title("Gender vs Smoker — Counts")
plt.show()

# multiple='stack': raw counts stacked on top of each other
plt.figure()
sns.histplot(
    data=df,
    x='gender',
    hue='smoker',
    multiple='stack',
    discrete=True
)
plt.title("Gender vs Smoker — Stacked Counts")
plt.show()

# multiple='fill': same data, but as a proportion (each bar sums to 1) —
# easier to compare shares across categories of different sizes
plt.figure()
sns.histplot(
    data=df,
    x='gender',
    hue='smoker',
    multiple='fill',
    discrete=True
)
plt.title("Gender vs Smoker — Proportions")
plt.show()


# =========================================================
# 11) CORRELATION MATRIX
# =========================================================
corr = df.corr(numeric_only=True)

plt.figure(figsize=(15, 10))
sns.heatmap(corr, annot=True, fmt='.2f', vmin=0, vmax=1, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


# =========================================================
# 12) MULTIVARIATE WRAP-UP (pairplot)
# =========================================================
# A pairplot draws every pairwise scatterplot between the chosen numeric
# columns at once, plus a distribution on the diagonal — a fast way to
# scan for relationships across many variables in one figure. Coloring
# by "disease_risk" shows whether any of these health metrics visibly
# separate low/medium/high-risk patients.
numeric_cols = [
    'age',
    'bmi',
    'systolic_bp',
    'diastolic_bp',
    'exercise_minutes_per_week'
]

sns.pairplot(df[numeric_cols + ['disease_risk']], hue='disease_risk', diag_kind='kde')
plt.show()
