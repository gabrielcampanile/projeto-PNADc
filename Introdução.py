import streamlit as st
from utils.data import *

st.set_page_config(
    page_title="Análise de Pobreza Extrema",
    page_icon="📊",
    layout="wide"
)

# st.sidebar.page_link("streamlit_app.py", label="Início", icon="🏠")
# st.sidebar.page_link("pages/1_Historico.py", label="Histórico", icon="📊")
# st.sidebar.page_link("pages/2_Regional.py", label="Regional", icon="⚙️")
# st.sidebar.page_link("pages/3_Mapas.py", label="Mapas", icon="⚙️")
# st.sidebar.page_link("pages/4_Projecoes.py", label="Projeções", icon="⚙️")

st.title("Análise de Pobreza Extrema no Brasil")

st.markdown("""
Esta aplicação apresenta análises sobre a pobreza extrema no Brasil entre 2015 e 2023,
com projeções até 2030. Os dados são analisados em diferentes níveis e perspectivas.

Utilize o menu lateral para explorar as diferentes análises:

1. **Histórico**: Evolução temporal da pobreza extrema e comparativo entre regiões e estados
2. **Mapas**: Visualização geográfica da distribuição
3. **Resultados**: Tabelas e gráficos dos resultados obtidos
""")

# Métricas principais
col1, col2, col3 = st.columns(3)

national_metrics = calculate_projection("Nacional")
with col1:
    st.metric(
        label="Taxa Nacional 2023",
        value=f"{national_metrics['current_rate']:.2f}%",
        delta=f"{-national_metrics['observed_reduction']:.2f}%",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="Projeção Nacional 2030",
        value=f"{national_metrics['projection_2030']:.2f}%"
    )

with col3:
    st.metric(
        label="Redução Anual Necessária",
        value=f"{national_metrics['required_reduction']:.2f}%"
    )