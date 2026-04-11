import yfinance as yf
import pandas as pd

# choose stock ticker
ticker = "AAPL"

# ✅ USE RECENT DATA ONLY (IMPORTANT)
data = yf.download(ticker, start="2024-01-01", interval="1d")

# keep only date and closing price
data = data.reset_index()[["Date", "Close"]]

# rename columns
data.columns = ["date", "price"]

# save
data.to_csv("raw_prices.csv", index=False)

print("Dataset saved as raw_prices.csv")
print(data.head())