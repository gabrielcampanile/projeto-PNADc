import streamlit as st
from io import BytesIO
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
        "Análise de benefícios sociais:",
        ["Com benefícios", "Sem benefícios"],
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

st.pyplot(fig)

# Add metrics section
if view_level == "Regional":
    metrics = calculate_projection("Regional", region, benefits == "Com Benefícios")
    region_name = region
else:
    metrics = calculate_projection("Nacional", "Brasil", benefits == "Com Benefícios")
    region_name = "Brasil"

# Display metrics in columns
st.markdown("---")  # Add separator
st.subheader("Métricas de Pobreza")

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