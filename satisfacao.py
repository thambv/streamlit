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

nivel_satisfacao = st.select_slider(
    'Qual é o seu nível de satisfação?',  # Texto para o usuário
    options=range(0, 101, 10),  # Opções de 0 a 100 com intervalo de 10
    value=50  # Valor inicial (por exemplo, 50%)
)
