import streamlit as st
from utils.data import *

st.set_page_config(page_title="Análises", page_icon="📈")

st.title("Histórico de Pobreza Extrema")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    view_level = st.radio(
        "Nível de análise:",
        ["Nacional", "Regional"],
        index=0
    )

with col2:
    benefits = st.radio(
        "Tipo de Análise:",
        ["Com Benefícios", "Sem Benefícios"],
        index=0
    )
    
if view_level == "Regional":
    region = st.selectbox(
        "Selecione a região:",
        list(regions.keys())
    )
    fig = plot_region_comparison(region, benefits == "Com Benefícios")
else:
    fig = plot_national_comparison(benefits == "Com Benefícios")

with col3:
    buf = save_fig_to_bytes(fig)
    st.download_button(
        label="Download Gráfico",
        data=buf,
        file_name=f"analise_pobreza_{view_level.lower()}_{'com' if benefits == 'Com Benefícios' else 'sem'}_beneficios.png",
        mime="image/png",
        key=f"download_{view_level}"
    )

# st.plotly_chart(fig)
st.pyplot(fig)