import mysql.connector

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    return mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database="ALX_prodev"
    )

def stream_users():
    """
    Generator function to fetch rows from the user_data table one by one.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    finally:
        cursor.close()
        connection.close()

