import pyodbc

# Function to connect to the master database with autocommit enabled
def connect_to_master_with_autocommit():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=master;'
        'UID=sa;'
        'PWD=AnupJha760',
        autocommit=True  # Required for CREATE DATABASE
    )

# Function to connect to the target database
def connect_to_target_database():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=MyDatabase1;'
        'UID=sa;'
        'PWD=AnupJha760'
    )

# Setup database and table
def setup_database():
    # Connect to the master database to create the new database
    conn = connect_to_master_with_autocommit()
    cursor = conn.cursor()

    # Create the database if it doesn't exist
    cursor.execute("""
        IF NOT EXISTS (
            SELECT name 
            FROM sys.databases 
            WHERE name = 'MyDatabase1'
        )
        BEGIN
            CREATE DATABASE MyDatabase1
        END
    """)
    print("Database 'MyDatabase1' created or already exists.")
    conn.close()

    # Connect to the new database
    conn = connect_to_target_database()
    cursor = conn.cursor()

    # Create the Users table if it doesn't exist
    cursor.execute("""
        IF NOT EXISTS (
            SELECT * 
            FROM sysobjects 
            WHERE name = 'Users' AND xtype = 'U'
        )
        CREATE TABLE Users (
            id INT PRIMARY KEY,
            name NVARCHAR(100),
            age INT
        )
    """)

    # Insert data into the Users table
    cursor.execute("""
        INSERT INTO Users (id, name, age)
        VALUES
        (1, 'Anup Jha', 30),
        (2, 'Heerak Mani', 40),
        (3, 'Ganesh Prohorizon', 40)
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Table 'Users' created and data inserted successfully.")

# Run setup
if __name__ == "__main__":
    setup_database()
