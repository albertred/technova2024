import streamlit as st

def show():
    st.title("Home Page")
    st.write("Welcome to the Home Page")
    if st.button("Go to Results"):
        st.session_state.page = "results"
