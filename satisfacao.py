import streamlit as st

st.write('Vamos aprender streamlit juntos!')
st.title('Nível de Satisfação do Cliente')

st.slider('Qual é o seu nível de satisfação?',  min_value=0, max_value=100)

