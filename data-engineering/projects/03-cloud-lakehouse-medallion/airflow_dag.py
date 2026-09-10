"""
Optional Airflow orchestration wrapper for the local medallion ETL.

Author: Youssef Ibrahim Mohamed Soliman
GitHub: https://github.com/Yosef-Ibrahim
Email: youssefibrahimelisely@gmail.com

Airflow is imported lazily so this file can be linted and inspected without
installing Airflow. Airflow itself imports this module only in an Airflow
environment.
"""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path


def build_dag():
    try:
        from airflow import DAG
        from airflow.operators.python import PythonOperator
    except ImportError as exc:
        raise RuntimeError("airflow_dag.py requires Apache Airflow to build the DAG") from exc

    project_dir = Path(__file__).resolve().parent
    input_path = Path(os.environ.get("LAKEHOUSE_INPUT", project_dir / "sample_events.jsonl"))
    root_path = Path(os.environ.get("LAKEHOUSE_ROOT", project_dir / "lakehouse"))

    def execute_etl() -> None:
        from medallion_etl import ensure_sample, run_pipeline

        ensure_sample(input_path)
        run_pipeline(input_path, root_path)

    with DAG(
        dag_id="cloud_lakehouse_medallion",
        start_date=datetime(2026, 1, 1),
        schedule="@daily",
        catchup=False,
        tags=["data-engineering", "lakehouse"],
    ) as dag:
        PythonOperator(
            task_id="run_bronze_silver_gold",
            python_callable=execute_etl,
            retries=2,
        )
    return dag


try:
    dag = build_dag()
except RuntimeError:
    dag = None
