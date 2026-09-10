# ⚡ Apache Spark & PySpark — Distributed Big Data Processing Reference

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Apache Spark: An Introduction to Big Data Processing with PySpark* course material (Rowad Misr Al-Raqmeya).

---

## 📑 Table of Contents
1. [What is Apache Spark? (Spark vs. Hadoop MapReduce)](#1-what-is-apache-spark)
2. [Apache Spark Ecosystem (Spark SQL, Streaming, MLlib, GraphX)](#2-apache-spark-ecosystem)
3. [Cluster Architecture & Runtime Components (Driver, Executors, YARN/K8s)](#3-cluster-architecture--runtime-components)
4. [Spark Entry Points (SparkContext vs. SparkSession)](#4-spark-entry-points)
5. [Resilient Distributed Datasets (RDDs)](#5-resilient-distributed-datasets-rdds)
6. [Lazy Evaluation: Transformations vs. Actions](#6-lazy-evaluation-transformations-vs-actions)
7. [PySpark DataFrame API & StructType Schemas](#7-pyspark-dataframe-api--structtype-schemas)
8. [DAG Scheduler, Stages & Shuffling](#8-dag-scheduler-stages--shuffling)
9. [PySpark SQL Functions, GroupBy & Windowing](#9-pyspark-sql-functions-groupby--windowing)
10. [PySpark User-Defined Functions (UDFs)](#10-pyspark-user-defined-functions-udfs)

---

## 1) What is Apache Spark?

**Apache Spark** is a multi-language, unified engine for large-scale distributed data processing.

```
+--------------------------------------------------------------------+
|                         Apache Spark API                           |
|       (Python / Scala / Java / R / ANSI SQL / Pandas on Spark)      |
+--------------------------------------------------------------------+
|  Spark SQL   |  Spark Streaming  |    MLlib     |    GraphX     |
+--------------------------------------------------------------------+
|                        Spark Core Engine                           |
|               (RDDs, DAG Scheduler, Memory Manager)                |
+--------------------------------------------------------------------+
|                   Cluster Resource Managers                        |
|            (YARN / Kubernetes / Standalone Cluster)               |
+--------------------------------------------------------------------+
```

### Spark vs. Hadoop MapReduce
* **In-Memory Computing**: MapReduce writes intermediate results to disk after every Map/Reduce phase. Spark keeps intermediate partitions in RAM, yielding up to **100x faster execution**.
* **Unified Pipeline Engine**: Combines batch ETL, real-time streaming, machine learning, and interactive SQL under a single engine framework.

---

## 2) Apache Spark Ecosystem

* **Spark Core**: Base engine handling memory management, fault recovery, and task scheduling.
* **Spark SQL**: Distributed ANSI SQL execution engine for structured DataFrames.
* **Spark Structured Streaming**: Real-time micro-batching and event-time processing engine.
* **MLlib**: Scalable machine learning algorithms (VectorAssembler, Random Forests, K-Means).
* **GraphX**: Graph computation engine for network connectivity algorithms.

---

## 3) Cluster Architecture & Runtime Components

```
+------------------------------------+
|           Driver Program           |
|  (SparkSession / DAG Scheduler)    |
+-----------------+------------------+
                  |
                  v
+-----------------+------------------+
|         Cluster Manager            |
|    (YARN / Kubernetes / Standalone)|
+---------+----------------+---------+
          |                |
          v                v
+---------+------+   +-----+---------+
|  Worker Node 1 |   |  Worker Node 2|
| +------------+ |   | +------------+|
| | Executor   | |   | | Executor   ||
| | (Tasks)    | |   | | (Tasks)    ||
| +------------+ |   | +------------+|
+----------------+   +---------------+
```

1. **Driver Program**: Runs the client code, maintains `SparkSession`, translates operations into a DAG execution plan, and negotiates with the Cluster Manager.
2. **Cluster Manager**: Allocates compute resources across the cluster (YARN, Kubernetes, Standalone).
3. **Executors**: Worker processes that store data partitions in RAM/disk and run physical compute tasks.

---

## 4) Spark Entry Points

* **`SparkContext`** (`sc`): Low-level entry point used for RDD-based operations.
* **`SparkSession`** (`spark`): Modern unified entry point for structured DataFrames and SQL queries.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DEPI-Spark-Reference") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

sc = spark.sparkContext
```

---

## 5) Resilient Distributed Datasets (RDDs)

An **RDD** is an immutable, fault-tolerant, partitioned collection of records distributed across cluster nodes. Fault tolerance is guaranteed through **lineage graphs** (recomputing missing partitions if a worker fails).

```python
# Create RDD from Python list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Read external text file as RDD
file_rdd = sc.textFile("hdfs://cluster/logs/app.log")
```

---

## 6) Lazy Evaluation: Transformations vs. Actions

Spark defers execution until an **Action** is explicitly called.

### Transformations (Lazy)
Build an execution plan (DAG) without running computation:
`map()`, `filter()`, `flatMap()`, `groupByKey()`, `reduceByKey()`

### Actions (Eager)
Trigger physical execution across the cluster and return results:
`collect()`, `count()`, `first()`, `take(n)`, `saveAsTextFile()`

```python
# Transformations (Lazy - Nothing executes yet)
squared_rdd = rdd.map(lambda x: x ** 2)
filtered_rdd = squared_rdd.filter(lambda x: x > 10)

# Action (Triggers execution and returns Python list)
results = filtered_rdd.collect()
print("Collected Results:", results)
```

---

## 7) PySpark DataFrame API & Schemas

DataFrames add a named columnar schema over RDDs, allowing Catalyst Optimizer query optimizations.

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Explicit Schema Definition
custom_schema = StructType([
    StructField("emp_id", StringType(), False),
    StructField("name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("salary", DoubleType(), True)
])

# Create DataFrame
data = [
    ("E101", "Alice", "IT", 75000.0),
    ("E102", "Bob", "HR", 50000.0),
    ("E103", "Charlie", "IT", 82000.0)
]
df = spark.createDataFrame(data, schema=custom_schema)
df.show()
```

---

## 8) DAG Scheduler, Stages & Shuffling

1. **DAG Scheduler**: Splits the job into physical **Stages** based on shuffle boundaries.
2. **Narrow Transformations**: Operations like `map()` or `filter()` where child partitions depend on a single parent partition (no data movement across network).
3. **Wide Transformations (Shuffling)**: Operations like `groupBy()`, `join()`, or `distinct()` where data from multiple partitions across the network must be regrouped.

---

## 9) PySpark SQL Functions, GroupBy & Windowing

```python
from pyspark.sql.functions import col, avg, max, rank
from pyspark.sql.window import Window

# 1. Column Transformations & Filtering
filtered_df = df.filter(col("salary") >= 60000) \
                .withColumn("salary_after_bonus", col("salary") * 1.10)

# 2. GroupBy Aggregations
dept_summary = df.groupBy("department").agg(
    avg("salary").alias("avg_dept_salary"),
    max("salary").alias("max_dept_salary")
)

# 3. Window Ranking
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
ranked_df = df.withColumn("dept_rank", rank().over(window_spec))
ranked_df.show()
```

---

## 10) PySpark User-Defined Functions (UDFs)

```python
from pyspark.sql.functions import udf

def add_title_prefix(name):
    return f"Mr/Ms. {name}"

# Register UDF
prefix_udf = udf(add_title_prefix, StringType())

# Apply UDF to DataFrame
formatted_df = df.withColumn("formatted_name", prefix_udf(col("name")))
formatted_df.show()
```

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
