import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = "database/trades.db"

def create_table_if_not_exists():
  
    Path("database").mkdir(parents=True, exist_ok=True)  
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS eth_prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                price REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        conn.commit()

def save_price_to_db(price: float, timestamp: str):
    
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO eth_prices (price, timestamp) VALUES (?, ?)",
            (price, timestamp)
        )
        conn.commit()


