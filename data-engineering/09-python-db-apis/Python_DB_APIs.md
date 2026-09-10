# 🔌 Python for Databases & REST APIs — Pipeline Connectivity Reference

**Author:** Youssef Ibrahim Mohamed Soliman
**GitHub:** https://github.com/Yosef-Ibrahim
**Email:** youssefibrahimelisely@gmail.com
**Phone:** 01119834356

> Have an idea, correction, or new example to contribute (ML / Data Science / Data Analysis / Data Engineering topics only)? Reach out using the contact info above.
>
> 📖 Source: *Python for Databases & APIs* course material (Rowad Misr Al-Raqmeya).

---

## 📑 Table of Contents
1. [SQL Database Connections (SQLite & SQLAlchemy)](#1-sql-database-connections)
2. [NoSQL Database Connections (MongoDB & PyMongo)](#2-nosql-database-connections)
3. [REST API Architectural Principles](#3-rest-api-architectural-principles)
4. [HTTP Verbs & Status Codes (GET, POST, PUT, PATCH, DELETE)](#4-http-verbs--status-codes)
5. [Building Ingestion APIs with Flask](#5-building-ingestion-apis-with-flask)
6. [Consuming External REST APIs (Requests Library)](#6-consuming-external-rest-apis)
7. [REST vs. GraphQL in Data Pipelines](#7-rest-vs-graphql-in-data-pipelines)

---

## 1) SQL Database Connections

Data engineers rely on database drivers (`sqlite3`, `psycopg2`, `pymysql`, `SQLAlchemy`) to ingest and extract data.

```python
import sqlite3

# 1. Connect & Create Cursor
conn = sqlite3.connect('pipeline_database.db')
cursor = conn.cursor()

# 2. Execute DDL
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# 3. Parameterized DML (Prevents SQL Injection)
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

# 4. Commit Changes & Query
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

# 5. Resource Cleanup
conn.close()
```

> ⚠️ **Critical Rule**: Always call `conn.commit()` after mutating statements (`INSERT`, `UPDATE`, `DELETE`), otherwise changes will not persist. Always close cursors and connections in production.

---

## 2) NoSQL Database Connections (MongoDB)

In NoSQL document stores (like MongoDB), data is stored as BSON/JSON documents inside **collections**.

```python
from pymongo import MongoClient

# Connect to local MongoDB instance
client = MongoClient("mongodb://localhost:27017/")
db = client["analytics_db"]
collection = db["raw_events"]

# 1. Insert Document
collection.insert_one({"user_id": 101, "event": "click", "timestamp": "2026-09-10T00:00:00Z"})

# 2. Read Documents
events = list(collection.find({"user_id": 101}))

# 3. Update Document
collection.update_one({"user_id": 101}, {"$set": {"status": "processed"}})

# 4. Delete Document
collection.delete_one({"user_id": 101})
```

---

## 3) REST API Architectural Principles

**REST** (Representational State Transfer) is a stateless client-server architecture.

### 5 Core REST Principles
1. **Stateless**: Every HTTP request contains all authentication and context required. No session state lives on the server.
2. **Client-Server Separation**: UI/Client and Data Storage/Server scale independently.
3. **Cacheable**: Server responses indicate if data can be cached by clients/gateways.
4. **Uniform Interface**: Resource identifiers (URIs) and standard HTTP methods.
5. **Layered System**: Intermediate proxies, load balancers, and gateways are transparent to the client.

---

## 4) HTTP Verbs & Status Codes

| Method | Purpose | Idempotent? | Safe? | Typical Status Codes |
|---|---|---|---|---|
| **`GET`** | Retrieve resource | ✅ Yes | ✅ Yes | `200 OK`, `404 Not Found` |
| **`POST`** | Create new resource | ❌ No | ❌ No | `201 Created`, `400 Bad Request` |
| **`PUT`** | Replace entire resource | ✅ Yes | ❌ No | `200 OK`, `204 No Content` |
| **`PATCH`** | Partial resource update | ⚠️ Usually | ❌ No | `200 OK`, `400 Bad Request` |
| **`DELETE`** | Remove resource | ✅ Yes | ❌ No | `200 OK`, `204 No Content` |

---

## 5) Building Ingestion APIs with Flask

**Flask** is a lightweight Python microframework ideal for exposing lightweight data endpoints.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database table
users_db = [{"id": 1, "name": "Alice", "age": 25}]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users_db), 200

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_user = {
        "id": len(users_db) + 1,
        "name": data.get("name"),
        "age": data.get("age")
    }
    users_db.append(new_user)
    return jsonify({"message": "User created successfully!", "user": new_user}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

---

## 6) Consuming External REST APIs

Data pipelines extract data from external third-party web services using the `requests` library.

```python
import requests

# 1. GET Request
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    posts = response.json()
    print(f"Retrieved {len(posts)} posts.")

# 2. POST Request with Payload
payload = {"title": "ETL Ingestion Log", "body": "Batch completed successfully.", "userId": 1}
post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
print("Response Code:", post_response.status_code)
```

---

## 7) REST vs. GraphQL in Data Pipelines

```
REST API Architecture:
[Client] ---> GET /users/1 -----------> [Server]
[Client] ---> GET /users/1/orders ---> [Server]  (Over-fetching / Multiple roundtrips)

GraphQL Architecture:
[Client] ---> POST /graphql ------------> [GraphQL Engine] ---> [DB / Microservices]
               query { user(id: 1) { name, orders { id, total } } }
```

### Advantages of GraphQL for Data Aggregation
* **Single Endpoint**: Eliminates multiple HTTP roundtrips.
* **No Over-Fetching**: Clients specify exact fields required in payload.
* **Strong Schema Typing**: Self-documenting graph schemas.

---

## 📬 Contributing

Have an addition, correction, or idea for this reference (ML / Data Science / Data Analysis / Data Engineering topics only)? Get in touch:

- **Youssef Ibrahim Mohamed Soliman**
- 📱 01119834356
- 📧 youssefibrahimelisely@gmail.com
- 💻 https://github.com/Yosef-Ibrahim
