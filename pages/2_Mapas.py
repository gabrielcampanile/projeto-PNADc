import streamlit as st
from utils.data import *

st.set_page_config(page_title="Mapas", page_icon="🗺️")

st.title("Mapas de Pobreza Extrema")

col1, col2 = st.columns(2)

# Get years from data structure (excluding 'Local' column)
years = [year for year in data_com_beneficio.keys() if year != 'Local']

with col1:
    year = st.selectbox(
        "Selecione o ano:",
        sorted(years)  # Sort years in ascending order
    )

with col2:
    benefits = st.radio(
        "Análise considerando benefícios sociais:",
        ["Com Benefícios", "Sem Benefícios"],
        index=0
    )

fig = create_poverty_map(year, benefits == "Com Benefícios")
st.pyplot(fig)