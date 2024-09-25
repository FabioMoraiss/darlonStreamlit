import streamlit as st  
import pandas as pd

st.title("CD/TEC")
st.write("ola amiguinho, vamos brincar ?")
animes = ["hedo of healer", "shikanokonoko", "anime do slime", "oshi no ko"]


anime_predileto = st.selectbox("anime predileto:", animes)
st.write(f"seu filme predileto é{anime_predileto}")

bandas = ["linkin park", "imagine dragons", "deco*27"]

bandas_prediletas = st.multiselect("bandas prediletas: ", bandas)
st.write(f"bandas escolhidas: {bandas_prediletas}")


genero_musicais = ["rock", "metal", "EDM", "qualquer coisa"]

bandas = {
    "rock": ["linkin park", "addc", "kiss"],
    "metal": ["metalica","megadeth", "slayer"],
    "EDM": ["reol", "deco*27", "shiguri UI"],
    "qualquer coisa": ["banda 1", "banda 2", "banda 3"]
}

genero_musical = st.selectbox("escolha seu genero: ", bandas.keys())

banda_predileta = st.selectbox("escolha sua banda predileta: ", bandas[genero_musical])

