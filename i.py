import streamlit as st
from streamlit.components.v1 import components

st.set_page_config(
    page_title="RapidTV",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded",
    )

canal, info = st.tabs(["Canales", "Info"])
with canal:
    ancho = 750
    alto = ancho/1.77
    canales = {'Cinemax': 'https://latele-envivo.com/Embed/cinemax/',
                'History': 'https://latele-envivo.com/Embed/history/',
                'HBO': 'https://latele-envivo.com/Embed/hbo/',
                'Star': 'https://latele-envivo.com/Embed/star-channel/',
                'HBO+': 'https://latele-envivo.com/Embed/hbo-plus/',
                'Space': 'https://latele-envivo.com/Embed/space/',
                'Cinecanal': 'https://latele-envivo.com/Embed/cinecanal/',
                'TNT': 'https://latele-envivo.com/Embed/tnt/',
                'Warner TV': 'https://latele-envivo.com/Embed/warner/',
                'AXN': 'https://latele-envivo.com/Embed/axn/',
                'AMC': 'https://latele-envivo.com/Embed/amc/',
                'FX': 'https://latele-envivo.com/Embed/fx/',
                'Studio Universal': 'https://latele-envivo.com/Embed/studio-universal/',
                'Paramount': 'https://latele-envivo.com/Embed/paramount-channel/',
                'Cartoon Network': 'https://latele-envivo.com/Embed/cartoon-network/',
                'Discovery Kids': 'https://latele-envivo.com/Embed/discovery-kids/',
                'Disney Junior': 'https://latele-envivo.com/Embed/disney-junior/',
                'Disney Channel': 'https://latele-envivo.com/Embed/disney-channel/',
                'Nick': 'https://latele-envivo.com/Embed/nick/',
                'Nick Jr': 'https://latele-envivo.com/Embed/nickmusic/',
                'Tooncast': 'https://latele-envivo.com/Embed/tooncast/',
                'Discovery Channel': 'https://latele-envivo.com/Embed/discovery-channel/',
                'Discovery Turbo': 'https://latele-envivo.com/Embed/discovery-turbo/',
                'Discovery Science': 'https://latele-envivo.com/Embed/discovery-sciencie/',
                'Discovery H&H': 'https://latele-envivo.com/Embed/discovery-hh/',
                'Nat Geo': 'https://latele-envivo.com/Embed/national-geographic/',
                'A & E': 'https://latele-envivo.com/Embed/ae/',
                'Venus': 'https://latele-envivo.com/Embed/venus/',
                'ESPN': 'https://latele-envivo.com/Deportes/espn/',
                'ESPN2': 'https://latele-envivo.com/Deportes/espn2/',
                'ESPN3': 'https://latele-envivo.com/Deportes/espn3/',
                'ESPN Estra': 'https://latele-envivo.com/Deportes/espnextra/',
                'FOX Sports': 'https://latele-envivo.com/Deportes/fox-sports/',
                'DAZN Formula 1': 'https://latele-envivo.com/Deportes/formula1/'}
    lista, ver = st.columns([0.2, 0.8])
    with lista:
        seleccion = st.radio('Selecciona un canal', list(canales.keys()))
    with ver:
        src = canales[seleccion]
        st.components.v1.iframe(src, width=ancho, height=alto, scrolling=True)

with info:
    st.components.v1.iframe("https://latele-envivo.com/embeds/", width=900, height=700, scrolling=True)

