import sqlite3


def create_tables():
    conn = sqlite3.connect("gym.db")
    cursor = conn.cursor()

    # Parent table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            gender TEXT,
            age INTEGER
        )
    """)

    # Child table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memberships (
            membership_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            membership_type TEXT,
            duration_months INTEGER,

            FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id)
        )
    """)

    conn.commit()
    conn.close()


def add_customer(name, gender, age):
    conn = sqlite3.connect("gym.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers (name, gender, age)
        VALUES (?, ?, ?)
    """, (name, gender, age))

    customer_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return customer_id


def add_membership(customer_id, membership_type, duration):
    conn = sqlite3.connect("gym.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memberships
        (customer_id, membership_type, duration_months)
        VALUES (?, ?, ?)
    """, (customer_id, membership_type, duration))

    conn.commit()
    conn.close()



def get_customers_with_membership():
    conn = sqlite3.connect("gym.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            customers.customer_id,
            customers.name,
            customers.gender,
            customers.age,
            memberships.membership_type,
            memberships.duration_months
        FROM customers
        JOIN memberships
        ON customers.customer_id = memberships.customer_id
    """)

    data = cursor.fetchall()

    conn.close()

    return data

