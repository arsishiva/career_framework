import streamlit as st
import json
import pandas as pd

# Page configuration
st.set_page_config(page_title="Career Map Expectations", layout="wide")

# Wise-inspired custom CSS
st.markdown("""
<style>
    :root {
        --primary: #163300;
        --secondary: #9fe870;
        --tertiary: #16330014;
    }
    .main { background-color: #ffffff; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h1, h2, h3 { color: var(--primary); font-weight: 700; }
    .stTable table { width: 100%; border-collapse: collapse; }
    .stTable th, .stTable td { padding: 12px; border: 1px solid var(--tertiary); }
</style>
""", unsafe_allow_html=True)

st.title("Analytics Career Map: Expectations")

# Load data
with open("app/data/career_framework_data.json", "r") as f:
    data = json.load(f)

# Sidebar for navigation
category = st.sidebar.selectbox("Category", ["Dimensions", "Technical Skills"])

if category == "Dimensions":
    st.header("Responsibilities & Dimensions")
    for dim in data["dimensions"]:
        with st.expander(f"**{dim['name']}** ({dim['category']})"):
            st.write(f"*{dim['question']}*")
            # Create a table for level-wise expectations
            df = pd.DataFrame(dim["levels"])
            st.table(df)
else:
    st.header("Technical Skills")
    for skill in data["technical_skills"]:
        with st.expander(f"**{skill['area']}**"):
            st.write(f"*{skill['question']}*")
            df = pd.DataFrame(skill["levels"])
            st.table(df)
