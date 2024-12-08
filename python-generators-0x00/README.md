# Getting Started with Python Generators and SQL

This project demonstrates the use of Python for managing MySQL databases and preparing a foundation for working with generators to stream rows from a database. The focus is on setting up the database, populating it with sample data, and preparing for advanced generator-based data handling.

## Prerequisites

1. **Python**: Ensure Python 3.7 or higher is installed on your system.
2. **MySQL**: Install and configure MySQL Server.
3. **Dependencies**:
    - `mysql-connector-python`
    - `csv`

   Install the required Python package using pip:
   ```bash
   pip install mysql-connector-python
   ```

4. **CSV Data**: Ensure you have the `user_data.csv` file containing sample user data.

## Overview

The project comprises the following functionalities:

- **Database Connection**: Connect to the MySQL server.
- **Database Creation**: Create the `ALX_prodev` database if it doesn't exist.
- **Table Creation**: Create the `user_data` table with the specified schema.
- **Data Insertion**: Populate the table with data from a CSV file.

## File Structure

- `seed.py`: Contains the logic for database setup and data insertion.
- `0-main.py`: Entry point to execute the functions in `seed.py`.
- `user_data.csv`: Sample data file for populating the database.

## Functions in `seed.py`

1. **`connect_db()`**:
   - Connects to the MySQL database server.

2. **`create_database(connection)`**:
   - Creates the `ALX_prodev` database if it doesn't exist.

3. **`connect_to_prodev()`**:
   - Connects to the `ALX_prodev` database.

4. **`create_table(connection)`**:
   - Creates the `user_data` table with the following schema:
     ```sql
     user_id CHAR(36) PRIMARY KEY,
     name VARCHAR(255) NOT NULL,
     email VARCHAR(255) NOT NULL,
     age DECIMAL(3, 0) NOT NULL
     ```

5. **`insert_data(connection, csv_file)`**:
   - Inserts data into the `user_data` table from the specified CSV file.

## Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/alx-backend-python
   cd alx-backend-python/python-generators-0x00
   ```

2. Place the `user_data.csv` file in the project directory.

3. Update `seed.py` with your MySQL credentials:
   ```python
   user="your_username"
   password="your_password"
   ```

4. Run the script:
   ```bash
   python3 0-main.py
   ```

## Sample Output

On successful execution, the script will:
- Confirm the database and table creation.
- Insert data from the CSV file.
- Display a sample of rows from the table.

```plaintext
connection successful
Table user_data created successfully
Database ALX_prodev is present
[('00234e50-34eb-4ce2-94ec-26e3fa749796', 'Dan Altenwerth Jr.', 'Molly59@gmail.com',
