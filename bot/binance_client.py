# bot/binance_client.py

from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()  # .env dosyasını yükle

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET)
