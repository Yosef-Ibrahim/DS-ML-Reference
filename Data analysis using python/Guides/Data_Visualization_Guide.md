# 📊 Essential Data Visualization Techniques in EDA

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis topics only)? Reach out using the contact info above.
>
> 📖 This is a **decision guide** — "which chart do I use for this kind of data/question?" — not tied to one dataset. For a worked example applying most of these chart types to a real dataset, see [`../../Libraries/Matplotlib and Seaborn/`](<../../Libraries/Matplotlib and Seaborn/>) and [`../Medical risk eda/`](<../Medical risk eda/>).

## 1. Understanding Data Types

### Categorical Data
- **Definition:** Data divided into distinct groups or labels.
  Example: Gender (Male/Female), City (Cairo, Giza, Luxor).
- **Properties:** Qualitative — describes *categories* rather than measurements.
- **Subtypes:**
  - **Nominal:** No natural order (e.g., color: red, blue, green).
  - **Ordinal:** Has order but not evenly spaced (e.g., education level: primary, secondary, university).

### Numerical Data
- **Definition:** Data that can take any numeric value within a range.
  Example: Age, Salary, Temperature.
- **Properties:** Quantitative — can be measured, averaged, and used in mathematical operations.
- **Subtypes:**
  - **Discrete:** Countable values (number of students = 25, 30, 31).
  - **Continuous:** Infinite possible values (height = 172.4 cm).

---

## 2. Levels of Data Analysis

| Type | Meaning | Example | Typical Visualization |
|------|----------|----------|------------------------|
| **Univariate** | One variable | Distribution of Age | Histogram, Boxplot |
| **Bivariate** | Relationship between two variables | Age vs Salary | Scatter Plot, Bar Plot |
| **Multivariate** | Relationship among three or more variables | Age, Salary, and Gender | Pair Plot, Heatmap, 3D Scatter |

---

## 3. Visualization Techniques by Purpose

### A. Understanding Data Distribution (Univariate)
| Chart | Works Best For | Purpose | When to Use |
|--------|----------------|----------|--------------|
| **Histogram** | Continuous data | Shows the frequency distribution of numeric data. | To see the shape of distribution (normal, skewed, bimodal). |
| **Boxplot** | Continuous data | Displays median, quartiles, and outliers. | To detect outliers and compare distributions across categories. |
| **Violin Plot** | Continuous data | Combines boxplot with a density curve. | When you want to see both distribution shape and spread. |
| **Bar Plot** | Categorical data | Shows counts or averages for each category. | To compare category sizes or frequencies. |
| **Pie Chart / Donut Chart** | Categorical data | Shows proportions of a whole. | For small number of categories (≤ 5). |

---

### B. Understanding Relationships (Bivariate)
| Chart | Works Best For | Purpose | When to Use |
|--------|----------------|----------|--------------|
| **Scatter Plot** | Two continuous variables | Shows correlation or pattern between two variables. | To check linear/non-linear relationships or clusters. |
| **Line Plot** | Continuous data over time | Tracks changes or trends over time. | For time series analysis (e.g., temperature per day). |
| **Bar Plot (Grouped)** | Categorical vs continuous | Compares mean or total of a numeric variable across categories. | To compare values by group (e.g., avg salary per department). |
| **Boxplot (Grouped)** | Categorical vs continuous | Shows distribution per category. | When comparing spread of numeric data between groups. |
| **Hexbin Plot** | Large scatter data | Groups nearby points into hexagonal bins. | For large datasets to reduce overplotting. |

---

### C. Understanding Correlations and Patterns (Multivariate)
| Chart | Works Best For | Purpose | When to Use |
|--------|----------------|----------|--------------|
| **Pair Plot (Seaborn)** | Multiple continuous variables | Shows scatter plots and distributions for all pairs. | To explore relationships between several features. |
| **Heatmap** | Correlation matrices or categorical cross-tabs | Visualizes relationships or strengths of correlation. | To identify multicollinearity or feature importance. |
| **Facet Grid / Subplots** | Mixture of variables | Splits visualizations by additional categorical features. | To see how relationships change by another variable. |
| **3D Scatter Plot** | Three continuous variables | Visualizes 3D relationships. | When the third variable provides meaningful context. |

---

### D. Understanding Composition
| Chart | Works Best For | Purpose | When to Use |
|--------|----------------|----------|--------------|
| **Stacked Bar Chart** | Categorical data | Shows contribution of sub-categories. | When comparing part-to-whole relationships across groups. |
| **Pie Chart / Treemap** | Categorical data | Visualizes percentage composition. | When showing how total is divided among few categories. |

---

### E. Understanding Trends and Time
| Chart | Works Best For | Purpose | When to Use |
|--------|----------------|----------|--------------|
| **Line Plot** | Continuous (over time) | Shows trends or patterns. | For daily, monthly, or yearly data trends. |
| **Area Chart** | Continuous (over time) | Highlights total volume over time. | When cumulative effect is important (e.g., revenue growth). |
| **Bar Plot (Time Series)** | Discrete time categories | Compare values at different time periods. | When showing totals per month or quarter. |

---

### F. Understanding Distribution Across Categories
| Chart | Works Best For | Purpose | When to Use |
|--------|----------------|----------|--------------|
| **Boxplot by Category** | Continuous vs Categorical | Compare spread, median, and outliers per group. | To compare numerical distributions between categories. |
| **Violin Plot by Category** | Continuous vs Categorical | Shows density and shape differences across categories. | When you want more detail than boxplot. |
| **Swarm / Strip Plot** | Continuous vs Categorical | Plots all data points to show distribution and overlap. | For small datasets or when showing actual points helps. |

---

## 4. Summary: Choosing the Right Plot

| Goal | Best Charts |
|------|--------------|
| **Compare Categories** | Bar Plot, Grouped Bar, Stacked Bar |
| **Show Distribution** | Histogram, Boxplot, Violin Plot |
| **Find Relationships** | Scatter Plot, Line Plot, Pair Plot |
| **Show Composition** | Pie Chart, Treemap, Stacked Bar |
| **Analyze Time Trends** | Line Plot, Area Chart, Time-Series Bar |
| **Explore Correlations** | Heatmap, Pair Plot |

---

## 5. Practical Notes
- **Categorical Variables** → summarized with counts and proportions.
- **Continuous Variables** → summarized with mean, median, std, range, and visualized using histograms or boxplots.
- **Mix of Both** → use grouped visualizations (boxplot or barplot with hue).

---

## 6. Example (Python / Seaborn)
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Histogram for continuous data
sns.histplot(df['age'], bins=20, kde=True)

# Barplot for categorical data
sns.countplot(x='gender', data=df)

# Scatter plot for two continuous variables
sns.scatterplot(x='age', y='income', data=df)

# Boxplot for distribution by category
sns.boxplot(x='department', y='salary', data=df)

# Correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()
```

---

**In summary:**
Exploratory data visualization is about selecting the right chart for the right data type and analytical goal.
Use univariate plots to understand individual variables, bivariate plots to explore relationships, and multivariate plots to understand complex patterns across multiple variables.

---

## 📬 Contributing

Have an addition, correction, or idea for this guide (ML / Data Science / Data Analysis topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
