from .binance_client import client

def get_price():
    ticker = client.get_symbol_ticker(symbol="ETHUSDT")
    return float(ticker["price"])
