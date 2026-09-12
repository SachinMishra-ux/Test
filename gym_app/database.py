import sqlite3


def create_table():
    conn = sqlite3.connect("gym.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            gender TEXT,
            age INTEGER,
            membership TEXT,
            weight REAL
        )
    """)

    conn.commit()
    conn.close()


def add_customer(name, gender, age, membership, weight):
    conn = sqlite3.connect("gym.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers
        (name, gender, age, membership, weight)
        VALUES (?, ?, ?, ?, ?)
    """, (name, gender, age, membership, weight))

    conn.commit()
    conn.close()


def get_customers():
    conn = sqlite3.connect("gym.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()

    conn.close()

    return data

