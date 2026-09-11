# DS-ML-Reference

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

> A structured, example-driven reference for Data Analysis, Data Science,
> Machine Learning, Deep Learning, Agentic AI, and Data Engineering.

## 1. What happened in this repository?

This repository started as a collection of course PDFs, slide decks, notebooks,
and small exercises. It is being converted into a public learning reference
without throwing away the original teaching material:

1. **Source preservation:** PDFs, PPTX files, datasets, and original notebooks
   remain available in the normalized source folders so every explanation can be
   traced back to the material it came from.
2. **Curriculum separation:** unrelated subjects are no longer mixed together.
   Linear algebra and statistics support the Data Science foundation; classical
   Machine Learning and Deep Learning live in the modeling track; Data
   Engineering remains its own sequential curriculum.
3. **Readable conversion:** every important source group gets a Markdown guide
   explaining the concepts, formulas, workflow, file mapping, prerequisites,
   practical use, and any correction made to the source.
4. **Runnable learning:** when a topic is computational, matching Python and/or
   notebook examples are provided. Cloud and service-dependent material is
   documented honestly rather than pretending it can run without credentials.
5. **Progressive learning:** each track has a recommended order, so a learner
   knows what to study first and why a later folder depends on an earlier one.

## 2. Repository architecture

```text
DS-ML-Reference/
├── README.md
├── Libraries/
├── Data analysis using python/
│   ├── Guides/
│   └── Medical risk eda/
├── data-science/
│   ├── README.md
│   ├── linear-algebra/
│   │   ├── README.md
│   │   ├── Linear_Algebra_Reference.md
│   │   └── pdfs/
│   └── statistics/
│       ├── README.md
│       ├── Statistics_Reference.md
│       └── pdfs/
├── machine-learning/
│   ├── README.md
│   ├── iti/                         # One complete classical ML curriculum
│   │   ├── foundations/
│   │   ├── supervised/
│   │   ├── unsupervised/
│   │   ├── evaluation/
│   │   ├── projects/
│   │   ├── examples/
│   │   └── reference/
│   └── deep-learning/               # ANN and CNN curriculum
│       ├── README.md
│       ├── ann/
│       ├── cnn/
│       └── reference/
├── data-engineering/
│   ├── Data_Engineering_Roadmap.md
│   ├── 01-fundamentals/ ... 15-performance-tricks/
│   └── projects/
├── agentic-ai/
│   ├── README.md
│   ├── overview.md
│   ├── resources.md
│   ├── workflow.md
│   └── projects/
│       ├── 01-rag-hr-assistant/
│       ├── 02-analysis-agent-chatbi/
│       └── 03-deep-research-agent/
├── projects/                          # Cross-track project index
└── (original source drops removed after normalization)
```

The original source drops were used as input and then removed from the public
root after normalization. This avoids four competing copies of the same
curriculum. Source PDFs, slide decks, datasets, and selected notebooks that are
needed for provenance remain in the relevant `pdfs/`, `reference/`, `data/`, and
`notebooks/` directories beside the normalized explanations. The guides retain
the original filenames and source mapping so credits and traceability are not
lost.

## 3. Which track should I follow?

| Track | Start here | What it answers |
|---|---|---|
| Data Analysis | [`Data analysis using python/Guides/`](<./Data analysis using python/Guides/>) | How do I inspect, clean, summarize, and communicate data? |
| Data Science foundations | [`data-science/`](./data-science/) | What mathematical and statistical ideas make modeling reliable? |
| Machine Learning | [`machine-learning/`](./machine-learning/) | How do I train, evaluate, compare, and deploy predictive models? |
| Machine Learning + Deep Learning | [`machine-learning/`](./machine-learning/) | How do I prepare data, train/evaluate classical models, then progress to ANN/CNN? |
| Data Engineering | [`data-engineering/Data_Engineering_Roadmap.md`](./data-engineering/Data_Engineering_Roadmap.md) | How do I build reliable systems that collect, transform, store, and serve data? |
| Agentic AI | [`agentic-ai/`](./agentic-ai/) | How do I build RAG, ChatBI, and deep-research agents with tools, memory, and evaluation? |

### Recommended complete order

```text
Python → NumPy/Pandas → Data Analysis
       → Linear Algebra → Statistics
       → Classical Machine Learning → Deep Learning
       → Agentic AI (RAG → ChatBI → Deep Research)
       → Data Engineering in parallel for production systems
```

Linear algebra explains vectors, matrices, transformations, and optimization.
Statistics explains distributions, variability, correlation, regression, and
uncertainty. Together they make model behavior understandable instead of
turning machine learning into a collection of APIs.

## 4. Data Science foundations

### Linear Algebra

The [`linear-algebra/`](./data-science/linear-algebra/) track reorganizes the
seven ITI PDFs into a progression:

