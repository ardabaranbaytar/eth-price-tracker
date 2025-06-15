import sqlite3
from datetime import datetime

def save_price_to_db(price: float):
    conn = sqlite3.connect("database/trades.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO eth_prices (price, timestamp) VALUES (?, ?)", (price, timestamp))
    conn.commit()
    conn.close()
