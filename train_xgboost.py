import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("data/features.csv")

# 🔥 Simulate sentiment
df["sentiment"] = df["price"].pct_change()

# 🔥 Lagged sentiment
df["sentiment_lag1"] = df["sentiment"].shift(1)

# 🔥 Target
df["target"] = df["price"].shift(-1) - df["price"]

# Drop NaNs
df = df.dropna()

# Features
features = [
    "price",
    "span",
    "max_price",
    "min_price",
    "profit",
    "sentiment_lag1"
]

X = df[features]
y = df["target"]

# Time-based split
split = int(len(df) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

# Model
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
preds = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, preds)

print("XGBoost MAE:", mae)

results = pd.DataFrame({
    "date": df["date"].iloc[split:],
    "actual": df["price"].iloc[split:],
    "predicted": df["price"].iloc[split:] + preds
})

results.to_csv("data/xgb_results.csv", index=False)