1. Linear equations and geometric interpretation.
2. Vectors, vector operations, and geometric meaning.
3. Matrices and matrix operations.
4. Solving linear systems with inverses and elimination.
5. Special cases: no solution, one solution, and infinitely many solutions.
6. Eigenvalues and eigenvectors.

The guide connects each idea to feature representations, transformations,
least-squares regression, PCA, and neural-network layers.

### Statistics

The [`statistics/`](./data-science/statistics/) track converts the eleven ITI
lessons into:

1. Data description and graph selection.
2. Quartiles and interquartile range.
3. Variance, standard deviation, and z-scores.
4. Correlation and Pearson's coefficient.
5. Regression lines, best fit, and regression analysis.

The guide distinguishes association from causation, explains outlier handling,
and shows why statistical assumptions must be checked before trusting a metric.

## 5. Machine Learning and Deep Learning

The Machine Learning track is organized by the modeling problem rather than by
the accidental order of the source files:

- **Foundations and preprocessing:** train/test split, scaling, encoding,
  pipelines, leakage prevention, and reproducibility.
- **Supervised learning:** linear and polynomial regression, regularization,
  logistic regression, KNN, decision trees, ensembles, Naive Bayes, and SVM.
- **Unsupervised learning:** clustering, PCA, dimensionality reduction, and
  interpretation without labels.
- **Evaluation:** confusion matrices, precision/recall, ROC-AUC, regression
  error metrics, cross-validation, overfitting, and model selection.
- **Deep Learning:** ANN fundamentals, forward/backward propagation, activation
  functions, optimization, regularization, CNN convolution/pooling, and image
  workflows.

The [Machine Learning README](./machine-learning/README.md) maps the ITI
documents and notebooks to those categories. The [Deep Learning README](./machine-learning/deep-learning/README.md)
does the same for ANN and CNN sessions, datasets, and corrected runnable
examples.

## 6. Data Engineering

The [Data Engineering Roadmap](./data-engineering/Data_Engineering_Roadmap.md)
is a sequential 15-module curriculum:

| Stage | Outcome |
|---:|---|
| 01–03 | Concepts, data modeling, relational databases, and SQL |
| 04–07 | Advanced SQL, Python, Pandas, and performance-aware tabular work |
| 08–10 | Visualization, database/API integration, and pipeline orchestration |
| 11–13 | Spark, cloud foundations, and Azure data engineering |
| 14–15 | MLflow, optimization, and production readiness |

The [`data-engineering/projects/`](./data-engineering/projects/) suite applies
the curriculum to batch ETL, real-time fraud detection, and a cloud lakehouse.
Each project includes architecture, study checkpoints, source code, and a local
execution path.

Use the [`Projects Index`](./projects/README.md) to compare projects across
Data Engineering, Machine Learning, Agentic AI, and Data Analysis without searching through
lesson folders.

## 6b. Agentic AI

The [Agentic AI track](./agentic-ai/) covers LLM agents with tools, memory,
retrieval, and evaluation loops:

- **RAG HR Assistant:** PDF chunking, ChromaDB retrieval, cited answers, and "I don't know" discipline.
- **Analysis Agent (ChatBI):** NL-to-SQL with views/procedures/functions, safe execution, charts, and business reports.
- **Deep Research Agent:** Firecrawl research, reflexion, knowledge graph, SWOT, and scored opportunities.

Start from [`agentic-ai/overview.md`](./agentic-ai/overview.md), pick videos in
[`agentic-ai/resources.md`](./agentic-ai/resources.md) (including Bakrianoo Mini-RAG),
then work through [`agentic-ai/projects/`](./agentic-ai/projects/) Level 1 → 3 with
[`agentic-ai/workflow.md`](./agentic-ai/workflow.md) for logging, Docker, and evaluation.

## 7. File-format policy

| File | Role |
|---|---|
| `.md` | Detailed explanation, source mapping, formulas, decisions, and checklists |
| `.py` | Headless executable reference for local experimentation |
| `.ipynb` | Interactive explanation with Markdown and code cells |
| `.sql` | Database schema, transformations, and analytical queries |
| `.pdf` / `.pptx` | Preserved source material, not silently replaced |
| Dataset files | Small teaching inputs kept beside the example that uses them |

Not every conceptual file receives artificial code. A mathematical explanation
or cloud architecture guide remains Markdown-only when adding a script would
hide important assumptions or require an external service.

## 8. Validation and trust

Generated notebooks are checked as valid JSON, Python references are compiled
and locally executed where dependencies permit, SQL examples are tested against
SQLite when compatible, and relative Markdown links are audited. Optional
libraries such as TensorFlow, PySpark, Airflow, and MLflow are imported lazily
or documented as prerequisites; no credentials are stored in the repository.

When a source contains a wrong variable, malformed notebook cell, misleading
assumption, or incomplete section, the cleaned guide records an explicit
`⚠️ Correction` note rather than silently changing history.

## 📬 Contributing

Have an addition, correction, or better example for ML, Data Science, Data
Analysis, or Data Engineering? Please contact:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
