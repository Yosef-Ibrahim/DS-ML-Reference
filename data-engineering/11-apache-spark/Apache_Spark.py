# =============================================================================
# ⚡ Apache Spark & PySpark — Headless Executable Script
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import sys
import os

# Set Python worker to match driver executable
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def run_pyspark_demo():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, avg, max, rank
    from pyspark.sql.window import Window
    from pyspark.sql.types import StructType, StructField, StringType, DoubleType

    print("[+] Initializing PySpark Session (local mode)...")
    spark = SparkSession.builder \
        .appName("DEPI-PySpark-Demo") \
        .master("local[2]") \
        .config("spark.sql.shuffle.partitions", "2") \
        .getOrCreate()

    # 1. Schema Definition & DataFrame Creation
    schema = StructType([
        StructField("emp_id", StringType(), False),
        StructField("name", StringType(), True),
        StructField("department", StringType(), True),
        StructField("salary", DoubleType(), True)
    ])

    data = [
        ("E101", "Alice", "IT", 75000.0),
        ("E102", "Bob", "HR", 50000.0),
        ("E103", "Charlie", "IT", 82000.0),
        ("E104", "David", "HR", 53000.0),
        ("E105", "Eve", "Finance", 90000.0)
    ]

    df = spark.createDataFrame(data, schema=schema)
    print("\n--- 1. Raw PySpark DataFrame ---")
    df.show()

    # 2. Transformations & Aggregations
    print("--- 2. Average Salary by Department ---")
    dept_summary = df.groupBy("department").agg(
        avg("salary").alias("avg_salary"),
        max("salary").alias("max_salary")
    )
    dept_summary.show()

    # 3. Window Function Ranking
    print("--- 3. Window Function: Salary Rank by Department ---")
    window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
    ranked_df = df.withColumn("dept_rank", rank().over(window_spec))
    ranked_df.show()

    spark.stop()
    print("[SUCCESS] PySpark Demo Executed Successfully!")

def main():
    try:
        run_pyspark_demo()
    except Exception as e:
        print(f"[!] PySpark execution notice: {e}")

if __name__ == "__main__":
    main()
