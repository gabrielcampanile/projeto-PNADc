import streamlit as st
from utils.data import *

st.set_page_config(page_title="Projeções", page_icon="📈")

st.title("Projeções de Pobreza Extrema até 2030")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    view_type = st.radio(
        "Nível de Análise:",
        ["Nacional", "Regional"],
        index=0
    )

with col2:
    benefits = st.radio(
        "Tipo de Análise:",
        ["Com Benefícios", "Sem Benefícios"],
        index=0
    )

# Create appropriate plot based on view type
if view_type == "Nacional":
    fig = plot_national_projection(benefits == "Com Benefícios")
    filename = f"projecao_nacional"
else:
    region = st.selectbox("Selecione a região:", list(regions.keys()))
    fig = plot_region_projection(region, regions[region], benefits == "Com Benefícios")
    filename = f"projecao_{region.lower()}"

# Add download button
with col3:
    buf = save_fig_to_bytes(fig)
    st.download_button(
        label="📥 Download Gráfico",
        data=buf,
        file_name=f"{filename}_{'com' if benefits == 'Com Benefícios' else 'sem'}_beneficios.png",
        mime="image/png"
    )

# Display plot
st.pyplot(fig)

# Update metrics calculation
if view_type == "Regional":
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
        value=f"{metrics['current_rate']:.2f}%",
        delta=f"{-metrics['observed_reduction']:.2f}%",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="Projeção 2030",
        value=f"{metrics['projection_2030']:.2f}%"
    )

with col3:
    st.metric(
    label="Redução Anual Necessária para Zerar até 2030",
    value=f"{metrics['required_reduction']:.2f}%"
)