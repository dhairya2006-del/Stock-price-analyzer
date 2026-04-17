import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

# PAGE CONFIG
st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📊 Stock Price Analyzer")

# LOAD DATA
df = pd.read_csv("data/features.csv")
df["date"] = pd.to_datetime(df["date"])

lr = pd.read_csv("data/lr_results.csv")
rf = pd.read_csv("data/rf_results.csv")
xgb = pd.read_csv("data/xgb_results.csv")

lr["date"] = pd.to_datetime(lr["date"])
rf["date"] = pd.to_datetime(rf["date"])
xgb["date"] = pd.to_datetime(xgb["date"])


# SIDEBAR NAVIGATION

st.sidebar.title("📂 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["📈 Price Dashboard", "📊 Model Comparison", "📉 Performance Metrics"]
)


# PAGE 1: PRICE DASHBOARD

if page == "📈 Price Dashboard":

    st.header("📈 Stock Price Trend")

    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(df["date"], df["price"], color="black", linewidth=2)
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    st.pyplot(fig)


# PAGE 2: MODEL COMPARISON

elif page == "📊 Model Comparison":

    st.header("📊 Model-wise Comparison")

    
    # Linear Regression (Green)
    
    st.subheader("🟢 Linear Regression")

    fig1, ax1 = plt.subplots(figsize=(10,4))

    ax1.plot(
        lr["date"], lr["actual"],
        label="Actual",
        linewidth=2,
        color="dodgerblue"
    )

    ax1.plot(
        lr["date"], lr["predicted"],
        label="Predicted",
        linestyle="-.",
        color="green"
    )

    ax1.set_title("Linear Regression vs Actual")
    ax1.legend()

    st.pyplot(fig1)

    
    # Random Forest (Orange)
    
    st.subheader("🟠 Random Forest")

    fig2, ax2 = plt.subplots(figsize=(10,4))

    ax2.plot(
        rf["date"], rf["actual"],
        label="Actual",
        linewidth=2,
        color="dodgerblue"
    )

    ax2.plot(
        rf["date"], rf["predicted"],
        label="Predicted",
        linestyle="-.",
        color="orange"
    )

    ax2.set_title("Random Forest vs Actual")
    ax2.legend()

    st.pyplot(fig2)

    
    # XGBoost (Red)
    
    st.subheader("🔴 XGBoost")

    fig3, ax3 = plt.subplots(figsize=(10,4))

    ax3.plot(
        xgb["date"], xgb["actual"],
        label="Actual",
        linewidth=2,
        color="dodgerblue"
    )

    ax3.plot(
        xgb["date"], xgb["predicted"],
        label="Predicted",
        linestyle="-.",
        color="red"
    )

    ax3.set_title("XGBoost vs Actual")
    ax3.legend()

    st.pyplot(fig3)


# PAGE 3: PERFORMANCE METRICS

elif page == "📉 Performance Metrics":

    st.header("📊 Model Performance")

    lr_mae = mean_absolute_error(lr["actual"], lr["predicted"])
    rf_mae = mean_absolute_error(rf["actual"], rf["predicted"])
    xgb_mae = mean_absolute_error(xgb["actual"], xgb["predicted"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Linear Regression", f"{lr_mae:.2f}")
    col2.metric("Random Forest", f"{rf_mae:.2f}")
    col3.metric("XGBoost", f"{xgb_mae:.2f}")

    # Best model
    best_model = min(
        [("Linear Regression", lr_mae),
         ("Random Forest", rf_mae),
         ("XGBoost", xgb_mae)],
        key=lambda x: x[1]
    )

    st.success(f"🏆 Best Model: {best_model[0]} (MAE = {best_model[1]:.2f})")

# to run : streamlit run dashboard.py