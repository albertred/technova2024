import streamlit as st
from pages import home, results
# Initialize session state for page
if 'page' not in st.session_state:
    st.session_state.page = 'home'
# Navigation logic
if st.session_state.page == 'home':
    home.show()
elif st.session_state.page == 'results':
    results.show()
