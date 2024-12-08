import mysql.connector
import csv
import os
from mysql.connector import Error
import uuid

def connect_db():
    """Connect to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="",  
            password=""
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database(connection):
    """Create the ALX_prodev database if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="",  
            password="",
            database="ALX_prodev"
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None

def create_table(connection):
    """Create the user_data table if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3, 0) NOT NULL
            );
            """
        )
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_data(connection, csv_file):
    """Insert data from the CSV file into the user_data table."""
    try:
        if not os.path.exists(csv_file):
            print(f"CSV file {csv_file} not found.")
            return

        cursor = connection.cursor()
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                try:
                    cursor.execute(
                        """
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        name=VALUES(name), email=VALUES(email), age=VALUES(age);
                        """,
                        (user_id, name, email, age)
                    )
                except Error as e:
                    print(f"Error inserting row {row}: {e}")

        connection.commit()
        cursor.close()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data: {e}")

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~OA
~
~
~
~
~
~
seed.py [unix] (02:59 01/01/1970)                                                                                                                                                      0,0-1 All
"seed.py" [New]

