import streamlit as st
import pandas as pd
import plotly.express as px

def get_excel_file_as_bytes(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

# Data with benefits
data_com_beneficios = {
    'Local': ['Brasil', 'Norte', 'RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'Nordeste', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'Sudeste', 'MG', 'ES', 'RJ', 'SP', 'Sul', 'PR', 'SC', 'RS', 'Centro-Oeste', 'MS', 'MT', 'GO', 'DF'],
    'Situação Atual 2023 (%)': [4.4, 5.97, 4.38, 13.24, 6.63, 7.2, 5.72, 3.6, 4.24, 9.08, 12.22, 8.05, 9.39, 6.32, 7.37, 9.31, 8.81, 8.08, 8.8, 2.5, 2.18, 2.66, 3.61, 2.21, 1.67, 2.23, 1.41, 1.28, 1.82, 1.98, 2.6, 1.32, 1.94],
    'Taxa de Redução Anual (%)': [0.09, 0.47, 0.14, 0.18, 0.73, -0.28, 0.7, 0.75, 0.35, 0.27, 1.09, 0.91, 0.55, 0.58, 0.17, 0.25, 0.71, 0.62, 0.66, 0.01, 0.27, 0.35, -0.06, 0.03, 0.05, 0.01, 0, 0.11, 0.14, 0.08, 0.02, 0.24, 0.09],
    'Projeção 2030 (%)': [3.77, 2.67, 3.43, 11.98, 1.51, 9.14, 0.82, 0, 1.81, 7.19, 4.59, 1.68, 5.54, 2.24, 6.15, 7.57, 3.82, 3.76, 4.2, 2.4, 0.32, 0.24, 4, 2.02, 1.35, 2.18, 1.42, 0.5, 0.86, 1.45, 2.47, 0, 1.28],
    'Taxa Necessária Anual (%)': [0.63, 0.85, 0.63, 1.89, 0.95, 1.03, 0.82, 0.51, 0.61, 1.3, 1.75, 1.15, 1.34, 0.9, 1.05, 1.33, 1.26, 1.15, 1.26, 0.36, 0.31, 0.38, 0.52, 0.32, 0.24, 0.32, 0.2, 0.18, 0.26, 0.28, 0.37, 0.19, 0.28]
}

# Data without benefits
data_sem_beneficios = {
    'Local': ['Brasil', 'Norte', 'RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'Nordeste', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'Sudeste', 'MG', 'ES', 'RJ', 'SP', 'Sul', 'PR', 'SC', 'RS', 'Centro-Oeste', 'MS', 'MT', 'GO', 'DF'],
    'Situação Atual 2023 (%)': [11.15, 16.72, 8.96, 25.4, 20.18, 14.11, 17.01, 15.27, 11.85, 23.29, 26.07, 22.91, 24.23, 18.57, 23.02, 22.82, 22.09, 21.63, 23.49, 5.72, 5.71, 6.53, 7.83, 4.87, 4.19, 5.07, 2.25, 4.57, 5.02, 5.42, 6.07, 4.28, 5.22],
    'Taxa de Redução Anual (%)': [-0.36, -0.02, -0.22, -0.44, -0.02, -0.63, 0.11, 0.19, -0.14, -0.68, -0.14, -0.46, -0.7, -0.62, -1.1, -0.96, -0.32, -0.69, -0.78, -0.32, -0.15, -0.14, -0.65, -0.3, -0.21, -0.28, -0.13, -0.2, -0.18, -0.12, -0.27, -0.13, -0.25],
    'Projeção 2030 (%)': [13.68, 16.85, 10.53, 28.51, 20.33, 18.53, 16.25, 13.93, 12.84, 28.04, 27.06, 26.1, 29.12, 22.91, 30.74, 29.51, 24.36, 26.46, 28.92, 7.97, 6.76, 7.5, 12.35, 6.95, 5.68, 7.05, 3.13, 5.98, 6.28, 6.28, 7.99, 5.18, 6.99],
    'Taxa Necessária Anual (%)': [1.59, 2.39, 1.28, 3.63, 2.88, 2.02, 2.43, 2.18, 1.69, 3.33, 3.72, 3.27, 3.46, 2.65, 3.29, 3.26, 3.16, 3.09, 3.36, 0.82, 0.82, 0.93, 1.12, 0.7, 0.6, 0.72, 0.32, 0.65, 0.72, 0.77, 0.87, 0.61, 0.75]
}

# Convert to DataFrames
df_com_beneficios = pd.DataFrame(data_com_beneficios)
df_sem_beneficios = pd.DataFrame(data_sem_beneficios)

# Page title
st.title('Resultados da Análise de Pobreza')

# Create tabs
tab1, tab2 = st.tabs(['Com Benefícios Sociais', 'Sem Benefícios Sociais'])

with tab1:
    st.subheader('Análise com Benefícios Sociais')
    st.dataframe(df_com_beneficios)
    
    # Download Excel file
    excel_com = get_excel_file_as_bytes("data/resultados_com_beneficios.xlsx")
    st.download_button(
        "Download dados (Excel)",
        excel_com,
        "resultados_com_beneficios.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key='download-excel-com'
    )
    
    # Visualization
    fig1 = px.bar(df_com_beneficios, 
                 x='Local', 
                 y=['Situação Atual 2023 (%)', 'Projeção 2030 (%)'],
                 title='Comparação: Situação Atual vs Projeção 2030 (Com Benefícios)',
                 barmode='group')
    st.plotly_chart(fig1)

with tab2:
    st.subheader('Análise sem Benefícios Sociais')
    st.dataframe(df_sem_beneficios)
    
    # Download Excel file
    excel_sem = get_excel_file_as_bytes("data/resultados_sem_beneficios.xlsx")
    st.download_button(
        "Download dados (Excel)",
        excel_sem,
        "resultados_sem_beneficios.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key='download-excel-sem'
    )
    
    # Visualization
    fig2 = px.bar(df_sem_beneficios, 
                 x='Local', 
                 y=['Situação Atual 2023 (%)', 'Projeção 2030 (%)'],
                 title='Comparação: Situação Atual vs Projeção 2030 (Sem Benefícios)',
                 barmode='group')
    st.plotly_chart(fig2)