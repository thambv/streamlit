import streamlit as st
import plotly.express as px
import pandas as pd

st.write('Vamos aprender streamlit juntos!')
st.title('Nível de Satisfação do Cliente')
st.header('Este é o subtítulo')
st.subheader('Este é o terceiro subtítulo')
st.markdown('Este é o texto')
st.caption('Esta é a legenda')
st.code('x=2021')
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.slider('Qual é o seu nível de satisfação?',  min_value=0, max_value=100)

