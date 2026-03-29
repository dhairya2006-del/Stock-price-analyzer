import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# -------------------------
# Load dataset
# -------------------------
data = pd.read_csv("data/features.csv")

# -------------------------
# Create target (next day price)
# -------------------------
data["target"] = data["price"].shift(-1)

# Remove last row (no target)
data = data.dropna()

# -------------------------
# Features and target
# -------------------------
features = ["price", "span", "max_price", "min_price", "profit"]

X = data[features]
y = data["target"]

# -------------------------
# Time-based split (NO data leakage)
# -------------------------
split_index = int(len(data) * 0.8)

X_train = X[:split_index]
X_test = X[split_index:]

y_train = y[:split_index]
y_test = y[split_index:]

# -------------------------
# Model
# -------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------
# Prediction
# -------------------------
predictions = model.predict(X_test)

# -------------------------
# Evaluation
# -------------------------
error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", error)

# -------------------------
# Example prediction (FIXED WARNING)
# -------------------------
sample = pd.DataFrame(
    [[120, 1, 120, 120, 0]],
    columns=features
)

predicted_price = model.predict(sample)
print("Predicted next price:", predicted_price[0])

#Mean Absolute Error: 2.8093588790129362
# Predicted next price: 118.87620069662505
