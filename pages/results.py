import streamlit as st
from streamlit_extras.let_it_rain import rain 

def show():
    st.title("Results Page")
    st.write("This is the results page!")
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    if st.button("Go Back to Home"):
        st.session_state.page = "home"
