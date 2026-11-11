import streamlit as st
import json
import pandas as pd

# Page configuration
st.set_page_config(page_title="Career Map Matrix", layout="wide")

st.markdown("""
<style>
    .main { background-color: #ffffff; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h1 { color: #163300; font-weight: 700; }
    .stTable table { width: 100%; border-collapse: collapse; }
    .stTable th, .stTable td { padding: 12px; border: 1px solid #16330014; }
</style>
""", unsafe_allow_html=True)

st.title("Analytics Career Map Matrix")

# Load data
with open("app/data/career_framework_data.json", "r") as f:
    data = json.load(f)

# Combine dimensions and skills
all_components = data["dimensions"] + data["technical_skills"]

# Build a matrix (Rows: Levels, Cols: Dimensions/Skills)
levels = ["IC1", "IC2", "IC3", "IC4", "AL1", "AL2", "AL3"]
matrix = pd.DataFrame(index=levels, columns=[c["name"] if "name" in c else c["area"] for c in all_components])

# Populate matrix
for comp in all_components:
    col_name = comp["name"] if "name" in comp else comp["area"]
    for level_exp in comp["levels"]:
        if level_exp["level"] in levels:
            matrix.at[level_exp["level"], col_name] = level_exp["description"]

st.table(matrix)
