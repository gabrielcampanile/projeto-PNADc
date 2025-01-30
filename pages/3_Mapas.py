import streamlit as st
from io import BytesIO
from utils.data import *

st.set_page_config(page_title="Mapas", page_icon="🗺️")

st.title("Mapas de Pobreza Extrema")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    map_type = st.radio(
        "Tipo de Mapa:",
        ["Histórico", "Projeção 2030"],
        index=0
    )

with col2:
    benefits = st.radio(
        "Tipo de Análise:",
        ["Com Benefícios", "Sem Benefícios"],
        index=0
    )

# Show year selection only for current map
if map_type == "Histórico":
    years = [year for year in data_com_beneficio.keys() if year != 'Local']
    year = st.selectbox(
        "Selecione o ano:",
        sorted(years, reverse=True)
    )
else:
    year = '2023'

# Create map with projection if selected
fig = create_poverty_map(year, 
                        benefits == "Com Benefícios", 
                        show_projection=(map_type == "Projeção 2030"))

with col3:
    buf = save_fig_to_bytes(fig)
    file_year = "2030" if map_type == "Projeção 2030" else year
    st.download_button(
        label="Download Mapa",
        data=buf,
        file_name=f"mapa_pobreza_{file_year}_{'com' if benefits == 'Com Benefícios' else 'sem'}_beneficios.png",
        mime="image/png",
        key=f"download_{file_year}"
    )

st.pyplot(fig)