import streamlit as st
from pages import results, upload

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
