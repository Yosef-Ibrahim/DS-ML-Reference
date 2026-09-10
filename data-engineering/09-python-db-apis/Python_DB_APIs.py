# =============================================================================
# 🔌 Python for Databases & APIs — Runnable Python Script
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import sqlite3
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def main():
    print("[+] Executing Python Database & API Connectivity Reference Script...\n")

    # 1. SQLite Database Ingestion & Querying
    print("--- 1. SQLite Ingestion & Querying ---")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE pipeline_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pipeline_name TEXT NOT NULL,
        status TEXT NOT NULL,
        records_processed INTEGER
    );
    """)

    logs = [
        ('batch_etl_ecommerce', 'SUCCESS', 15000),
        ('realtime_fraud_stream', 'SUCCESS', 84000),
        ('cloud_lakehouse_sync', 'FAILED', 0)
    ]

    cursor.executemany("""
    INSERT INTO pipeline_logs (pipeline_name, status, records_processed)
    VALUES (?, ?, ?);
    """, logs)
    conn.commit()

    cursor.execute("SELECT * FROM pipeline_logs WHERE status = 'SUCCESS';")
    successful_runs = cursor.fetchall()
    print("Successful Pipeline Runs:\n", successful_runs, "\n")

    conn.close()

    # 2. Mock REST API Endpoint Simulation
    print("--- 2. REST API Request / Response Simulation ---")
    mock_payload = {"pipeline": "ecommerce_batch", "processed_records": 15000, "status": "200 OK"}
    print(f"Mock API JSON Response: {mock_payload}\n")

    print("[SUCCESS] Python Database & API Script Executed Successfully!")

if __name__ == "__main__":
    main()
