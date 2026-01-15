import sqlite3

def run():
    # Connect to a db
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    # Create a simple table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    """)

    # Insert data
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

    # Read data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Commit changes and close
    conn.commit()
    conn.close()
