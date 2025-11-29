import pandas as pd
import plotly.express as px
import streamlit as st


# Configuração do layout
st.set_page_config(page_title='DASHCOVID', layout='wide')

# Título do dashboard
st.title('DASHCOVID - Um Painel de Informações sobre a COVID-19 - Ano 2020')

# Carregamento dos dados
df = pd.read_csv('WHO_time_series.csv')

# Conversão da data
df['Date_reported'] = pd.to_datetime(df['Date_reported'])

# --- GRÁFICO 1: LINHA GLOBAL ---

fig1 = px.line(
    df,
    x='Date_reported',
    y='Cumulative_cases',
    color='Country',
    title=''
)

fig1.update_layout(
    xaxis_title='Data',
    yaxis_title='Casos Acumulados',
)

st.plotly_chart(fig1, use_container_width=True)

# --- GRÁFICO 2: PIZZA BRASIL x EUA x ÍNDIA ---

# Filtrar apenas os 3 países
df_three = df[df['Country'].isin(['Brazil', 'United States of America', 'India'])]

# Pegar os valores do último dia disponível
df_last = df_three.sort_values('Date_reported').groupby('Country').tail(1)

fig2 = px.pie(
    df_last,
    names='Country',
    values='Cumulative_cases',
    title='Comparativo Total de Casos – Brasil x EUA x Índia'
)

st.plotly_chart(fig2, use_container_width=True)


