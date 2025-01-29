import streamlit as st
from utils.data import *

st.set_page_config(page_title="Projeções", page_icon="📊")
st.title("Projeções para 2030")

col1, col2 = st.columns(2)

with col1:
    benefits = st.radio(
        "Análise considerando benefícios sociais:",
        ["Com Benefícios", "Sem Benefícios"],
        index=0
    )

with col2:
    analysis_type = st.radio(
        "Tipo de análise:",
        ["Nacional", "Regional", "Estadual"],
        index=0
    )

if analysis_type == "Regional":
    macro_regions = ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']
    selected = st.selectbox("Selecione a região:", macro_regions)
elif analysis_type == "Estadual":
    states = [state for state in data_com_beneficio['Local'] 
             if state not in ['Brasil', 'Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']]
    selected = st.selectbox("Selecione o estado:", sorted(states))
else:
    selected = None

metrics = calculate_projection(
    analysis_type, 
    selected, 
    benefits == "Com Benefícios"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Taxa Atual (2023)",
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

st.metric(
    label="Redução Anual Necessária para Zerar até 2030",
    value=f"{metrics['required_reduction']:.2f}%"
)