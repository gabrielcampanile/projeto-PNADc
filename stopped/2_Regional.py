import streamlit as st
from utils.data import *

st.set_page_config(page_title="Análise Regional", page_icon="🗺️")

st.title("Análise Regional")

benefits = st.radio(
    "Análise considerando benefícios sociais:",
    ["Com Benefícios", "Sem Benefícios"],
    index=0
)

region = st.selectbox(
    "Selecione a região:",
    list(regions.keys())
)

fig = plot_region_comparison(region, benefits == "Com Benefícios")
st.pyplot(fig)

# Métricas regionais
metrics = calculate_projection("Regional", region, benefits == "Com Benefícios")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label=f"Taxa Atual (2023) - {region}",
        value=f"{metrics['current_rate']:.2f}%"
    )

with col2:
    st.metric(
        label="Redução Anual Observada",
        value=f"{metrics['observed_reduction']:.2f}%"
    )

with col3:
    st.metric(
        label="Projeção 2030",
        value=f"{metrics['projection_2030']:.2f}%"
    )