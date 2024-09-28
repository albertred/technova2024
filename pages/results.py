import streamlit as st

def show():
    st.title("Results Page")
    st.write("This is the results page!")
    if st.button("Go Back to Home"):
        st.session_state.page = "home"
