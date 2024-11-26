from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    """
    Fetch all user records from the database.
    """
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = connection.cursor()
    try:
        query = "SELECT * FROM Users"
        cursor.execute(query)
        
        # Fetch all rows and convert to a list of dictionaries
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        return jsonify(results), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to fetch users"}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
