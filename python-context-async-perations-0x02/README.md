# Advanced Python: Generators, Decorators, Context Managers, and Asynchronous Programming

## Project Overview
This project is part of the ProDev program and focuses on advanced Python programming concepts, specifically:
- Context managers
- Asynchronous programming with `asyncio`
- Handling database connections efficiently

The tasks involve creating reusable and efficient Python scripts to manage database operations and asynchronous tasks. Each script is designed to demonstrate real-world applications of these concepts.

---

## Repository Structure
The project files are organized as follows:

```
alx-backend-python/
├── python-context-async-perations-0x02/
│   ├── 0-databaseconnection.py
│   ├── 1-execute.py
│   ├── 3-concurrent.py
│   ├── README.md
```

---

## Tasks

### Task 0: Custom Class-Based Context Manager for Database Connection
- **Objective**: Create a class-based context manager to manage opening and closing database connections automatically.
- **Implementation**:
  - Define a `DatabaseConnection` class.
  - Implement `__enter__` and `__exit__` methods.
  - Use the context manager to run a query (`SELECT * FROM users`) and print the results.
- **File**: `0-databaseconnection.py`

#### Usage Example:
```python
with DatabaseConnection() as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
```

---

### Task 1: Reusable Query Context Manager
- **Objective**: Create a reusable context manager for executing queries dynamically.
- **Implementation**:
  - Define an `ExecuteQuery` class.
  - Implement `__enter__` and `__exit__` methods to manage the connection and cursor lifecycle.
  - Accept a query and parameters as inputs and return the query results.
- **File**: `1-execute.py`

#### Usage Example:
```python
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as results:
    for row in results:
        print(row)
```

---

### Task 2: Concurrent Asynchronous Database Queries
- **Objective**: Perform multiple database queries concurrently using `asyncio.gather`.
- **Implementation**:
  - Use the `aiosqlite` library for asynchronous database operations.
  - Create `async_fetch_users()` to fetch all users.
  - Create `async_fetch_older_users()` to fetch users older than 40.
  - Use `asyncio.gather()` to run the queries concurrently.
  - Execute the main function using `asyncio.run()`.
- **File**: `3-concurrent.py`

#### Usage Example:
```python
import asyncio
from 3-concurrent import fetch_concurrently

asyncio.run(fetch_concurrently())
```

---

## Tools and Libraries
- **Python 3.8+**: The primary programming language for the project.
- **SQLite**: Database system used for queries.
- **aiosqlite**: Library for asynchronous SQLite operations.
- **asyncio**: Python’s standard library for asynchronous programming.

---

## Instructions to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/mosekyle/alx-backend-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-backend-python/python-context-async-perations-0x02
   ```
3. Run the scripts:
   - For Task 0:
     ```bash
     python3 0-databaseconnection.py
     ```
   - For Task 1:
     ```bash
     python3 1-execute.py
     ```
   - For Task 2:
     ```bash
     python3 3-concurrent.py
     ```

---

## Learning Outcomes
- Understand and implement context managers to manage resources efficiently.
- Perform asynchronous database operations using `asyncio` and `aiosqlite`.
- Manage concurrent tasks with `asyncio.gather`.
- Write reusable and maintainable Python scripts.

---


