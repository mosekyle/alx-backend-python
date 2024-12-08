from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """
    Fetches a single page of users from the database.
    Args:
        page_size (int): Number of users per page.
        offset (int): Offset to start fetching data from.
    Returns:
        list[dict]: A list of user records as dictionaries.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        connection.close()

def lazy_paginate(page_size):
    """
    Generator function to lazily load pages of users.
    Args:
        page_size (int): Number of users per page.
    Yields:
        list[dict]: A page of user records as dictionaries.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

