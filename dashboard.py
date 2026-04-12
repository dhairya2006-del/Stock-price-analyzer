import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

st.set_page_config(layout="wide")

st.title("📊 Stock Price Analyzer Dashboard")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data/features.csv")
df["date"] = pd.to_datetime(df["date"])

lr = pd.read_csv("data/lr_results.csv")
rf = pd.read_csv("data/rf_results.csv")
xgb = pd.read_csv("data/xgb_results.csv")

lr["date"] = pd.to_datetime(lr["date"])
rf["date"] = pd.to_datetime(rf["date"])
xgb["date"] = pd.to_datetime(xgb["date"])

# =========================
# PRICE CHART
# =========================

st.subheader("📈 Stock Price Trend")

fig1, ax1 = plt.subplots()
ax1.plot(df["date"], df["price"])
ax1.set_xlabel("Date")
ax1.set_ylabel("Price")

st.pyplot(fig1)

# =========================
# MODEL COMPARISON
# =========================

st.subheader("📊 Model Comparison: Actual vs Predicted")

fig2, ax2 = plt.subplots(figsize=(10,5))

# Actual
ax2.plot(lr["date"], lr["actual"], label="Actual", linewidth=2)

# Predictions
ax2.plot(lr["date"], lr["predicted"], label="Linear Regression", linestyle="--")
ax2.plot(rf["date"], rf["predicted"], label="Random Forest", linestyle="--")
ax2.plot(xgb["date"], xgb["predicted"], label="XGBoost", linestyle="--")

ax2.set_title("Actual vs Predicted Prices")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price")
ax2.legend()

st.pyplot(fig2)

# =========================
# ERROR METRICS
# =========================

st.subheader("📊 Model Errors (MAE)")

lr_mae = mean_absolute_error(lr["actual"], lr["predicted"])
rf_mae = mean_absolute_error(rf["actual"], rf["predicted"])
xgb_mae = mean_absolute_error(xgb["actual"], xgb["predicted"])

col1, col2, col3 = st.columns(3)

col1.metric("Linear Regression MAE", f"{lr_mae:.2f}")
col2.metric("Random Forest MAE", f"{rf_mae:.2f}")
col3.metric("XGBoost MAE", f"{xgb_mae:.2f}")