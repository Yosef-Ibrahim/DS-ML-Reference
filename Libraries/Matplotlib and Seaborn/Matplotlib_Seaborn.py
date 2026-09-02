"""
Matplotlib & Seaborn Reference — Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email : youssefibrahimelisely@gmail.com
Phone : 01119834356

Want to contribute an idea, fix, or new example (ML / Data Science / Data
Analysis topics only)? Reach out on the contact info above.

Note: this script expects "employees.csv" to be in the same folder.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random

# =========================================================
# 1) INTRODUCTION
# =========================================================
# Matplotlib is the foundational plotting library in Python — it gives
# you full, low-level control over every part of a chart (axes, ticks,
# colors, layout...).
#
# Seaborn is built ON TOP of Matplotlib. It's higher-level and made for
# statistical plots: it understands pandas DataFrames directly (you pass
# column names instead of raw lists), and it comes with better default
# styling out of the box.
#
# Rule of thumb: reach for Matplotlib when you need precise, custom
# control or a chart type Seaborn doesn't cover. Reach for Seaborn when
# you're exploring a DataFrame and want good-looking statistical plots
# fast.


# =========================================================
# 2) LINE PLOT
# =========================================================
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 8, 16, 32, 64]

# ---- Matplotlib ----
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# ---- Seaborn (works with raw lists too) ----
sns.lineplot(x=x, y=y)
plt.title("Line Plot (Seaborn)")   # unlike Matplotlib's plt.title(), Seaborn
                                     # functions don't set the title themselves —
                                     # you still call plt.title() afterward
plt.show()

# ---- Seaborn (the more common way: from a DataFrame, by column name) ----
data = {
    "ahmed": [1, 2, 3, 4, 5, 6],
    "Mahmoud": [2, 3, 4, 5, 6, 7]
}
df = pd.DataFrame(data)

sns.lineplot(data=df, x="ahmed", y="Mahmoud")
plt.show()


# =========================================================
# 3) SCATTER PLOT
# =========================================================
height = [160, 165, 170, 175, 180]
weight = [60, 65, 70, 75, 80]

# ---- Matplotlib ----
plt.scatter(height, weight)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

# ---- Seaborn (from a DataFrame) ----
sns.scatterplot(data=df, x="ahmed", y="Mahmoud")
plt.show()


# =========================================================
# 4) BAR PLOT
# =========================================================
courses = ["Ml", "Ty", "Ry", "Ss", "Yes"]
students = [30, 40, 50, 60, 70]

# ---- Matplotlib ----
plt.bar(courses, students)
plt.title("Bar Plot")
plt.xlabel("Course")
plt.ylabel("Students")
plt.show()


# =========================================================
# 5) HISTOGRAMS & RANDOM DATA
# =========================================================
# np.random.normal(loc, scale, size):
# - loc   = mean of the distribution
# - scale = standard deviation (SD)
# - size  = number of observations to generate
sales = [random.randint(0, 100) for i in range(100)]
new_sales = np.random.normal(loc=100, scale=1, size=100)

plt.hist(new_sales, bins=20)
plt.title("Histogram of Sales")
plt.xlabel("Sales")
plt.ylabel("Count")
plt.show()


# =========================================================
# 6) MULTIPLE PLOTS IN ONE FIGURE
# =========================================================
# subplot(rows, columns, position) lets you place several charts side by
# side in the same figure.
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


# =========================================================
# 7) LOADING REAL DATA & WORKING WITH DATES
# =========================================================
# Load the dataset (keep the CSV in the same folder as this script)
df = pd.read_csv("employees.csv")
print(df.head())
print(df.info())

# Convert the join-date column to a real datetime type FIRST — the .dt
# accessor (used below to pull out the year) only works on a datetime
# column, not on plain text.
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
df["year_Joining_Date"] = df["Joining_Date"].dt.year
print(df)


# =========================================================
# 8) GROUPBY + TREND LINE
# =========================================================
# Combine pandas' groupby with a Seaborn line plot to show a trend over
# time — here, average salary per joining year.
year_stats = df.groupby("year_Joining_Date")["Salary"].mean().reset_index()
sns.lineplot(data=year_stats, x="year_Joining_Date", y="Salary")
plt.title("Average Salary by Joining Year")
plt.show()


# =========================================================
# 9) MODIFYING DATA WITH iloc
# =========================================================
# A quick reminder that .iloc lets you edit a single cell by its
# (row, column) position — useful for fixing a bad data point by hand.
df.iloc[0, 3] = 28   # sets column index 3 ("Age") of row 0 to 28


# =========================================================
# 10) DISTRIBUTION PLOTS (Seaborn)
# =========================================================
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


# =========================================================
# 11) CATEGORICAL COUNTS
# =========================================================
# countplot: counts how many rows fall into each category automatically
sns.countplot(data=df, x="Department")
plt.title("Employees per Department")
plt.show()

# If you already have the counts as a column (e.g. from value_counts()),
# use barplot instead of countplot:
dept_counts = df["Department"].value_counts().reset_index()
dept_counts.columns = ["Department", "count"]   # name the columns explicitly for clarity

sns.barplot(data=dept_counts, x="Department", y="count")
plt.title("Employees per Department (Barplot)")
plt.show()


# =========================================================
# 12) CORRELATION HEATMAP
# =========================================================
corr_matrix = df.corr(numeric_only=True)

# Correlation values range from -1 to 1, so the color scale must match:
# vmin=-1, vmax=1 (not vmin=1 — that would collapse the color scale to a
# single value and make the heatmap meaningless).
sns.heatmap(data=corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

# A strong negative correlation here (e.g. between Age and
# year_Joining_Date) makes sense: older employees tend to have joined
# in earlier years.
plt.scatter(df["Age"], df["year_Joining_Date"])
plt.xlabel("Age")
plt.ylabel("Year Joined")
plt.show()


# =========================================================
# 13) PIE CHART
# =========================================================
dpt_info = df["Department"].value_counts().reset_index()
dpt_info.columns = ["Department", "count"]

plt.pie(dpt_info["count"], labels=dpt_info["Department"], autopct="%1.1f%%")
plt.title("Department Share")
plt.show()


# =========================================================
# 14) SAVING PLOTS
# =========================================================
# savefig() saves whatever was plotted before it — call it BEFORE
# plt.show(), since show() can clear the current figure on some setups.
plt.bar(courses, students)
plt.title("Bar Plot")
plt.savefig("bar_plot.png", dpi=300, bbox_inches="tight")
plt.show()
