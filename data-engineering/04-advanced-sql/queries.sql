-- =============================================================================
-- Advanced SQL for Data Engineers — Runnable SQL Queries Script
-- Author: Youssef Ibrahim Mohamed Soliman
-- GitHub: https://github.com/Yosef-Ibrahim
-- Email:  youssefibrahimelisely@gmail.com
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. Table Setup & Data Population
-- -----------------------------------------------------------------------------
DROP TABLE IF EXISTS audit_log;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS job_grades;

CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    emp_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    dept_id INT,
    supervisorID VARCHAR(10),
    FOREIGN KEY (dept_id) REFERENCES departments(id)
);

CREATE TABLE job_grades (
    grade CHAR(1) PRIMARY KEY,
    lowsal DECIMAL(10,2),
    highsal DECIMAL(10,2)
);

CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    action VARCHAR(50),
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO departments VALUES (100, 'IT'), (200, 'Marketing'), (300, 'HR');

INSERT INTO job_grades VALUES ('C', 1000.00, 3500.00), ('B', 3500.01, 7000.00), ('A', 7000.01, 15000.00);

INSERT INTO employees VALUES
('1122', 'Ahmed Ali', 5000.00, 100, '2233'),
('2233', 'Kamel Mohamed', 8500.00, 100, '1234'),
('1234', 'Hanaa Sobhy', 9000.00, 200, '2233'),
('3216', 'Amr Omran', 3000.00, 100, NULL),
('9685', 'Noha Mohamed', 4200.00, 200, '2233');

-- -----------------------------------------------------------------------------
-- 2. Advanced Joins
-- -----------------------------------------------------------------------------
-- Equi-Join
SELECT e.name AS Employee_Name, d.name AS Department_Name
FROM employees e
JOIN departments d ON e.dept_id = d.id;

-- Non-Equi Join
SELECT e.name, e.salary, j.grade
FROM employees e
JOIN job_grades j ON e.salary BETWEEN j.lowsal AND j.highsal;

-- Self Join
SELECT e.name AS Employee, s.name AS Supervisor
FROM employees e
LEFT JOIN employees s ON e.supervisorID = s.emp_id;

-- Outer Join (Right Outer Join)
SELECT e.name AS Employee, d.id AS Dept_ID, d.name AS Department
FROM employees e
RIGHT OUTER JOIN departments d ON e.dept_id = d.id;

-- -----------------------------------------------------------------------------
-- 3. Window Functions
-- -----------------------------------------------------------------------------
SELECT name, salary, dept_id,
       AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg_salary,
       RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dept_salary_rank,
       LEAD(salary, 1) OVER (ORDER BY salary DESC) AS next_lower_salary
FROM employees;

-- -----------------------------------------------------------------------------
-- 4. CTEs (Common Table Expressions)
-- -----------------------------------------------------------------------------
WITH HighEarnerEmployees AS (
    SELECT emp_id, name, salary, dept_id
    FROM employees
    WHERE salary >= 5000.00
),
DeptAggregates AS (
    SELECT dept_id, COUNT(*) AS high_earner_count
    FROM HighEarnerEmployees
    GROUP BY dept_id
)
SELECT d.name AS Department_Name, da.high_earner_count
FROM DeptAggregates da
JOIN departments d ON da.dept_id = d.id;

-- -----------------------------------------------------------------------------
-- 5. Views
-- -----------------------------------------------------------------------------
CREATE OR REPLACE VIEW vw_high_earners AS
SELECT name, salary, dept_id
FROM employees
WHERE salary >= 5000.00;

SELECT * FROM vw_high_earners;
