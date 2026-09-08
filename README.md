# DS-ML-Reference

A growing, practical reference repo for anyone working (or starting out) in **Data Science, Data Analysis, Machine Learning, and Data Engineering**.

## 🎯 Purpose

This repo is **not just a library cheat-sheet**. The goal is bigger than that: to build a set of clear, well-explained, example-driven references that actually help someone understand *why* a tool or concept works the way it does — not just copy-paste syntax.

Each topic here is written to be useful for:
- **Beginners** who need a structured, from-scratch explanation with real examples
- **People preparing for interviews or coursework** who need a quick, accurate refresher
- **Anyone working on a real project** who needs a reliable reference they can trust and reuse

## 🏗️ Repo Architecture

The repo is split into different **kinds** of content, kept in separate top-level folders so they don't get mixed up:

| Folder | What goes here |
|---|---|
| **`libraries/`** | Tool-by-tool references. Each library gets its own folder covering its features in isolation (syntax, functions, small standalone examples) — not tied to any one dataset or real-world question. |
| **`data-analysis/`** | Two kinds of content: **`guides/`** — dataset-agnostic methodology (checklists, "which technique/chart do I use and when") — and full, real **case studies** applying that methodology end-to-end on one dataset. |
| **`data-engineering/`** | Numbered, ordered topic folders (fundamentals → data modeling → SQL → ...) forming a **roadmap** — the material builds on itself, so it's read in order rather than picked at random like `libraries/`. |
| **`data-science/`** *(coming soon)* | Statistics, hypothesis testing, feature engineering — the layer between analysis and modeling. |
| **`machine-learning/`** *(coming soon)* | Model building & evaluation (Scikit-learn, etc.) — where a project moves from "understanding the data" to "predicting something from it". |

**The simple rule for where something goes:**
- Teaching one library on its own, no fixed order → `libraries/`
- A general method/checklist not tied to any dataset → `data-analysis/guides/`
- A project answering a real question using a real dataset → the matching stage folder's case-study section (e.g. `data-analysis/medical-risk-eda/`)
- A structured course/curriculum where each topic builds on the last → a numbered folder under the matching stage (e.g. `data-engineering/01-fundamentals/`)

```
DS-ML-Reference/
├── README.md
│
├── libraries/
│   ├── numpy/
│   │   ├── Numpy.py
│   │   ├── NumPy_Reference.md
│   │   └── NumPy.ipynb
│   ├── pandas/
│   │   ├── Pandas.py
│   │   ├── Pandas_Reference.md
│   │   └── Pandas.ipynb
│   └── matplotlib_seaborn/
│       ├── Matplotlib_Seaborn.py
│       ├── Matplotlib_Seaborn_Reference.md
│       ├── Matplotlib_Seaborn.ipynb
│       └── employees.csv
│
├── data-analysis/
│   ├── guides/
│   │   ├── EDA_Methods_Reference.md
│   │   └── Data_Visualization_Guide.md
│   └── medical-risk-eda/
│       ├── Medical_Risk_EDA.py
│       ├── Medical_Risk_EDA_Reference.md
│       ├── Medical_Risk_EDA.ipynb
│       └── medical_data.csv
│
├── data-engineering/
│   ├── Data_Engineering_Roadmap.md
│   ├── 01-fundamentals/
│   │   └── DE_Fundamentals.md
│   ├── 02-data-modeling-and-databases/
│   │   └── Data_Modeling_Databases.md
│   ├── 03-sql/
│   │   └── SQL_Reference.md
│   └── 04-...+                 # more numbered folders added as course material comes in
│
├── data-science/            # placeholder for now
└── machine-learning/         # placeholder for now
```

## 📂 What's Inside

Project/library topics come in **three formats** where a script makes sense:

| Format | Best for |
|---|---|
| `.md` | Reading top to bottom, or jumping straight to a section |
| `.py` | Running as a plain script and experimenting with the code |
| `.ipynb` | Running interactively, cell by cell — best for seeing tables and charts rendered live |

Pure **guides** and **conceptual course material** (dataset-agnostic checklists, decision references, theory) are `.md` only — there's no dataset or single script to "run," so a `.py`/`.ipynb` version wouldn't add anything.

### `libraries/`
| Library | Covers |
|---|---|
| **NumPy** | Arrays (1D–4D), indexing & slicing, broadcasting, reshaping, aggregations, linear algebra, sorting, saving/loading |
| **Pandas** | Series & DataFrames, exploring data, boolean indexing, `loc`/`iloc`, missing data, groupby, `apply`, loading/saving data, working with dates, sorting |
| **Matplotlib & Seaborn** | Line/scatter/bar plots, histograms, multi-plot figures, distribution plots, categorical counts, correlation heatmaps, pie charts, saving plots |

### `data-analysis/guides/`
| Guide | Covers |
|---|---|
| **EDA Methods Reference** | The 10-step EDA checklist: peek, shape/index, dtypes/info, describe, missing values, duplicates, cardinality, correlations, groupby, outlier scanning |
| **Data Visualization Guide** | How to pick the right chart: data types (categorical/numerical), univariate/bivariate/multivariate, and a chart-selection table by analytical goal |

### `data-analysis/` (case studies)
| Project | What it's about |
|---|---|
| **Medical Risk EDA** | A 1000-patient clinical dataset (demographics, lifestyle, vitals, outcomes). A full walkthrough of univariate → bivariate → categorical → multivariate analysis, ending in a correlation matrix and pairplot — the kind of analysis that precedes a real health-risk prediction project. |

### `data-engineering/` (read in order — see [`Data_Engineering_Roadmap.md`](./data-engineering/Data_Engineering_Roadmap.md))
| Step | Covers |
|---|---|
| **01 — Fundamentals** | What data engineering is, the DE lifecycle, roles & titles, ETL, types of data, storage systems, a real-world (Uber) case study |
| **02 — Data Modeling & Databases** | Data models, databases, primary/foreign keys, relationships, fact & dimension tables |
| **03 — SQL** | RDBMS, database design process, full SQL syntax — CRUD, filtering, ordering, aggregates, grouping, datetime ops, joins, subqueries, window functions, Python + MySQL |

## 🧭 How to Use This Repo

- Each `.md` file is a self-contained, readable reference — read it top to bottom or jump to the section you need.
- Each `.py` / `.ipynb` file is meant to be **run and experimented with**, not just read — change the values, break things, see what happens.
- Some folders include a small dataset (`.csv`) used by the examples — keep it in the same folder as the code so the file paths resolve correctly.
- `libraries/` and `data-analysis/guides/` are reference material — jump in wherever you need. `data-engineering/` is a curriculum — read its numbered folders in order, starting from the roadmap file.
- Code and comments are kept in **English** for consistency and easier searchability, regardless of the explanation language used elsewhere.

## 🤝 Contributing

Got an idea, a correction, a missing topic, or a better example? This repo is meant to grow with input from anyone in the field — contributions are welcome.

Reach out directly:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 [github.com/Yosef-Ibrahim](https://github.com/Yosef-Ibrahim)

## 📜 License

Free to use for learning purposes. Attribution appreciated if you reuse or redistribute significant parts of it.
