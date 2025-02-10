import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px


label_encoder_city_of_birth=load(open("./le_city_of_birth.sav", "rb"))
label_encoder_country_of_birth=load(open("./le_country_of_birth.sav", "rb"))
label_encoder_competition_id=load(open("./le_competition_id.sav", "rb"))
label_encoder_club_name=load(open("./le_club_name.sav", "rb"))
label_encoder_foot=load(open("./le_foot", "rb"))
label_encoder_sub_position=load(open("./le_sub_position.sav", "rb"))
label_encoder_position=load(open("./le_position.sav", "rb"))


@st.cache(persist=True)
def load_data():
    df = pd.read_csv("your_data.csv")
    return df

# Solo se ejecutará una vez si ya está en caché
data = load_data()
st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
st.title('Prediccin de el valor de mercado de un jugador de fútbol')
st.markdown("<description> Descripcion a gusto </description>", unsafe_allow_html=True)
# Agregar un título a la barra lateral
st.sidebar.title('Selecciona los parámetros para analizar la predicción de el valor de mercado de un futbolista')

# Agregar otros elementos a la barra lateral según sea necesario
# Por ejemplo, un control deslizante:
matches_played = st.sidebar.slider('matches_played', 0, 100, 25)
yellow_cards = st.sidebar.slider('yellow_cards', 0, 100, 25)
red_cards = st.sidebar.slider('red_cards', 0, 100, 25)
goals = st.sidebar.slider('goals', 0, 100, 25)
assists = st.sidebar.slider('assists', 0, 100, 25)
minutes_played = st.sidebar.slider('minutes_played', 0, 100, 25)
age = st.sidebar.slider('age', 0, 100, 25)
height_in_cm = st.sidebar.slider('height_in_cm', 0, 100, 25)
highest_market_value_in_eur = st.sidebar.slider('highest_market_value_in_eur', 0, 100, 25)
competition_id_le = st.selectbox('Select a competition', data['competition_id_le'])
club_name_le = st.selectbox('Select a club name', data['club_name_le'])
foot_le = st.selectbox('Select a foot', data['foot_le'])
position_le = st.selectbox('Select a position', data['position_le'])
sub_position_le	 = st.selectbox('Select a sub position', data['sub_position_le'])
country_of_birth_le = st.selectbox('Select a country of birth', data['country_of_birth_le'])
city_of_birth_le= st.selectbox('Select a city of birth', data['city_of_birth_le'])
# Contenido principal
st.write(f'La matches_played seleccionada es {matches_played}')
st.write(f'La yellow_cards seleccionada es {yellow_cards}')
st.write(f'La red_cards seleccionada es {red_cards}')
st.write(f'La goals seleccionada es {goals}')
st.write(f'La assists seleccionada es {assists}')
st.write(f'La minutes_played seleccionada es {minutes_played}')
st.write(f'La age seleccionada es {age}')
st.write(f'La height_in_cm seleccionada es {height_in_cm}')
st.write(f'La highest_market_value_in_eur seleccionada es {highest_market_value_in_eur}')
st.write(f'La competition_id_le seleccionada es {competition_id_le}')
st.write(f'La club_name_le seleccionada es {club_name_le}')
st.write(f'La foot_le seleccionada es {foot_le}')
st.write(f'La position_le seleccionada es {position_le}')
st.write(f'La sub_position_le seleccionada es {sub_position_le}')
st.write(f'La country_of_birth_le seleccionada es {country_of_birth_le}')
st.write(f'La city_of_birth_le seleccionada es {city_of_birth_le}')