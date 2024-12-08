# Python Decorators for Database Operations

This project demonstrates the use of Python decorators to enhance database operations in Python applications. The primary focus is on automating common tasks like logging SQL queries, managing database connections, handling transactions, retrying failed database operations, and caching query results. These decorators are designed to make your database interactions more efficient, maintainable, and resilient.

## Table of Contents

- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Task Breakdown](#task-breakdown)
  - [Task 0: Logging Database Queries](#task-0-logging-database-queries)
  - [Task 1: Handle Database Connections with a Decorator](#task-1-handle-database-connections-with-a-decorator)
  - [Task 2: Transaction Management Decorator](#task-2-transaction-management-decorator)
  - [Task 3: Retry Database Queries](#task-3-retry-database-queries)
  - [Task 4: Cache Database Queries](#task-4-cache-database-queries)
- [GitHub Repository](#github-repository)
- [License](#license)

## Project Overview

This project focuses on mastering Python decorators to automate common database management tasks. By completing the tasks, learners will create custom decorators to:

- Log SQL queries
- Handle database connections
- Manage transactions
- Retry failed queries
- Cache query results

These decorators can be applied to optimize database interactions, improve performance, and increase code reusability.

## Learning Objectives

By completing this project, developers will:

- Gain an in-depth understanding of Python decorators.
- Automate repetitive tasks in database operations.
- Ensure database integrity with transaction management.
- Enhance performance using caching mechanisms.
- Build resilience into database operations through retry mechanisms.

## Requirements

- Python 3.8 or higher
- SQLite3 database setup (with a `users` table for testing)
- Working knowledge of Python decorators and database operations
- Familiarity with Git and GitHub

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/python-decorators-0x01.git
   cd python-decorators-0x01
   ```

2. **Install dependencies (if any)**:
   ```bash
   pip install -r requirements.txt
   ```

   If no `requirements.txt` file is available, ensure that the necessary dependencies (e.g., `sqlite3`) are installed by using:
   ```bash
   pip install sqlite3
   ```

3. **Ensure you have SQLite3 installed**:
   - SQLite comes pre-installed with Python, but ensure it's available for database operations.

4. **Run the script**:
   Each task script is self-contained. You can run individual scripts to test the decorators.

## Task Breakdown

### Task 0: Logging Database Queries

**Objective**: Create a decorator that logs all SQL queries executed by any function.

**Key Points**:
- Logs the SQL query before executing it.
- Enhances observability of database operations.

```python
def log_queries(func):
    def wrapper(*args, **kwargs):
        query = args[0]
        print(f"Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper
```

### Task 1: Handle Database Connections with a Decorator

**Objective**: Create a decorator that automatically handles opening and closing database connections.

**Key Points**:
- Opens a connection before the function runs and closes it afterward.
- Reduces boilerplate code for connection management.

```python
def with_db_connection(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper
```

### Task 2: Transaction Management Decorator

**Objective**: Create a decorator that manages database transactions by automatically committing or rolling back changes.

**Key Points**:
- Wraps functions in a transaction block.
- Commits the transaction if no error occurs; rolls back if an error happens.

```python
def transactional(func):
OA    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception:
            conn.rollback()
            raise
    return wrapper
```

### Task 3: Retry Database Queries

**Objective**: Create a decorator that retries database operations if they fail due to transient errors.

**Key Points**:
- Retries a failed operation up to a specified number of retries.
- Introduces a delay between retries.

```python
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < retries - 1:
                        time.sleep(delay)
                    else:
                        raise e
        return wrapper
    return decorator
```

### Task 4: Cache Database Queries

**Objective**: Create a decorator that caches the results of database queries to avoid redundant calls.

**Key Points**:
- Caches the results based on the query string.
- Returns cached results for repeated queries.

```python
def cache_query(func):
    query_cache = {}
    def wrapper(*args, **kwargs):
        query = args[1]  # Assumes the query is the second argument
        if query in query_cache:
            return query_cache[query]
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper
```

## GitHub Repository

You can view or contribute to the project on GitHub:

[GitHub Repository](https://github.com/mosekyle/python-decorators-0x01)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
