import streamlit as st  
import pandas as pd

st.title("APARTAMETNOS NA CIDADE DO RIO DE JANEIRO ??????")
rioAptos = pd.read_csv("https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv")

st.data_editor(rioAptos)

bairro_escolhido = st.multiselect("escolha um bairro:", rioAptos["bairro"].unique())

st.write(f"bairro escolhido {bairro_escolhido}")

rioAptos_bairro = rioAptos[rioAptos['bairro'].isin(bairro_escolhido) ]

st.data_editor(rioAptos_bairro)

menor_preco = rioAptos_bairro["preco"].min()
maior_preco = rioAptos_bairro["preco"].max()
st.write(menor_preco)
st.write(maior_preco)


if bairro_escolhido:
    valor = st.slider("faixa de $", menor_preco, maior_preco, (menor_preco,maior_preco))
    rioAptos_filtro_preco = rioAptos_bairro[rioAptos_bairro['preco'].between(valor[0], valor[1])]
    st.data_editor(rioAptos_filtro_preco)


