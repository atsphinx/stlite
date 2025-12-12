import streamlit as st

name = st.text_input("Your name?")
st.write("Hello,", name or "world", "!")

value = st.slider("Value?")
st.write("The slider value is", value)
