import pandas as pd
from xgboost import XGBRegressor
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

# -------------------------
# Target = NEXT DAY PRICE CHANGE
# -------------------------
data["target"] = data["price"].shift(-1) - data["price"]

# Remove NaN rows
data = data.dropna()

# -------------------------
# Features
# -------------------------
features = [
    "price",
    "prev_price",
    "price_change",
    "span",
    "max_price",
    "min_price",
    "profit"
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
model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# -------------------------
# Prediction (predict CHANGE)
# -------------------------
predicted_changes = model.predict(X_test)

# Convert to actual price
actual_prices = X_test["price"].values + y_test.values
predicted_prices = X_test["price"].values + predicted_changes

# -------------------------
# Evaluation (on actual price)
# -------------------------
error = mean_absolute_error(actual_prices, predicted_prices)

print("Mean Absolute Error:", error)

# -------------------------
# Example prediction
# -------------------------
sample = pd.DataFrame(
    [[120, 119, 1, 1, 120, 118, 2]],
    columns=features
)

predicted_change = model.predict(sample)[0]
predicted_price = sample["price"].values[0] + predicted_change

print("Predicted next price:", predicted_price)