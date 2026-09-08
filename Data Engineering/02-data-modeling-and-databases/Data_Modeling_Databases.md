# 🗄️ Data Modeling & Databases

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: Data Engineering course material, Part 2. This builds on [`../01-fundamentals/DE_Fundamentals.md`](../01-fundamentals/DE_Fundamentals.md) and leads directly into [`../03-sql/SQL_Reference.md`](../03-sql/SQL_Reference.md) — the concepts here (entities, keys, relationships) are exactly what SQL tables are built from.

---

## 📑 Table of Contents
1. [What is a Data Model?](#1-what-is-a-data-model)
2. [What is a Database?](#2-what-is-a-database)
3. [Why is a Database Important?](#3-why-is-a-database-important)
4. [Types of Relationships](#4-types-of-relationships)
5. [What is a Primary Key?](#5-what-is-a-primary-key)
6. [What is a Foreign Key?](#6-what-is-a-foreign-key)
7. [Fact Tables & Dimension Tables](#7-fact-tables--dimension-tables)

---

## 1) What is a Data Model?

Data models are made up of **entities** — the objects or concepts we want to track data about. Entities become the **tables** in a database. For example, in an e-commerce system, entities might be `Customers`, `Products`, and `Orders` — each becomes its own table.

---

## 2) What is a Database?

A **database** is an organized collection of structured information, or data, typically stored electronically in a computer system.

Together, the data and the **DBMS** (Database Management System — the software that manages the database) — along with the applications associated with them — are referred to as a **database system**, often shortened to just "database."

---

## 3) Why is a Database Important?

- **To manage large chunks of data**
- **Accuracy**
- **Security of data**
- **Data Integrity**
- **Organize data**

---

## 4) Types of Relationships

There are three fundamental ways entities can relate to each other:

- **One to One (1:1)** — one row in Table A relates to exactly one row in Table B (e.g., one `User` has exactly one `UserProfile`).
- **One to Many (1:M)** — one row in Table A relates to many rows in Table B (e.g., one `Category` has many `Products`).
- **Many to Many (M:M)** — many rows in Table A relate to many rows in Table B (e.g., many `Orders` can each contain many `Products`, and each `Product` can appear in many `Orders`).

> A many-to-many relationship can't be represented directly with a simple foreign key — it needs a **junction/bridge table** in between (see the SQL reference for the worked example: `Order_Details`).

---

## 5) What is a Primary Key?

A **primary key** is a column — or a group of columns — in a table that **uniquely identifies** each row in that table. For example, in a `Customers` table, `CustomerNo` (the ID assigned to each customer) is the primary key.

**Properties of a primary key:**
- Enforces uniqueness — it does not accept any duplicate values.
- Uniquely identifies each row.
- A table can only have **one** primary key.
- Primary key columns have a maximum length of 900 bytes.
- A primary key column **cannot** accept `NULL` values.

---

## 6) What is a Foreign Key?

A **foreign key** is a column or group of columns in a relational database table that provides a **link between data in two tables**. It's how a "many" side of a relationship points back to the "one" side — e.g., a `CategoryID` column in a `Products` table that points to the `CategoryID` primary key in the `Categories` table.

---

## 7) Fact Tables & Dimension Tables

These two concepts come from data warehouse design (the **star schema** / **snowflake schema** patterns):

- **Fact table**: a table that stores **measures** — the numbers that measure the business, such as sales, cost of goods, or profit. Fact tables typically use **composite keys** (primary keys made up of a subset of other keys, usually foreign keys pointing to the surrounding dimension tables).
- **Dimension table**: a table that stores **attributes**, or dimensions, that describe the objects referenced in a fact table — e.g., a `Date` dimension (day, month, quarter, year), a `Product` dimension (name, category, brand), or a `Customer` dimension (name, region, segment).

**The typical pattern:** one central fact table (e.g., `Sales_Fact`, holding the transaction amounts) surrounded by several dimension tables (`Date_Dim`, `Product_Dim`, `Customer_Dim`) that each fact row links to via foreign keys — this is the "star" shape the star schema is named after.

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
