def save_price_to_db(price: float, timestamp: str):
    conn = sqlite3.connect("database/trades.db")
    c = conn.cursor()
    c.execute("INSERT INTO eth_prices (price, timestamp) VALUES (?, ?)", (price, timestamp))
    conn.commit()
    conn.close()

