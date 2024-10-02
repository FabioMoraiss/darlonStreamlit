import streamlit as st  
import pandas as pd

st.title("DIFERENÇA ENTRE HOMENS E MULHERES NO PAGAMENTO DE PENSÃO")
df = pd.read_csv("https://www.gov.br/receitafederal/dados/faixa-etaria-do-declarante-e-genero.csv/@@download/file/Faixa%20Et%C3%A1ria%20do%20Declarante%20e%20G%C3%AAnero.csv", delimiter=';')


st.write("base completa:")
st.data_editor(df)
st.write("apenas as colunas de interesse:")
st.write("nota* a coluna 'quantidade de declarantes' não é de interesse pois não há informações se um declarante é pagante de pensão ou não")
st.data_editor(df[['Ano-Calendário', 'Gênero', 'Faixa Etária', 'Deduções  com Pensão Alimentícia Total']])

st.write("pensão por ano em BILHÕES")

df['Deduções  com Pensão Alimentícia Total'] = df['Deduções  com Pensão Alimentícia Total'].str.replace(',', '.', regex=True)
df['Deduções  com Pensão Alimentícia Total'] = pd.to_numeric(df['Deduções  com Pensão Alimentícia Total'])

pensao_por_ano = df.groupby('Ano-Calendário')['Deduções  com Pensão Alimentícia Total'].sum()
st.data_editor(pensao_por_ano)
