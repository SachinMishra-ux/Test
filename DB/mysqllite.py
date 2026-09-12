import sqlite3

# Connect to database
conn = sqlite3.connect("mydb.db")

# Create cursor
cursor = conn.cursor()


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Insert data
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Sachin",))

# Save changes
conn.commit()

# Read data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close connection
conn.close()