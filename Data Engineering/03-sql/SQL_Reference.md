# 🗃️ SQL & RDBMS — A Complete Reference

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: Data Engineering course material, Part 3. Builds directly on [`../02-data-modeling-and-databases/Data_Modeling_Databases.md`](../02-data-modeling-and-databases/Data_Modeling_Databases.md).
>
> ⚠️ **Note:** the source slides listed every topic below in their agenda, but the worked query examples for "Aggregate Functions" through "MySQL Workbench" were shown as screenshots that couldn't be extracted as text. Those sections here are filled in with standard, correct MySQL syntax for the exact topics named in the agenda — genuinely new content added to complete the reference, not verbatim from the original slides.

---

## 📑 Table of Contents
1. [What is RDBMS?](#1-what-is-rdbms)
2. [Tables, Columns, and Data Types](#2-tables-columns-and-data-types)
3. [How to Design a Database](#3-how-to-design-a-database)
4. [One-to-Many & Many-to-Many Relationships](#4-one-to-many--many-to-many-relationships)
5. [What is SQL?](#5-what-is-sql)
6. [SQL Engines](#6-sql-engines)
7. [MySQL Data Types](#7-mysql-data-types)
8. [CRUD](#8-crud)
9. [Selecting Data](#9-selecting-data)
10. [Filtering Data](#10-filtering-data)
11. [Ordering Data](#11-ordering-data)
12. [Limiting Data](#12-limiting-data)
13. [Aggregate Functions](#13-aggregate-functions)
14. [Grouping Data](#14-grouping-data)
15. [Datetime Operations](#15-datetime-operations)
16. [Joining Tables](#16-joining-tables)
17. [Subqueries](#17-subqueries)
18. [Window Functions](#18-window-functions)
19. [Inserting, Updating, Deleting Data](#19-inserting-updating-deleting-data)
20. [Python & MySQL](#20-python--mysql)
21. [MySQL Workbench](#21-mysql-workbench)

Running example used throughout: an e-commerce database with `Customers`, `Products`, `Categories`, `Orders`, and `Order_Details` tables.

---

## 1) What is RDBMS?

**RDBMS** = Relational Database Management System. It's a file system made for storing and manipulating *relational* data:

- Data is organized in **tabular form** — each table represents an entity, like `Users`, `Products`, or `Categories`.
- Each table consists of **columns** that represent the entity's properties. Each column has a data type (numbers, text, etc.).
- **SQL** is the language used to connect to and query the data from an RDBMS easily.

---

## 2) Tables, Columns, and Data Types

- **Tables** — `Users`, `Posts`, `Comments`, `Products`, ...
- **Columns** — a `Users` table might have columns like `age`, `gender`, `username`, `email`, `is_online`, ...
- **Data Types** — `age` is Numeric, `username` is TEXT, `gender` is CHAR, `is_online` is BOOL.

---

## 3) How to Design a Database

1. **Analyze the system and divide it into its main entities (tables).**
   Example: for an e-commerce system, the main entities are `Categories`, `Products`, `Orders`, `Customers`, etc.
2. **For each table, define its properties (columns) and their data types.**
   Example: `Customers` has `name`, `city`, `phone`; `Products` has `price`, `name`, etc. Most importantly — every table needs a unique, auto-incrementing `id` column (the **Primary Key**), since it's the row's identifier.
3. **Define direct relationships between tables, and add foreign keys accordingly.**
   Example: there's a one-to-many relationship between `Products` and `Categories`, so a `CategoryID` column (foreign key) is added to `Products`. There's also a many-to-many relationship between `Orders` and `Products`, so an `Order_Details` table is created to hold both foreign keys.

---

## 4) One-to-Many & Many-to-Many Relationships

**One-to-Many:** `Products` → `Categories`. `CategoryID` in `Products` is a foreign key pointing to the `CategoryID` primary key in `Categories`.

```sql
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Price DECIMAL(10, 2),
    CategoryID INT,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
```

**Many-to-Many:** `Orders` and `Products` — an order can contain many products, and a product can appear in many orders. This can't be represented with a single foreign key on either side, so a **junction table** (`Order_Details`) is created holding both foreign keys:

```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE
);

CREATE TABLE Order_Details (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),   -- composite primary key
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
```

> 💡 **Design activity idea (from the course):** try modeling Facebook, YouTube, or Talabat this way yourself — identify the entities, then the relationships, then decide which need a junction table.

---

## 5) What is SQL?

**SQL** (Structured Query Language) is used to communicate with a database by executing commands to create tables and columns, and to read, filter, order, insert, update, and delete data.

Practice resources: [w3schools SQL tutorial](https://www.w3schools.com/sql/default.asp), [SQLite Tutorial](https://www.sqlitetutorial.net)

---

## 6) SQL Engines

SQL engines/servers are programs that host an RDBMS system, where you store databases and perform read/write operations. The most common ones:

- **MySQL** — very flexible, widely used, lots of tooling. (Installer: [dev.mysql.com/downloads/installer](https://dev.mysql.com/downloads/installer/))
- **Microsoft SQL Server**
- **PostgreSQL**
- **SQLite** — runs offline, file-based, no server needed

---

## 7) MySQL Data Types

Each column in SQL has exactly **one** data type. MySQL's data types fall into three categories:

- **Numeric** — `INT`, `FLOAT`, `DOUBLE`, `DECIMAL`
- **String (Text)** — `CHAR`, `VARCHAR`, `TEXT`
- **Datetime** — `DATE`, `DATETIME`, `TIMESTAMP`, `TIME`, `YEAR`

Full reference: [w3schools SQL data types](https://www.w3schools.com/sql/sql_datatypes.asp), [MySQL docs](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

---

## 8) CRUD

SQL supports four core operations, together known as CRUD:

| Letter | Operation | SQL Statement |
|---|---|---|
| **C** | Create | `INSERT INTO` |
| **R** | Read | `SELECT` |
| **U** | Update | `UPDATE` |
| **D** | Delete | `DELETE` |

---

## 9) Selecting Data

```sql
-- Select all columns from a table
SELECT * FROM Customers;

-- Select specific columns from a table
SELECT Name, City FROM Customers;
```

---

## 10) Filtering Data

```sql
-- WHERE clause: filter with text vs numeric fields
SELECT * FROM Customers WHERE City = 'Cairo';       -- text: quoted
SELECT * FROM Products  WHERE Price > 500;            -- numeric: unquoted

-- Comparison operators: =, !=, >, <, >=, <=
SELECT * FROM Products WHERE Price >= 100;

-- BETWEEN
SELECT * FROM Products WHERE Price BETWEEN 100 AND 500;

-- IN
SELECT * FROM Customers WHERE City IN ('Cairo', 'Giza', 'Alexandria');

-- LIKE (pattern matching: % = any sequence, _ = single character)
SELECT * FROM Customers WHERE Name LIKE 'A%';        -- starts with A
SELECT * FROM Customers WHERE Email LIKE '%@gmail.com';  -- ends with

-- Logic operators: AND, OR, NOT
SELECT * FROM Products WHERE Price > 100 AND CategoryID = 2;
SELECT * FROM Products WHERE CategoryID = 2 OR CategoryID = 3;
SELECT * FROM Products WHERE NOT CategoryID = 2;

-- IS NULL / IS NOT NULL
SELECT * FROM Customers WHERE Phone IS NULL;
SELECT * FROM Customers WHERE Phone IS NOT NULL;
```

---

## 11) Ordering Data

```sql
-- Order by a single column, ascending (default)
SELECT * FROM Products ORDER BY Price ASC;

-- Order by a single column, descending
SELECT * FROM Products ORDER BY Price DESC;

-- Filter then order
SELECT * FROM Products WHERE CategoryID = 2 ORDER BY Price DESC;

-- Order by several columns (ties in the first column break by the second)
SELECT * FROM Products ORDER BY CategoryID ASC, Price DESC;
```

---

## 12) Limiting Data

```sql
-- Limit results to a specific number, from the first row
SELECT * FROM Products LIMIT 10;

-- Limit results to a specific number, starting from a specific offset
-- (skip the first 10 rows, then return the next 10 — classic pagination)
SELECT * FROM Products LIMIT 10 OFFSET 10;
```

---

## 13) Aggregate Functions

Aggregate functions collapse many rows into a single summary value.

```sql
SELECT COUNT(*) FROM Orders;                    -- how many orders exist
SELECT SUM(Price) FROM Products;                  -- total value of all products
SELECT AVG(Price) FROM Products;                   -- average product price
SELECT MIN(Price), MAX(Price) FROM Products;        -- cheapest and most expensive product
```

---

## 14) Grouping Data

`GROUP BY` splits rows into buckets by a column's value, then an aggregate function summarizes each bucket. `HAVING` filters *after* grouping (unlike `WHERE`, which filters *before* grouping).

```sql
-- Number of products per category
SELECT CategoryID, COUNT(*) AS product_count
FROM Products
GROUP BY CategoryID;

-- Average price per category, but only categories averaging above 200
SELECT CategoryID, AVG(Price) AS avg_price
FROM Products
GROUP BY CategoryID
HAVING AVG(Price) > 200;
```

---

## 15) Datetime Operations

```sql
SELECT NOW();                                  -- current date and time
SELECT CURDATE();                                -- current date only

SELECT * FROM Orders WHERE YEAR(OrderDate) = 2024;
SELECT * FROM Orders WHERE MONTH(OrderDate) = 1;

-- Difference between two dates, in days
SELECT DATEDIFF(NOW(), OrderDate) AS days_since_order FROM Orders;

-- Reformat a date for display
SELECT DATE_FORMAT(OrderDate, '%Y-%m-%d') FROM Orders;

-- Orders placed in the last 30 days
SELECT * FROM Orders WHERE OrderDate >= NOW() - INTERVAL 30 DAY;
```

---

## 16) Joining Tables

Joins combine rows from two or more tables based on a related column (usually a foreign key ↔ primary key pair).

```sql
-- INNER JOIN: only rows that match in both tables
SELECT Orders.OrderID, Customers.Name
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- LEFT JOIN: all rows from the left table, matched data from the right if it exists
SELECT Customers.Name, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

-- RIGHT JOIN: all rows from the right table, matched data from the left if it exists
SELECT Orders.OrderID, Customers.Name
FROM Orders
RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- Joining 3 tables to build a full order summary (many-to-many via Order_Details)
SELECT Orders.OrderID, Products.Name, Order_Details.Quantity
FROM Orders
JOIN Order_Details ON Orders.OrderID = Order_Details.OrderID
JOIN Products ON Order_Details.ProductID = Products.ProductID;
```

---

## 17) Subqueries

A subquery is a query nested inside another query — used when you need the result of one query to filter or compute another.

```sql
-- Scalar subquery: products priced above the overall average
SELECT * FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);

-- IN subquery: customers who have placed at least one order
SELECT * FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);

-- Correlated subquery: products priced above the average of their OWN category
SELECT * FROM Products p1
WHERE Price > (
    SELECT AVG(Price) FROM Products p2 WHERE p2.CategoryID = p1.CategoryID
);
```

---

## 18) Window Functions

Unlike `GROUP BY` (which collapses rows), window functions calculate a value *across* a set of related rows while still returning every individual row.

```sql
-- Rank products by price within each category, without collapsing rows
SELECT
    Name,
    CategoryID,
    Price,
    RANK() OVER (PARTITION BY CategoryID ORDER BY Price DESC) AS price_rank
FROM Products;

-- Row number per customer's orders, oldest first
SELECT
    OrderID,
    CustomerID,
    OrderDate,
    ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS order_sequence
FROM Orders;

-- Running total of order amounts over time
SELECT
    OrderID,
    OrderDate,
    Amount,
    SUM(Amount) OVER (ORDER BY OrderDate) AS running_total
FROM Orders;
```

---

## 19) Inserting, Updating, Deleting Data

```sql
-- INSERT: add a new row
INSERT INTO Customers (Name, City, Phone)
VALUES ('Youssef Ibrahim', 'Cairo', '01119834356');

-- UPDATE: modify existing rows — ALWAYS use WHERE, or every row gets updated
UPDATE Products
SET Price = 450
WHERE ProductID = 12;

-- DELETE: remove rows — ALWAYS use WHERE, or the whole table gets emptied
DELETE FROM Orders
WHERE OrderID = 305;
```

---

## 20) Python & MySQL

Python connects to MySQL through a connector library (`mysql-connector-python`):

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="ecommerce"
)

cursor = conn.cursor()
cursor.execute("SELECT Name, Price FROM Products WHERE Price > 100")

for name, price in cursor.fetchall():
    print(name, price)

cursor.close()
conn.close()
```

This is the typical bridge between a data engineering pipeline (Python scripts, scheduled by something like Airflow) and the underlying relational database.

---

## 21) MySQL Workbench

**MySQL Workbench** is the official free GUI tool for working with MySQL — used to visually design database schemas (ER diagrams), run and test SQL queries, manage users/permissions, and inspect table structures without writing raw `CREATE TABLE` statements by hand. It's typically where step 3 ("How to Design a Database") gets drawn out visually before being turned into actual SQL.

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
