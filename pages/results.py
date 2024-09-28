import random
import streamlit as st
from streamlit_extras.let_it_rain import rain 

food_emojis = ["🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", 
               "🍒", "🍑", "🍍", "🥭", "🥥", "🥝", "🍅", "🥑", "🍆", "🥕", 
               "🌽", "🌶️", "🥔", "🥬", "🍞", "🥖", "🥯", "🥩", "🍗", "🍔", 
               "🍟", "🌭", "🍕", "🍣", "🍱", "🥗", "🍜", "🍲", "🍛", "🍥", 
               "🍦", "🍧", "🍨", "🍩", "🍪", "🎂", "🍰", "🧁", "🍭", "🍬"]

def show(ingredients):
    st.title("Results Page")
    st.write(", ".join(ingredients))
    rain(
        emoji=random.choice(food_emojis),
        font_size=54,
        falling_speed=5,
        animation_length=100,
    )
    if st.button("Go Back to Home"):
        st.session_state.page = "home"
    return []
