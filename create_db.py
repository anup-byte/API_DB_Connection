import pyodbc

# Database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=master;'
    'UID=sa;'
    'PWD=AnupJha760'
)
cursor = conn.cursor()

# SQL commands
cursor.execute("CREATE DATABASE MyDatabase")
cursor.execute("USE MyDatabase")
cursor.execute("""
    CREATE TABLE Users (
        id INT PRIMARY KEY,
        name NVARCHAR(100),
        age INT
    )
""")
cursor.execute("""
    INSERT INTO Users (id, name, age)
    VALUES
    (1, 'John Doe', 30),
    (2, 'Jane Smith', 25),
    (3, 'Alice Johnson', 35)
""")

# Commit and close
conn.commit()
conn.close()

print("Database and table created successfully!")
