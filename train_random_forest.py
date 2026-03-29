import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# -------------------------
# Load dataset
# -------------------------
data = pd.read_csv("data/features.csv")

# -------------------------
# Feature Engineering
# -------------------------
data["prev_price"] = data["price"].shift(1)
data["price_change"] = data["price"] - data["price"].shift(1)

# Moving averages
data["ma_5"] = data["price"].rolling(5).mean()
data["ma_10"] = data["price"].rolling(10).mean()

# Volatility
data["volatility"] = data["price"].rolling(5).std()

# Smarter feature
data["ma_ratio"] = data["price"] / data["ma_5"]

# -------------------------
# Target = NEXT DAY CHANGE
# -------------------------
data["target"] = data["price"].shift(-1) - data["price"]

# Remove NaNs
data = data.dropna()

# -------------------------
# Features (UPDATED)
# -------------------------
features = [
    "price",
    "prev_price",
    "price_change",
    "span",
    "ma_5",
    "ma_10",
    "volatility",
    "ma_ratio"
]

X = data[features]
y = data["target"]

# -------------------------
# Time-based split
# -------------------------
split_index = int(len(data) * 0.8)

X_train = X[:split_index]
X_test = X[split_index:]

y_train = y[:split_index]
y_test = y[split_index:]

# -------------------------
# Model
# -------------------------
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------
# Prediction (predict CHANGE)
# -------------------------
predicted_changes = model.predict(X_test)

# Convert to actual prices
actual_prices = X_test["price"].values + y_test.values
predicted_prices = X_test["price"].values + predicted_changes

# -------------------------
# Evaluation
# -------------------------
error = mean_absolute_error(actual_prices, predicted_prices)

print("Mean Absolute Error:", error)

# -------------------------
# Example prediction
# -------------------------
sample = pd.DataFrame(
    [[120, 119, 1, 1, 119, 118, 1.5, 120/119]],
    columns=features
)

predicted_change = model.predict(sample)[0]
predicted_price = sample["price"].values[0] + predicted_change

print("Predicted next price:", predicted_price)