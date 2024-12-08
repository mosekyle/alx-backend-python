from seed import connect_to_prodev

def stream_user_ages():
    """
    Generator function to stream user ages one by one from the user_data table.
    Yields:
        int: Age of the user.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT age FROM user_data")
        for (age,) in cursor:
            yield age
    finally:
        cursor.close()
        connection.close()

def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.
    Prints:
        Average age of users.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    average_age = total_age / count if count > 0 else 0
    print(f"Average age of users: {average_age:.2f}")

