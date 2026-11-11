import streamlit as st
from app.data.career_map import get_career_map

# Set page config
st.set_page_config(page_title="Career Map Explorer", layout="wide")

# Wise-inspired custom CSS
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h1, h2, h3 {
        color: #2e4369;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

st.title("Career Map Explorer")

career_map = get_career_map()

# Simple navigation
selected_level = st.selectbox(
    "Select Level",
    options=[level.id for level in career_map.levels],
    format_func=lambda x: career_map.get_level(x).name
)

level_data = career_map.get_level(selected_level)

if level_data:
    st.header(level_data.name)
    st.subheader("Dimensions")
    for dim in level_data.dimensions:
        st.write(f"**{dim.name}**: {dim.question}")
        lvl_exp = dim.get_level(level_data.id)
        if lvl_exp:
            st.write(f"- {lvl_exp.description}")
