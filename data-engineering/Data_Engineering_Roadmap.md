# 🧭 Data Engineering Roadmap

**Author:** Youssef Ibrahim Mohamed Soliman  
**GitHub:** https://github.com/Yosef-Ibrahim  
**Email:** youssefibrahimelisely@gmail.com  
**Phone:** 01119834356

> This track moves from concepts and relational foundations to distributed,
> cloud, MLOps, optimization, and production projects. Read the numbered folders
> in order; each stage assumes the previous one.

## 1. Recommended Reading Order

| Step | Folder | Focus | Prerequisite |
|---:|---|---|---|
| 01 | [`01-fundamentals/`](./01-fundamentals/DE_Fundamentals.md) | DE lifecycle, roles, ETL, data types, and storage | None |
| 02 | [`02-data-modeling-and-databases/`](./02-data-modeling-and-databases/Data_Modeling_Databases.md) | Relational models, keys, normalization, facts, and dimensions | 01 |
| 03 | [`03-sql/`](./03-sql/SQL_Reference.md) | SQL querying, joins, aggregation, windows, and Python access | 01–02 |
| 04 | [`04-advanced-sql/`](./04-advanced-sql/Advanced_SQL.md) | CTEs, views, procedures, triggers, UDFs, windows, and cursors | 03 |
| 05 | [`05-python-fundamentals/`](./05-python-fundamentals/Python_Fundamentals.md) | Python foundations for robust automation | 03 |
| 06 | [`06-pandas/`](./06-pandas/Pandas_Reference.md) | DataFrames, cleaning, grouping, merging, and I/O | 05 |
| 07 | [`07-advanced-pandas/`](./07-advanced-pandas/Advanced_Pandas.md) | Method chains, transforms, memory, and Parquet | 06 |
| 08 | [`08-visualization-matplotlib-seaborn/`](./08-visualization-matplotlib-seaborn/Matplotlib_Seaborn.md) | Visualization and EDA communication | 06 |
| 09 | [`09-python-db-apis/`](./09-python-db-apis/Python_DB_APIs.md) | Drivers, SQLAlchemy, APIs, retries, and rate limits | 03, 05 |
| 10 | [`10-data-pipelines/`](./10-data-pipelines/Data_Pipelines.md) | ETL/ELT, orchestration, loading, and observability | 01–09 |
| 11 | [`11-apache-spark/`](./11-apache-spark/Apache_Spark.md) | Distributed processing, Spark SQL, and tuning | 06, 10 |
| 12 | [`12-cloud-foundations/`](./12-cloud-foundations/Cloud_Foundations.md) | Cloud service models, storage, compute, IAM, and security | 01–11 |
| 13 | [`13-azure-data-engineering/`](./13-azure-data-engineering/Azure_Data_Engineering.md) | ADLS Gen2, ADF, Databricks, and Synapse | 11–12 |
| 14 | [`14-mlflow/`](./14-mlflow/MLflow_Workshops.md) | Experiment tracking, registry, and reproducibility | 05, 11 |
| 15 | [`15-performance-tricks/`](./15-performance-tricks/Performance_Tricks.md) | Query, memory, partition, and Spark optimization | 03, 06, 11 |

## 2. How to Study Each Module

1. Read the Markdown guide completely and reproduce its diagrams and SQL mentally.
2. Run the `.py` companion in a clean environment where dependencies are available.
3. Open the `.ipynb` companion when one exists and change the sample inputs.
4. Compare the module's trade-offs with the source PDF retained in the same folder.
5. Complete the relevant checkpoint in the project suite before moving on.

The runnable examples use small deterministic data and avoid embedded credentials.
Cloud, Kafka, Spark, Airflow, and MLflow sections explicitly distinguish local
demonstrations from production deployment requirements.

## 3. Project Progression

| Project | Best time to start | Main skills |
|---|---|---|
| [`01-ecommerce-batch-etl/`](./projects/01-ecommerce-batch-etl/) | After 04, 06, 09, and 10 | SQL, dimensional modeling, idempotent batch loads |
| [`02-realtime-fraud-detection/`](./projects/02-realtime-fraud-detection/) | After 11 and 15 | Kafka, streaming windows, state, and anomaly detection |
| [`03-cloud-lakehouse-medallion/`](./projects/03-cloud-lakehouse-medallion/) | After 10, 12, 13, and 15 | Airflow, cloud storage, Spark quality gates, medallion layers |

Read the [`projects/README.md`](./projects/README.md) before choosing a project.
It maps every project task back to the curriculum and explains local, containerized,
and cloud execution paths.

## 4. Why This Order?

The sequence is intentional:

```text
Concepts → relational structure → SQL → Python/table tools → pipelines
         → distributed processing → cloud platforms → MLOps → optimization
```

Skipping the modeling and SQL foundations makes later Spark and cloud abstractions
harder to reason about. Optimization is last because reliable performance work
requires understanding the query plan, storage layout, and execution engine first.

## 📬 Contributing

Have an addition, correction, or idea for this roadmap (ML / Data Science /
Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
