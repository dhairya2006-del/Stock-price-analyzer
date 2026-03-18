import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("data/features.csv")

# Create target (next day price)
data["target"] = data["price"].shift(-1)

# Remove last row (no target available)
data = data.dropna()

# Features
X = data[["price", "span", "max_price", "min_price", "profit"]]

# Target
y = data["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluate
error = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", error)

# Example prediction
sample = [[120, 1, 120, 120, 0]]

predicted_price = model.predict(sample)

print("Predicted next price:", predicted_price[0])