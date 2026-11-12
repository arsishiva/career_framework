import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Salary Bands", layout="wide")

st.title("💰 Regional Salary Bands (USD Equivalent)")

# Load salary data
df = pd.read_csv("app/data/salary_bands.csv")

# Currency conversion rates
rates = {
    "GBP": 1.30,
    "EUR": 1.08,
    "HUF": 0.0025,
    "SGD": 0.75,
    "USD": 1.00,
    "BRL": 0.18,
    "INR": 0.012
}

# Add USD columns
df["Min Salary (USD)"] = (df["min_salary"] * df["currency"].map(rates)).round(0)
df["Max Salary (USD)"] = (df["max_salary"] * df["currency"].map(rates)).round(0)
df["Avg Salary (USD)"] = ((df["Min Salary (USD)"] + df["Max Salary (USD)"]) / 2).round(0)

# Display table
st.dataframe(
    df[["level", "location", "Min Salary (USD)", "Max Salary (USD)"]],
    use_container_width=True,
    hide_index=True,
    column_config={
        "Min Salary (USD)": st.column_config.NumberColumn("Min Salary (USD)", format="$%d"),
        "Max Salary (USD)": st.column_config.NumberColumn("Max Salary (USD)", format="$%d"),
    }
)

st.subheader("Salary Heatmap Matrix (Average Salary)")
# Pivot matrix
pivot_df = df.pivot(index="level", columns="location", values="Avg Salary (USD)")

# Sort by default high to low for convenience
pivot_df = pivot_df[pivot_df.mean().sort_values(ascending=False).index]

# Use st.dataframe for interactive sorting (built-in)
st.dataframe(
    pivot_df.style.background_gradient(cmap="RdYlGn_r", axis=1).format("{:,.0f}"),
    use_container_width=True
)
