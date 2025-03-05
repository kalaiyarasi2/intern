import streamlit as st
st.title("LOGIN")


col1,col2 = st.columns([1,2])
col1.title('Welcome to our page')

with st.form('user login'):
    a = st.text_input('Email')
    b = st.text_input('password')
    submit = st.form_submit_button('Submit')

if submit:
    st.write("Your login successfully")
    