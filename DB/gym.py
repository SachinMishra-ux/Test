import sqlite3

# Connect to database
conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

# Create customer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    age INTEGER,
    membership TEXT,
    weight REAL
)
""")

# Insert customer data
customers = [
    (1, "Rahul", "Male", 25, "Monthly", 72.5),
    (2, "Priya", "Female", 28, "Yearly", 58.0),
    (3, "Amit", "Male", 32, "Monthly", 85.2),
    (4, "Neha", "Female", 24, "Quarterly", 62.5),
    (5, "Rohit", "Male", 29, "Yearly", 78.3)
]

cursor.executemany("""
INSERT INTO customers
(id, name, gender, age, membership, weight)
VALUES (?, ?, ?, ?, ?, ?)
""", customers)

# Save changes
conn.commit()

# Display data
cursor.execute("SELECT * FROM customers")

for customer in cursor.fetchall():
    print(customer)

# Close database
conn.close()