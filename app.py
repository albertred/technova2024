import streamlit as st
import streamlit as st
from pages import results, upload

from propelauth import auth

user = auth.get_user()
if user is None:
    st.error('Please Login')
    st.stop()

with st.sidebar:
    st.link_button('Account', auth.get_account_url(), use_container_width=True)

st.text("Logged in as " + user.email + " with user ID " + user.user_id)

with st.sidebar:
    if st.button("Logout"):
        auth.logout()
        st.markdown(
            """
        <meta http-equiv="refresh" content="0; URL='/api/auth/logout'" /> 
            """,
            unsafe_allow_html=True,
        )


# Initialize session state for page
if 'page' not in st.session_state:
    st.session_state.page = 'home'
# Navigation logic
if st.session_state.page == 'home':
    ingredients = upload.upload()
    with open("ingredients.txt", "w") as file:
        for item in ingredients:
            file.write(f"{item}\n")
elif st.session_state.page == 'results':
    with open("ingredients.txt", "r") as file:
        ingredients = [line.strip() for line in file.readlines()]  # Remove newline characters
    results.show(ingredients)