import streamlit as st
from io import BytesIO
from utils.data import *

st.set_page_config(page_title="Mapas", page_icon="🗺️")

st.title("Mapas de Pobreza Extrema")

col1, col2, col3 = st.columns(3, gap="large")

# Get years from data structure (excluding 'Local' column)
years = [year for year in data_com_beneficio.keys() if year != 'Local']

with col1:
    year = st.selectbox(
        "Selecione o ano:",
        sorted(years)  # Sort years in ascending order
    )

with col2:
    benefits = st.radio(
        "Análise de benefícios sociais:",
        ["Com benefícios", "Sem benefícios"],
        index=0
    )

fig = create_poverty_map(year, benefits == "Com Benefícios")

with col3:
    buf = save_fig_to_bytes(fig)
    st.download_button(
        label="Download Mapa",
        data=buf,
        file_name=f"mapa_pobreza_{year}_{'com' if benefits == 'Com Benefícios' else 'sem'}_beneficios.png",
        mime="image/png",
        key=f"download_{year}"
    )

st.pyplot(fig)