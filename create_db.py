import pyodbc

# Database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=master;'  # Connect to the default "master" database for DB creation
    'UID=sa;'
    'PWD=AnupJha760'
)
cursor = conn.cursor()

# SQL commands to create database and table
cursor.execute("IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'MyDatabase1') CREATE DATABASE MyDatabase1")
conn.commit()

# Connect directly to MyDatabase1 for further operations
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=MyDatabase1;'
    'UID=sa;'
    'PWD=AnupJha760'
)
cursor = conn.cursor()

# Create table and insert data
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
    CREATE TABLE Users (
        id INT PRIMARY KEY,
        name NVARCHAR(100),
        age INT
    )
""")
cursor.execute("""
    INSERT INTO Users (id, name, age)
    VALUES
    (1, 'Anup Jha', 30),
    (2, 'Heerak Mani', 40),
    (3, 'Ganesh Prohorizon', 40)
""")

# Commit and close
conn.commit()
conn.close()

print("Database and table created successfully!")
