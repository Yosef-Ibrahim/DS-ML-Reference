# =============================================================================
# 🔄 Data Pipelines & DAG Orchestration Engine — Runnable Python Script
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import sys
import time

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

class CustomDAG:
    """A lightweight Python DAG Orchestrator demonstrating Airflow concepts."""
    def __init__(self, dag_id):
        self.dag_id = dag_id
        self.tasks = {}
        self.dependencies = {}
        self.xcom_store = {}

    def add_task(self, task_id, func):
        self.tasks[task_id] = func
        self.dependencies[task_id] = set()

    def set_dependency(self, upstream_task_id, downstream_task_id):
        if downstream_task_id in self.dependencies:
            self.dependencies[downstream_task_id].add(upstream_task_id)

    def execute(self):
        print(f"[+] Starting Execution for DAG: '{self.dag_id}'")
        completed = set()
        
        while len(completed) < len(self.tasks):
            progress_made = False
            for task_id, func in self.tasks.items():
                if task_id not in completed:
                    # Check if all upstream tasks are completed
                    upstream_tasks = self.dependencies[task_id]
                    if upstream_tasks.issubset(completed):
                        print(f"  --> Executing Task: [{task_id}] (Upstream satisfied: {list(upstream_tasks)})")
                        result = func(self.xcom_store)
                        if result is not None:
                            self.xcom_store[task_id] = result
                        completed.add(task_id)
                        progress_made = True
                        
            if not progress_made:
                print("❌ Deadlock Detected! Circular dependency in DAG.")
                break
                
        print(f"[SUCCESS] DAG '{self.dag_id}' Finished Execution. Final XCom Store: {self.xcom_store}\n")

# --- Task Functions ---
def fetch_weather_task(xcom):
    print("      [Weather API] Extracting forecast data for Cairo...")
    return {"city": "Cairo", "temp": 32.5}

def fetch_sales_task(xcom):
    print("      [Sales DB] Querying historical umbrella sales...")
    return {"umbrella_units": 150}

def combine_data_task(xcom):
    weather = xcom.get('fetch_weather')
    sales = xcom.get('fetch_sales')
    print(f"      [ETL Combine] Merged Weather ({weather['temp']}C) with Sales ({sales['umbrella_units']} units)")
    return {"merged_rows": 1000}

def train_model_task(xcom):
    combined = xcom.get('combine_data')
    print(f"      [ML Train] Training model on {combined['merged_rows']} records...")
    return {"model_accuracy": 0.94}

def main():
    dag = CustomDAG("umbrella_demand_pipeline")
    
    # Register Tasks
    dag.add_task("fetch_weather", fetch_weather_task)
    dag.add_task("fetch_sales", fetch_sales_task)
    dag.add_task("combine_data", combine_data_task)
    dag.add_task("train_model", train_model_task)
    
    # Define Graph Dependencies:
    # fetch_weather \
    #                --> combine_data --> train_model
    # fetch_sales   /
    dag.set_dependency("fetch_weather", "combine_data")
    dag.set_dependency("fetch_sales", "combine_data")
    dag.set_dependency("combine_data", "train_model")
    
    # Run Orchestrator
    dag.execute()

if __name__ == "__main__":
    main()
