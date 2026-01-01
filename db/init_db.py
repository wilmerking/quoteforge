import sqlite3
import os

DB_PATH = "quoteforge.db"

def init_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Materials Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS materials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        density REAL NOT NULL, -- g/cm3
        cost_per_kg REAL NOT NULL
    )
    ''')

    # Processes Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS processes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        setup_cost REAL NOT NULL,
        hourly_rate REAL NOT NULL
    )
    ''')
    
    # Seed Materials
    materials = [
        ('Aluminum 6061', 2.7, 5.0),
        ('Steel 1018', 7.87, 2.0),
        ('Stainless 304', 8.0, 8.0),
        ('ABS Plastic', 1.04, 15.0) # approx
    ]
    cursor.executemany('INSERT OR IGNORE INTO materials (name, density, cost_per_kg) VALUES (?, ?, ?)', materials)

    # Seed Processes
    processes = [
        ('CNC Machining', 50.0, 80.0),
        ('Laser Cutting', 20.0, 120.0),
        ('3D Printing', 10.0, 15.0)
    ]
    cursor.executemany('INSERT OR IGNORE INTO processes (name, setup_cost, hourly_rate) VALUES (?, ?, ?)', processes)

    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH} with sample data.")

if __name__ == "__main__":
    init_db()
