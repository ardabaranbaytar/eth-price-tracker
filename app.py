from flask import Flask, render_template, jsonify
from bot.binance_client import client
from bot.price_fetcher import get_price
from datetime import datetime
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/ethprice")
def eth_price():
    # Binance API'den 1 dakikalık veriler çekilir
    klines = client.get_klines(symbol="ETHUSDT", interval="1m", limit=60)

    df = pd.DataFrame(klines, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "num_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    # Zamanı formatla (UTC+3 Türkiye saati)
    df["time"] = (
        pd.to_datetime(df["open_time"], unit="ms") + pd.Timedelta(hours=3)
    ).dt.strftime("%H:%M:%S")

    df["close"] = df["close"].astype(float)

    return jsonify({
        "labels": df["time"].tolist(),
        "data": df["close"].tolist()
    })

@app.route("/api/live_price")
def live_price():
    try:
        price = get_price()
        time_str = datetime.now().strftime("%H:%M:%S")
        return jsonify({"price": price, "timestamp": time_str})
    except Exception as e:
        print("Hata:", e)
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)
