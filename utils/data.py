import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import geopandas as gpd
from scipy.stats import linregress
from io import BytesIO

# Dados atualizados
data_com_beneficio = {
    'Local': ['Brasil', 'Norte', 'RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'Nordeste', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'Sudeste', 'MG', 'ES', 'RJ', 'SP', 'Sul', 'PR', 'SC', 'RS', 'Centro-Oeste', 'MS', 'MT', 'GO', 'DF'],
    '2015': [5.63, 10.51, 4.67, 11.68, 11.72, 4.50, 12.01, 11.46, 6.57, 11.81, 17.42, 11.25, 12.11, 8.31, 9.16, 11.14, 14.27, 8.97, 10.96, 2.57, 3.12, 4.62, 2.95, 1.98, 1.70, 2.15, 1.07, 1.64, 2.30, 2.32, 2.60, 2.10, 2.39],
    '2016': [6.73, 11.86, 5.94, 15.90, 14.56, 6.05, 12.63, 11.08, 7.50, 13.72, 19.40, 13.92, 14.08, 9.76, 10.92, 12.85, 15.18, 12.33, 12.87, 3.42, 4.79, 4.99, 3.56, 2.60, 2.12, 2.25, 1.84, 2.16, 2.85, 1.90, 2.69, 3.70, 1.92],
    '2017': [7.28, 11.65, 5.29, 16.82, 15.12, 7.87, 13.71, 10.02, 5.78, 15.19, 20.37, 16.93, 13.89, 12.01, 11.50, 13.49, 16.87, 14.97, 15.65, 3.61, 4.06, 5.61, 4.11, 3.04, 2.54, 2.99, 1.59, 2.67, 3.31, 3.32, 3.15, 3.24, 3.67],
    '2018': [7.35, 12.31, 5.25, 16.33, 15.49, 9.40, 13.00, 10.70, 8.05, 15.35, 21.84, 16.26, 13.63, 11.60, 12.91, 13.03, 19.28, 15.37, 15.25, 3.58, 3.99, 4.47, 4.20, 3.09, 2.45, 3.08, 1.59, 2.36, 3.25, 3.36, 2.74, 3.41, 3.33],
    '2019': [7.35, 13.04, 5.20, 17.77, 16.82, 12.48, 13.71, 7.90, 8.87, 15.31, 22.50, 15.83, 13.48, 12.05, 14.28, 14.31, 16.53, 13.97, 14.55, 3.51, 4.34, 3.89, 4.49, 2.72, 2.43, 2.83, 1.73, 2.46, 3.31, 2.79, 2.84, 3.66, 1.79],
    '2020': [6.04, 9.14, 5.23, 10.45, 13.22, 10.39, 8.27, 10.54, 5.92, 10.92, 15.10, 9.86, 9.86, 6.30, 9.78, 12.44, 12.24, 8.42, 10.34, 3.87, 3.39, 4.42, 5.76, 3.33, 2.92, 3.91, 1.98, 2.52, 3.05, 2.63, 2.98, 3.33, 2.87],
    '2021': [8.99, 13.95, 4.29, 14.03, 10.54, 7.75, 15.28, 7.94, 4.93, 17.62, 12.22, 8.05, 9.39, 6.32, 11.12, 11.70, 13.07, 8.08, 8.80, 3.32, 2.18, 2.66, 3.61, 2.21, 1.67, 2.23, 1.41, 1.28, 1.82, 1.98, 2.60, 1.32, 1.94],
    '2022': [5.87, 8.00, 4.29, 14.03, 10.54, 7.75, 7.54, 7.94, 4.93, 11.82, 12.22, 8.05, 10.95, 6.32, 11.12, 11.70, 13.07, 8.08, 8.80, 3.32, 2.18, 2.66, 3.61, 2.21, 1.67, 2.23, 1.41, 1.28, 1.82, 1.98, 2.60, 1.32, 1.94],
    '2023': [4.40, 5.97, 4.38, 13.24, 6.63, 7.20, 5.72, 3.60, 4.24, 9.08, 12.22, 8.05, 9.39, 6.32, 7.37, 9.31, 8.81, 8.08, 8.80, 2.50, 2.18, 2.66, 3.61, 2.21, 1.67, 2.23, 1.41, 1.28, 1.82, 1.98, 2.60, 1.32, 1.94]
}

data_sem_beneficio = {
    'Local': ['Brasil', 'Norte', 'RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO', 'Nordeste', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'Sudeste', 'MG', 'ES', 'RJ', 'SP', 'Sul', 'PR', 'SC', 'RS', 'Centro-Oeste', 'MS', 'MT', 'GO', 'DF'],
    '2015': [8.52, 16.08, 7.20, 18.87, 19.03, 9.89, 17.83, 15.41, 9.86, 17.95, 24.76, 17.48, 18.61, 13.36, 15.48, 16.89, 21.04, 14.60, 16.67, 3.68, 5.07, 5.98, 3.85, 2.77, 2.62, 3.23, 1.41, 2.75, 4.01, 4.83, 4.30, 3.91, 3.16],
    '2016': [9.68, 18.08, 9.67, 22.96, 21.52, 10.67, 19.30, 19.49, 11.13, 19.83, 26.71, 21.87, 20.57, 14.38, 17.77, 17.62, 20.99, 17.63, 18.97, 4.57, 6.77, 6.74, 4.55, 3.37, 3.21, 3.48, 2.20, 3.57, 4.34, 4.32, 4.01, 5.04, 3.12],
    '2017': [10.21, 17.41, 7.10, 24.01, 21.45, 11.03, 18.79, 17.86, 9.47, 21.23, 27.94, 23.20, 19.75, 17.20, 17.65, 18.78, 23.76, 19.70, 21.66, 4.83, 6.07, 7.44, 4.99, 3.97, 3.57, 4.34, 2.09, 3.72, 4.94, 5.72, 4.68, 4.75, 4.94],
    '2018': [10.35, 18.24, 7.62, 20.79, 21.97, 13.39, 20.13, 17.23, 11.08, 21.11, 27.68, 22.51, 19.20, 17.05, 19.12, 18.18, 25.55, 20.97, 21.24, 5.19, 6.21, 6.34, 5.58, 4.48, 3.34, 3.93, 2.13, 3.51, 4.72, 5.37, 4.66, 4.83, 3.98],
    '2019': [10.17, 18.48, 6.96, 23.96, 22.61, 16.13, 20.04, 14.60, 12.28, 21.16, 28.02, 22.99, 19.23, 17.65, 20.82, 19.34, 22.37, 20.12, 20.67, 4.73, 6.09, 5.86, 5.66, 3.65, 3.35, 4.10, 2.11, 3.39, 4.49, 4.57, 4.39, 5.10, 3.09],
    '2020': [13.45, 20.45, 10.14, 25.99, 26.95, 21.48, 19.86, 21.95, 14.48, 25.96, 30.39, 25.72, 24.74, 20.04, 27.54, 25.76, 27.96, 22.73, 25.81, 7.83, 8.57, 8.64, 10.58, 6.38, 5.45, 6.82, 3.10, 5.57, 7.23, 7.12, 6.65, 8.14, 5.86],
    '2021': [12.82, 20.16, 12.33, 24.48, 23.36, 16.26, 22.12, 15.68, 11.47, 25.24, 30.50, 24.33, 24.23, 20.05, 25.66, 26.21, 25.85, 23.70, 24.16, 7.42, 8.26, 9.66, 9.58, 6.02, 4.42, 5.59, 2.99, 4.16, 6.03, 6.43, 5.75, 6.14, 5.98],
    '2022': [10.63, 15.02, 7.49, 21.09, 17.49, 11.50, 16.08, 15.72, 8.85, 22.00, 25.19, 21.91, 22.22, 16.93, 21.63, 21.35, 23.88, 18.80, 22.19, 5.68, 6.66, 6.53, 7.44, 4.51, 4.09, 4.90, 2.66, 4.19, 5.02, 4.92, 5.75, 5.09, 4.10],
    '2023': [11.15, 16.72, 8.96, 25.40, 20.18, 14.11, 17.01, 15.27, 11.85, 23.29, 26.07, 22.91, 24.23, 18.57, 23.02, 22.82, 22.09, 21.63, 23.49, 5.72, 5.71, 6.53, 7.83, 4.87, 4.19, 5.07, 2.25, 4.57, 5.02, 5.42, 6.07, 4.28, 5.22]
}

# Converter os dados para DataFrames para facilitar a manipulação
df_com_beneficio = pd.DataFrame(data_com_beneficio)
df_sem_beneficio = pd.DataFrame(data_sem_beneficio)

# Definir regiões e seus estados
regions = {
    'Norte': ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO'],
    'Nordeste': ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA'],
    'Centro-Oeste': ['MS', 'MT', 'GO', 'DF'],
    'Sudeste': ['MG', 'ES', 'RJ', 'SP'],
    'Sul': ['PR', 'SC', 'RS']
}

# Função para salvar figura em bytes
def save_fig_to_bytes(fig):
    """Convert matplotlib figure to bytes for download"""
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=300)
    buf.seek(0)
    return buf

