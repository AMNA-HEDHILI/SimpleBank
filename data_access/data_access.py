import sqlite3
import os

# Define database path
DB_PATH = os.path.join("data", "bank.db")

# ✅ Single correct connection function
def get_connection():
    return sqlite3.connect(DB_PATH)

# ✅ Create accounts table
def create_accounts_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ✅ Insert new account
def insert_account(name, balance):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))
    conn.commit()
    conn.close()

# ✅ Fetch all accounts
def get_all_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    results = cursor.fetchall()
    conn.close()
    return results
