import yfinance as yf
import pandas as pd

# choose stock ticker
ticker = "AAPL"

# download historical data
data = yf.download(ticker, period="5y", interval="1d")

# keep only date and closing price
data = data.reset_index()[["Date", "Close"]]

# rename columns for easier C++ parsing
data.columns = ["date", "price"]

# save to csv
data.to_csv("raw_prices.csv", index=False)

print("Dataset saved as raw_prices.csv")
print(data.head())