# Funções de plotagem e análise
def plot_national_comparison(with_benefits=True):
    df = df_com_beneficio if with_benefits else df_sem_beneficio
    years = [int(col) for col in df.columns if col != 'Local']
    regions_to_plot = ['Brasil', 'Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    
    fig, ax = plt.subplots(figsize=(12, 7))
    x_smooth = np.linspace(min(years), max(years), 200)
    
    colors = {'Brasil': 'black', 'Norte': 'green', 'Nordeste': 'red', 
              'Centro-Oeste': 'orange', 'Sudeste': 'blue', 'Sul': 'purple'}
    
    for region in regions_to_plot:
        data = df[df['Local'] == region].iloc[:, 1:].values.flatten()
        cs = CubicSpline(years, data)
        ax.plot(x_smooth, cs(x_smooth), label=region, color=colors[region], linewidth=2)
        ax.scatter(years, data, color=colors[region], s=50)

    ax.set_title(f"Comparação Nacional e Regional ({('Com' if with_benefits else 'Sem')} Benefícios)")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Percentual de Pobreza Extrema (%)")
    ax.grid(True)
    ax.legend()
    
    return fig

def plot_region_comparison(region_name, with_benefits=True):
    df = df_com_beneficio if with_benefits else df_sem_beneficio
    years = [int(col) for col in df.columns if col != 'Local']
    x_smooth = np.linspace(min(years), max(years), 200)
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Plot estados
    for state in regions[region_name]:
        data = df[df['Local'] == state].iloc[:, 1:].values.flatten()
        cs = CubicSpline(years, data)
        ax.plot(x_smooth, cs(x_smooth), alpha=0.3)
        ax.scatter(years, data, label=state, s=30)
    
    # Plot nacional e regional
    for name, color in [("Brasil", "blue"), (region_name, "red")]:
        data = df[df['Local'] == name].iloc[:, 1:].values.flatten()
        cs = CubicSpline(years, data)
        ax.plot(x_smooth, cs(x_smooth), label=name, color=color, linewidth=2)
        ax.scatter(years, data, color=color, s=50)

    ax.set_title(f"Região {region_name} ({('Com' if with_benefits else 'Sem')} Benefícios)")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Percentual de Pobreza Extrema (%)")
    ax.grid(True)
    ax.legend()
    
    return fig

def create_poverty_map(year, with_benefits=True):
    df = df_com_beneficio if with_benefits else df_sem_beneficio
    
    # Carregar shapefile
    states = gpd.read_file('data/BR_UF_2022/BR_UF_2022.shp')
    
    # Preparar dados para o mapa
    state_values = df[df['Local'].isin(sum(regions.values(), []))][['Local', str(year)]].set_index('Local').to_dict()[str(year)]
    
    states['poverty'] = states['SIGLA_UF'].map(state_values)
    
    fig, ax = plt.subplots(figsize=(15, 10))
    states.plot(column='poverty',
               ax=ax,
               legend=True,
               vmin=0,
               vmax=25,
               legend_kwds={
                   'label': '% População em\nPobreza Extrema',
                   'orientation': 'vertical',
                   'shrink': 0.8
               },
               cmap='YlOrRd',
               missing_kwds={'color': 'lightgrey'})
    ax.axis('off')
    ax.set_title(f'Pobreza Extrema por Estado - {year}\n({("Com" if with_benefits else "Sem")} Benefícios)')

    return fig

def calculate_projection(local_type, name=None, with_benefits=True):
    df = df_com_beneficio if with_benefits else df_sem_beneficio
    years = np.array([int(col) for col in df.columns if col != 'Local'])
    
    if local_type == "Nacional":
        data = df[df['Local'] == 'Brasil'].iloc[:, 1:].values.flatten()
    elif local_type == "Regional":
        data = df[df['Local'] == name].iloc[:, 1:].values.flatten()
    else:  # Estadual
        data = df[df['Local'] == name].iloc[:, 1:].values.flatten()
    
    slope, intercept, _, _, _ = linregress(years, data)
    
    current_rate = data[-1]  # Taxa atual (2023)
    observed_reduction = -slope  # Taxa de redução anual observada (mantém sinal negativo para crescimento)
    years_until_2030 = 2030 - 2023
    projection_2030 = max(0, current_rate + (slope * years_until_2030))  # Projeção a partir da taxa atual
    required_reduction = current_rate / years_until_2030  # Taxa necessária para zerar até 2030
    
    return {
        "current_rate": current_rate,
        "observed_reduction": observed_reduction,
        "required_reduction": required_reduction,
        "projection_2030": projection_2030
    }