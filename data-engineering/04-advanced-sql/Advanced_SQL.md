# ⚡ Advanced SQL for Data Engineers — Complete Reference

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Advanced SQL for Data Engineer* course material (Rowad Misr Al-Raqmeya). Builds directly on [`../03-sql/SQL_Reference.md`](../03-sql/SQL_Reference.md).
>
> ⚠️ **Note:** The original course slides provided brief syntax templates for complex topics like Stored Procedures, Triggers, Window Functions, and Cursors. This reference expands every slide topic with comprehensive explanations, edge cases, production performance trade-offs, and runnable MySQL/PostgreSQL queries.

---

## 📑 Table of Contents
1. [Types of Table Joins (Equi, Non-Equi, Self, Outer)](#1-types-of-table-joins)
2. [Subqueries (Nested, Correlated & Inline Views)](#2-subqueries-nested-correlated--inline-views)
3. [Set Operators (UNION & UNION ALL)](#3-set-operators-union--union-all)
4. [Views & Check Options](#4-views--check-options)
5. [Built-in SQL Functions (Scalar, Aggregate, String, Math, Date)](#5-built-in-sql-functions)
6. [Stored Procedures](#6-stored-procedures)
7. [Database Triggers](#7-database-triggers)
8. [User-Defined Functions (UDFs)](#8-user-defined-functions-udfs)
9. [Window Functions (Aggregate, Value, Rank)](#9-window-functions-aggregate-value-rank)
10. [Common Table Expressions (CTEs)](#10-common-table-expressions-ctes)
11. [Database Indexes & Performance](#11-database-indexes--performance)
12. [Cursors vs. Set-Based SQL](#12-cursors-vs-set-based-sql)

---

## 1) Types of Table Joins

In relational databases, joins combine columns from one or more tables based on logical relationships.

### A) Equi-Join vs. Non-Equi Join
* **Equi-Join**: Joins tables based on exact equality comparison (`=`) between Primary Key (PK) and Foreign Key (FK).
  ```sql
  SELECT e.fname, e.lname, d.dname
  FROM employee e
  JOIN department d ON e.dno = d.dnumber;
  ```
* **Non-Equi Join**: Joins tables using comparison operators other than equality (`<`, `>`, `BETWEEN ... AND ...`, `<>`).
  ```sql
  -- Salary grade lookup using a non-equi join
  SELECT e.name, e.salary, j.grade
  FROM employees e
  JOIN job_grades j ON e.salary BETWEEN j.lowsal AND j.highsal;
  ```

### B) Self Join
Joining a table to itself. Requires using distinct table aliases for the left and right instances.
```sql
-- Retrieve each employee's name alongside their supervisor's name
SELECT e.name AS Employee_Name, s.name AS Supervisor_Name
FROM employees e
JOIN employees s ON e.supervisorID = s.ID;
```

### C) Outer Joins (LEFT, RIGHT, FULL)
* **LEFT OUTER JOIN**: Returns all records from the left table, and matching records from the right table. Non-matching right rows return `NULL`.
* **RIGHT OUTER JOIN**: Returns all records from the right table, and matching records from the left table.
* **FULL OUTER JOIN**: Returns all records when there is a match in either left or right table.

```sql
-- Display all departments even if no employees are assigned
SELECT e.name AS Employee, d.dept_id, d.name AS Department
FROM employees e
RIGHT OUTER JOIN departments d ON e.dept_id = d.id;
```

---

## 2) Subqueries (Nested, Correlated & Inline Views)

A subquery is a `SELECT` query nested inside another SQL statement.

### A) Single-Row & Multi-Row Subqueries
* **Single-Row Subquery**: Returns a single value (`=`, `>`, `<`).
* **Multi-Row Subquery**: Returns multiple rows (`IN`, `ANY`, `ALL`).

```sql
-- Find employees earning more than ALL employees in department 5
SELECT Lname, Fname
FROM employee
WHERE salary > ALL (
    SELECT salary 
    FROM employee 
    WHERE Dno = 5
);
```

### B) Subquery in `FROM` (Inline View)
```sql
SELECT avg_dept.dno, avg_dept.avg_sal
FROM (
    SELECT Dno, AVG(salary) AS avg_sal
    FROM employee
    GROUP BY Dno
) AS avg_dept
WHERE avg_dept.avg_sal > 50000;
```

---

## 3) Set Operators (UNION & UNION ALL)

Set operators combine the result sets of two or more queries into a single result set.

* **`UNION`**: Combines results and **removes duplicate rows**.
* **`UNION ALL`**: Combines results **including duplicates** (significantly faster because no distinct sort/hash step is needed).

> ⚠️ **Rules for Set Operations**:
> 1. Both `SELECT` statements must return the exact same number of columns.
> 2. Corresponding columns must have compatible data types.

```sql
-- Combine active and retired employee rosters without duplicates
SELECT Name FROM Employees
UNION
SELECT Name FROM Employees_retired;
```

---

## 4) Views & Check Options

A **View** is a virtual table defined by a saved SQL query. It does not store physical data (except Materialized Views).

### Advantages of Views
1. **Security**: Restricts user access to specific columns or rows.
2. **Simplicity**: Encapsulates complex joins and aggregations into a single queryable name.
3. **Data Independence**: Abstracts underlying schema changes from applications.

### Creating & Modifying Views
```sql
-- Create a view for employee project hours
CREATE OR REPLACE VIEW vw_work_hrs AS
SELECT e.Fname, e.Lname, p.Pname, w.Hours
FROM Employee e
JOIN Works_on w ON e.SSN = w.ESSN
JOIN Project p ON w.PNO = p.PNUMBER
WHERE e.Dno = 5;
```

### `WITH CHECK OPTION`
Prevents DML operations (`INSERT`/`UPDATE`) through a view if the new or modified row does not satisfy the view's `WHERE` clause.
```sql
CREATE VIEW Suppliers_HighStatus AS
SELECT * FROM suppliers
WHERE status > 15
WITH CHECK OPTION;
```

---

## 5) Built-in SQL Functions

### A) Scalar Functions
Operate on an individual input value and return a single transformed value:
* **String**: `UPPER(name)`, `LOWER(name)`, `CONCAT(first_name, ' ', last_name)`, `SUBSTRING(title, 1, 5)`
* **Math**: `ROUND(AVG(salary), 2)`, `ABS(delta)`, `CEIL(val)`, `FLOOR(val)`
* **Date & Time**: `YEAR(hire_date)`, `MONTH(hire_date)`, `DATE_ADD(rescue_date, INTERVAL 3 DAY)`, `DATEDIFF(CURRENT_DATE, rescue_date)`

```sql
SELECT CONCAT(Fname, ' ', Lname) AS Full_Name, ROUND(salary, 2) AS Salary
FROM employee;
```

---

## 6) Stored Procedures

A **Stored Procedure** is a precompiled collection of SQL statements stored on the database server.

### Benefits
* **Network Efficiency**: Reduces traffic between application and DB server.
* **Security**: Grants execution rights to procedure without giving raw table access.
* **Maintainability**: Reusable central business logic.

```sql
DELIMITER $$

CREATE PROCEDURE Update_Employee_Salary(
    IN empNum VARCHAR(10),
    IN rating SMALLINT
)
BEGIN
    IF rating = 1 THEN
        UPDATE employees SET salary = salary * 1.10 WHERE emp_id = empNum;
    ELSE
        UPDATE employees SET salary = salary * 1.05 WHERE emp_id = empNum;
    END IF;
END $$

DELIMITER ;

-- Calling the procedure
CALL Update_Employee_Salary('E12345', 1);
```

---

## 7) Database Triggers

A **Trigger** automatically fires in response to specific database events (`INSERT`, `UPDATE`, `DELETE`) on a specified table.

```sql
-- Audit log trigger whenever an order is inserted
CREATE TRIGGER after_insert_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (order_id, action, inserted_at)
    VALUES (NEW.order_id, 'INSERTED', NOW());
END;
```

---

## 8) User-Defined Functions (UDFs)

Custom functions written to encapsulate reusable calculation logic. Unlike procedures, UDFs must return a value and can be called directly inside `SELECT` queries.

```sql
DELIMITER $$

CREATE FUNCTION Format_Full_Name(first_name VARCHAR(50), last_name VARCHAR(50))
RETURNS VARCHAR(105)
DETERMINISTIC
BEGIN
    RETURN CONCAT(UPPER(LEFT(first_name, 1)), LOWER(SUBSTRING(first_name, 2)), ' ', UPPER(last_name));
END $$

DELIMITER ;

-- Usage in query
SELECT Format_Full_Name(fname, lname) AS Formatted_Name FROM employee;
```

---

## 9) Window Functions

Window functions perform calculations across a set of table rows related to the current row without collapsing rows into a single summary output (unlike `GROUP BY`).

### Syntax Structure
```sql
SELECT column_name,
       window_function() OVER (
           PARTITION BY partition_column
           ORDER BY sort_column
       ) AS result_alias
FROM table_name;
```

### Key Window Functions
1. **Aggregate Window**: `AVG(salary) OVER (PARTITION BY department_id)`
2. **Value Window**: `LEAD(salary, 1) OVER (ORDER BY hire_date)`, `LAG(salary, 1) OVER (ORDER BY hire_date)`
3. **Ranking Window**:
   * `ROW_NUMBER()`: Sequential integer starting at 1.
   * `RANK()`: Rank with gaps for ties (1, 2, 2, 4).
   * `DENSE_RANK()`: Rank without gaps for ties (1, 2, 2, 3).

```sql
SELECT name, salary, department_id,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_salary_rank,
       LEAD(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS next_lower_salary
FROM employees;
```

---

## 10) Common Table Expressions (CTEs)

A CTE is a temporary named result set defined within a `WITH` clause that exists only during query execution.

```sql
WITH HighEarnerEmployees AS (
    SELECT emp_id, name, salary, dept_id
    FROM employees
    WHERE salary > 70000
),
DeptAggregates AS (
    SELECT dept_id, COUNT(*) AS high_earner_count
    FROM HighEarnerEmployees
    GROUP BY dept_id
)
SELECT d.name AS Department_Name, da.high_earner_count
FROM DeptAggregates da
JOIN departments d ON da.dept_id = d.id;
```

---

## 11) Database Indexes & Performance

An **Index** is a data structure (typically B-Tree) that speeds up data retrieval on columns frequently used in `WHERE`, `JOIN`, and `ORDER BY` clauses.

```sql
-- Create single-column index
CREATE INDEX idx_department ON employees (department_id);

-- Create composite index
CREATE INDEX idx_dept_salary ON employees (department_id, salary DESC);

-- Drop index
DROP INDEX idx_department ON employees;
```

> ⚠️ **Performance Trade-Off**: Indexes speed up `SELECT` queries but slow down `INSERT`, `UPDATE`, and `DELETE` statements because the index B-Tree must be updated on every write.

---

## 12) Cursors vs. Set-Based SQL

A **Cursor** is a database object used to iterate through query results line by line (procedural row-by-row processing).

### Explicit Cursor Cycle
1. `DECLARE cursor_name CURSOR FOR SELECT ...`
2. `OPEN cursor_name;`
3. `FETCH cursor_name INTO variables;`
4. `CLOSE cursor_name;`

### Comparison Table

| Feature | Set-Based SQL (`SELECT`/`UPDATE`) | Cursors (Row-by-Row) |
|---|---|---|
| **Speed** | 🚀 Extremely fast (vectorized engine) | 🐢 Slow (procedural overhead) |
| **Memory** | Optimized allocation | High memory consumption |
| **Code Length** | Concise & declarative | Verbose & complex |
| **Use Case** | 99% of data engineering tasks | Legacy migrations or row-level complex API triggers |

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
