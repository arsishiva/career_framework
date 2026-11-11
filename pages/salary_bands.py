import streamlit as st
import pandas as pd

st.set_page_config(page_title="Salary Bands", layout="wide")

st.title("💰 Regional Salary Bands")

# Load salary data
df = pd.read_csv("app/data/salary_bands.csv")

# Filter/Search functionality
location = st.multiselect("Filter by Location", options=df["location"].unique())
if location:
    df = df[df["location"].isin(location)]

st.table(df)
