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



# URL of the background image
background_image_url = "https://media.discordapp.net/attachments/1155327631361835119/1289648145713856684/Untitled_design_37.png?ex=66f995ee&is=66f8446e&hm=0dc366d98bee629ae4de11661932e734a89c5c7a783d1e55ec5fdd278efee563&=&format=webp&quality=lossless&width=1100&height=618"

# CSS for background image and navbar styling
st.markdown(f"""
    <style>
    /* Set background image for the entire body */
      .stApp {{
        background-image: url('{background_image_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }}""", unsafe_allow_html=True)


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