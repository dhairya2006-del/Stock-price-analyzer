import pandas as pd

# Load data
df = pd.read_csv("data/features.csv")

# Sort by date
df = df.sort_values(by='date')

# =========================
# SMA
# =========================
df['sma_5'] = df['price'].rolling(window=5).mean()
df['sma_20'] = df['price'].rolling(window=20).mean()

# =========================
# RSI
# =========================
delta = df['price'].diff()

gain = (delta.where(delta > 0, 0)).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()

rs = gain / loss
df['rsi'] = 100 - (100 / (1 + rs))

# =========================
# MACD
# =========================
ema_12 = df['price'].ewm(span=12, adjust=False).mean()
ema_26 = df['price'].ewm(span=26, adjust=False).mean()

df['macd'] = ema_12 - ema_26

# Drop NaN
df = df.dropna()

# Save output
df.to_csv("../output/features_with_indicators.csv", index=False)

print("Feature engineering complete!")