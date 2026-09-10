# =============================================================================
# ⚡ Advanced SQL for Data Engineers — Runnable Python Script (SQLite Engine)
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import sqlite3
import sys

# Ensure UTF-8 output encoding for Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def print_table(title, cursor, query):
    print(f"--- {title} ---")
    cursor.execute(query)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    
    # Print header
    header = " | ".join(f"{col:<18}" for col in columns)
    print(header)
    print("-" * len(header))
    
    # Print rows
    for row in rows:
        print(" | ".join(f"{str(val):<18}" for val in row))
    print("\n")

def main():
    print("[+] Initializing In-Memory SQLite Database for Advanced SQL Reference...\n")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # 1. Table Creation
    cursor.executescript("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE employees (
        emp_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL NOT NULL,
        dept_id INTEGER,
        supervisorID TEXT
    );

    CREATE TABLE job_grades (
        grade TEXT PRIMARY KEY,
        lowsal REAL,
        highsal REAL
    );

    INSERT INTO departments VALUES (100, 'IT'), (200, 'Marketing'), (300, 'HR');

    INSERT INTO job_grades VALUES 
    ('C', 1000.0, 3500.0), 
    ('B', 3500.01, 7000.0), 
    ('A', 7000.01, 15000.0);

    INSERT INTO employees VALUES
    ('1122', 'Ahmed Ali', 5000.0, 100, '2233'),
    ('2233', 'Kamel Mohamed', 8500.0, 100, '1234'),
    ('1234', 'Hanaa Sobhy', 9000.0, 200, '2233'),
    ('3216', 'Amr Omran', 3000.0, 100, NULL),
    ('9685', 'Noha Mohamed', 4200.0, 200, '2233');
    """)
    conn.commit()

    # 2. Equi-Join Query
    print_table(
        "1. Equi-Join (Employees & Departments)",
        cursor,
        """
        SELECT e.emp_id, e.name AS employee_name, d.name AS dept_name, e.salary
        FROM employees e
        JOIN departments d ON e.dept_id = d.id;
        """
    )

    # 3. Non-Equi Join Query
    print_table(
        "2. Non-Equi Join (Salary Grades)",
        cursor,
        """
        SELECT e.name, e.salary, j.grade
        FROM employees e
        JOIN job_grades j ON e.salary BETWEEN j.lowsal AND j.highsal;
        """
    )

    # 4. Self Join
    print_table(
        "3. Self Join (Employee & Supervisor)",
        cursor,
        """
        SELECT e.name AS employee_name, COALESCE(s.name, 'No Supervisor') AS supervisor_name
        FROM employees e
        LEFT JOIN employees s ON e.supervisorID = s.emp_id;
        """
    )

    # 5. Window Functions
    print_table(
        "4. Window Functions (Partition & Rank)",
        cursor,
        """
        SELECT name, salary, dept_id,
               AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg_salary,
               DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dept_rank
        FROM employees;
        """
    )

    # 6. CTE
    print_table(
        "5. Common Table Expression (CTE)",
        cursor,
        """
        WITH HighEarners AS (
            SELECT emp_id, name, salary, dept_id
            FROM employees
            WHERE salary >= 5000
        )
        SELECT d.name AS department, COUNT(h.emp_id) AS high_earner_count
        FROM HighEarners h
        JOIN departments d ON h.dept_id = d.id
        GROUP BY d.name;
        """
    )

    conn.close()
    print("[SUCCESS] Advanced SQL Python Script Executed Successfully!")

if __name__ == "__main__":
    main()
