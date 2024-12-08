import sqlite3
import functools

def log_queries(func):
    """Decorator to log SQL queries."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query", args[0] if args else None)
        if query:
            print(f"Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

