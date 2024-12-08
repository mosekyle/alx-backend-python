import mysql.connector

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    return mysql.connector.connect(
        host="localhost",
        user="",  
        password="",
        database="ALX_prodev"
    )

def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows in batches from the user_data table.
    Args:
        batch_size (int): The number of rows to fetch per batch.
    Yields:
        list[dict]: A batch of rows as dictionaries.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """
    Processes batches to filter users over the age of 25.
    Args:
        batch_size (int): The number of rows to process per batch.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)

