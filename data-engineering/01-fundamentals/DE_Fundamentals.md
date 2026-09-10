# 🏗️ Data Engineering — Fundamentals

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Introduction to Data Engineering* course material (Rowad Misr Al-Raqmeya). This is Part 1 of the Data Engineering track — start here before Data Modeling & SQL.

---

## 📑 Table of Contents
1. [What is Data?](#1-what-is-data)
2. [Why Data is Important](#2-why-data-is-important)
3. [What is Data Engineering?](#3-what-is-data-engineering)
4. [What Does a Data Engineer Do?](#4-what-does-a-data-engineer-do)
5. [Data Engineering Lifecycle](#5-data-engineering-lifecycle)
6. [Different Roles & Titles](#6-different-roles--titles)
7. [ETL: Extract, Transform, Load](#7-etl-extract-transform-load)
8. [Types of Data](#8-types-of-data)
9. [Storage in Data Engineering](#9-storage-in-data-engineering)
10. [Uber Use Case](#10-uber-use-case)
11. [Tools & Technologies Used in This Course](#11-tools--technologies-used-in-this-course)

---

## 1) What is Data?

Data is a collection of facts, information, and statistics, and it can take many forms — numbers, text, sound, images, or any other format.

**What kind of data do real companies have?**

| Company | Types of Data Collected |
|---|---|
| Facebook (Meta) | User profiles, posts, likes, friends, ads, time spent |
| Netflix | Watch history, preferences, device used, search history, ratings |
| Spotify | Songs played, playlists, skips, search history, ads, subscriptions |
| Noon (E-commerce) | Browsing & purchase history, cart activity, payment, reviews |
| Banks | Transactions, loans, card usage, fraud detection, customer support |
| Seller Companies | Sales, customer details, payment trends, inventory |
| Vodafone & Telecom | Calls, SMS, internet usage, location, billing, customer support |

> 💬 **"Data is the new oil."** Just like oil needs refining before it's useful, raw data needs to be extracted, processed, and structured before it becomes valuable — which is exactly what data engineering does.

---

## 2) Why Data is Important

1. **Decision-making**
2. **Problem solving**
3. **Understanding**
4. **Improving processes**
5. **Understanding customers**

---

## 3) What is Data Engineering?

**Data engineering** is the practice of designing and building systems for the aggregation, storage, and analysis of data at scale. Data engineers empower organizations to get insights in real time from large datasets.

> Before AI and Data Science magic can happen, **you first need Data Engineering** — data scientists and ML models can't work with messy, scattered, or inaccessible data. Data engineering is the foundation everything else is built on.

---

## 4) What Does a Data Engineer Do?

- **Design & Build Data Pipelines** — collect, transform, and move data efficiently.
- **Develop & Manage Databases** — store structured & unstructured data for easy access.
- **Ensure Data Quality & Integrity** — validate data accuracy, consistency, and reliability.
- **Collaborate with Teams** — work with data scientists and analysts.
- **Optimize Data Workflows** — automate processes and improve efficiency.

---

## 5) Data Engineering Lifecycle

```
Generation → [ Ingestion → Transformation → Serving ]  →  Analytics
                        (Storage underlies all three)  →  Machine Learning
                                                        →  Reverse ETL

Undercurrents (run through every stage):
Security | Data Management | DataOps | Data Architecture | Orchestration | Software Engineering
```

- **Generation**: where the data is created (apps, sensors, transactions, user activity...)
- **Ingestion**: bringing generated data into the system
- **Transformation**: cleaning and reshaping the data into something usable
- **Serving**: making the processed data available for its final consumers (dashboards, ML models, reverse ETL back into business tools)
- **Storage**: not a single stage — it underlies ingestion, transformation, and serving simultaneously. Data gets stored *many* times as it moves through the lifecycle.
- **Undercurrents**: cross-cutting concerns that touch every stage rather than being a stage themselves.

---

## 6) Different Roles & Titles

**Data Engineer roles you'll see in job postings:**
- Pipeline Developer
- DataOps Engineer
- Data Quality Engineer
- Database Architect
- Data Integration Specialist
- Big Data Engineer

**How Data Engineer, Data Scientist, and Data Analyst differ:**

| Title | Focus |
|---|---|
| **Data Scientist** | Uses statistics and machine learning to make predictions and answer key business questions |
| **Data Engineer** | Builds and optimizes the systems that allow data scientists and analysts to perform their work |
| **Data Analyst** | Delivers value by taking data, communicating the results to help make business decisions |

A more detailed way to see the overlap:

| | Data Engineer | *(shared)* | Data Scientist | *(shared)* | Data Analyst |
|---|---|---|---|---|---|
| **Focus area** | Infrastructure | Integration | Modeling | Insights | Reporting |
| **Includes** | Data architecture, infrastructure setup, database management, scalability solutions | Pipeline optimization, data cleaning automation, real-time data processing | Machine learning, predictive modeling, statistical analysis, algorithm optimization | Data querying, data analysis, insight generation | KPI tracking & benchmarking, reporting automation & dashboards, business/market/industry analysis |

*(Adaptation of the data science Venn diagram originally by Kevin Schmidt, Towards Data Science, 2015.)*

---

## 7) ETL: Extract, Transform, Load

**ETL** stands for Extract, Transform, and Load — a traditionally accepted way for organizations to combine data from multiple systems into a single database, data store, data warehouse, or data lake.

### Extract
Retrieving data from one or more sources — online, on-premises, legacy systems, SaaS platforms, or others. After extraction, the data is loaded into a staging area.

### Transform
Taking the extracted data, cleaning it, and putting it into a common format so it can be stored in the target system. Cleaning typically involves removing duplicate, incomplete, or obviously erroneous records.

**Example — raw data before transformation:**

| Order ID | Customer Name | Date | Amount | Country |
|---|---|---|---|---|
| 101 | John Doe | 01/15/2024 | $50.00 | USA |
| 102 | Jane Smith | 15-01-2024 | $75.50 | UK |
| 103 | NULL | 2024-01-16 | $40.00 | USA |
| 104 | Mark Lee | 16-Jan-24 | -$20.00 | CAN |

**After transformation:**

| Order ID | Customer Name | Date | Amount | Country |
|---|---|---|---|---|
| 101 | John Doe | 2024-01-15 | 50.00 | USA |
| 102 | Jane Smith | 2024-01-15 | 75.50 | UK |
| 104 | Mark Lee | 2024-01-16 | 20.00 | Canada |

**Transformation steps applied:**
- Convert date formats to a standard format (`YYYY-MM-DD`)
- Remove duplicates and NULL values (row 103 was dropped — missing customer name)
- Convert negative amounts to absolute values
- Standardize country names (`CAN` → `Canada`)

### Load
Inserting the formatted data into the target database, data store, data warehouse, or data lake.

**Scenario:** A company collects daily sales data from multiple branches. After extracting the data and transforming it (cleaning, formatting), it needs to be **loaded** into a centralized database for reporting.

---

## 8) Types of Data

Data sources come in three main forms:

### Structured Data
Organized in a clear, predefined format (rows and columns). Its standardized nature makes it easily readable by data analytics tools, ML algorithms, and humans alike. Can include quantitative data (prices, revenue) and qualitative data (dates, names, addresses).

**Example:**

| index | last_name | first_name | office | address | number | city | zipcode |
|---|---|---|---|---|---|---|---|
| 0 | Thien | Vivian | Belgium | Martelarenlaan | 38 | Leuven | 3010 |
| 1 | Huong | Julian | Belgium | Martelarenlaan | 38 | Leuven | 3010 |
| 2 | Duplantier | Norbert | UK | Old Street | 207 | London | EC1V 9NR |

### Unstructured Data
Has no predefined format. Can be textual or non-textual, qualitative or quantitative.
- **Textual examples:** emails, text documents, social media posts, call transcripts, Slack/Teams messages
- **Non-textual examples:** images (JPEG, GIF, PNG), audio, video, mobile activity logs, IoT sensor data

### Semi-Structured Data
Has a loose structure — not a rigid schema like structured data, but not free-form either. Contains tags or markers to separate elements without conforming to a strict table format.
- **Textual examples:** JSON, XML, YAML files, NoSQL databases (MongoDB, Couchbase), email metadata
- **Non-textual examples:** server/application log files, labeled sensor logs, configuration files, streaming telemetry data, tagged image/video metadata (EXIF)

**Example (JSON, semi-structured):**
```json
{
  "user_1645156": {
    "last_name": "Lacroix",
    "first_name": "Hadrien",
    "favorite_artists": ["Fools in Deed", "Gojira", "Pain", "Nanowar of Steel"]
  },
  "user_5913764": {
    "last_name": "Billen",
    "first_name": "Sara",
    "favorite_artists": ["Tamino", "Taylor Swift"]
  }
}
```

---

## 9) Storage in Data Engineering

Storage is the cornerstone of the data engineering lifecycle and underlies its major stages — ingestion, transformation, and serving. Data gets stored many times as it moves through the lifecycle: "it's storage all the way down."

### Storage Components (from raw hardware up to abstractions)
- **Raw ingredients**: HDD, SSD, RAM, Networking, Serialization, Compression, CPU
- **Storage systems**: HDFS, RDBMS, Object storage, Cache/memory-based storage, Streaming storage
- **Storage abstractions**: Data lake, Data lakehouse, Data platform, Cloud data warehouse

### Storage Types — Latency, Bandwidth, and Price

| Storage Type | Data Fetch Latency | Bandwidth | Price |
|---|---|---|---|
| CPU cache | 1 nanosecond | 1 TB/s | N/A |
| RAM | 0.1 microseconds | 100 GB/s | $10/GB |
| SSD | 0.1 milliseconds | 4 GB/s | $0.20/GB |
| HDD | 4 milliseconds | 300 MB/s | $0.03/GB |
| Object storage | 100 milliseconds | 10 GB/s | $0.02/GB per month |
| Archival storage | 12 hours | Same as object storage once available | $0.004/GB per month |

*(A microsecond is 1,000 nanoseconds; a millisecond is 1,000 microseconds. The general pattern: the faster the storage, the higher the price per GB.)*

### Data Warehouse vs Data Lake vs Data Lakehouse

| Feature | Data Warehouse | Data Lake | Data Lakehouse |
|---|---|---|---|
| **Data Types** | Structured data only | Structured, semi-structured, unstructured | Structured, semi-structured, unstructured |
| **Storage Cost** | High (optimized for structured data) | Low (scalable for large volumes) | Moderate (balances cost & performance) |
| **Performance** | Fast for structured queries | Slower without optimization | Optimized for both structured & unstructured data |

---

## 10) Uber Use Case

Uber's abstracted data pipeline flow, end to end:

```
Data Collection & Ingestion
  → Sources: Uber App, Driver App, GPS, user interactions
  → Volume: ~75 GB/sec, handling petabytes of data
        ↓
Real-Time Data Processing
  → Streaming analytics; supports dynamic pricing, rider-driver matching
        ↓
Data Storage Solutions
  → Lakehouse architecture; supports structured & unstructured data
        ↓
Data Access & Querying
  → Presto & Apache Spark; ~500K queries, ~400K Spark jobs daily
        ↓
Machine Learning & Predictive Analytics
  → Demand forecasting; optimizes driver allocation, reduces wait time
        ↓
Infrastructure Management
  → Docstore (distributed DB); stores petabytes, serves millions of requests/sec
        ↓
Workflow Orchestration
  → Manages complex data workflows; enables UberPOOL, Uber Eats routing
```

This is a concrete, real-world illustration of the lifecycle from section 5 — generation (GPS/app events) → ingestion/transformation (streaming, Spark) → storage (lakehouse, Docstore) → serving (analytics, ML, orchestration).

---

## 11) Tools & Technologies Used in This Course

- **Programming:** Python
- **Cloud:** Microsoft Azure
- **Storage Tools:** MySQL / PostgreSQL
- **Querying:** SQL
- **Processing:** Apache Spark, Hadoop
- **Orchestration:** Apache Airflow

These map directly onto the lifecycle stages from section 5 — SQL/MySQL for storage & querying, Spark/Hadoop for transformation/processing, and Airflow for orchestrating it all together. Later parts of this course (and this repo) go deeper into each one.

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
