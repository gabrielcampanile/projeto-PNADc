import streamlit as st
from utils.data import *

st.set_page_config(
    page_title="Introdução",
    page_icon="📊",
    layout="wide"
)

st.title("Análise de Pobreza Extrema no Brasil")

st.markdown("""
Esta aplicação apresenta análises sobre a pobreza extrema no Brasil entre 2015 e 2023,
com projeções até 2030. Os dados são analisados em diferentes níveis e perspectivas.

Utilize o menu lateral para explorar as diferentes visualizações disponíveis:

1. **Apresentação**: Introdução e métricas principais
2. **Análises**: Evolução temporal da pobreza extrema e comparativo entre regiões e estados
3. **Mapas**: Visualização geográfica da distribuição
4. **Projeções**: Projeções de pobreza extrema até 2030
5. **Resultados**: Tabelas e gráficos dos resultados obtidos
6. **Relatório**: Relatório completo com todas as análises
""")

