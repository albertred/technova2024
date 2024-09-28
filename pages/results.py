import random
import streamlit as st
from streamlit_extras.let_it_rain import rain 


# nav bar

st.markdown("""
    <style>
            
            
    
    /* Styling the navigation bar */
    .navbar {
        position: sticky;
        top: 0;
        display: flex;
        justify-content: center;
        padding: 15px;
        z-index: 1000; /* Ensure it's on top of everything else */
    }
    .navbar a {
        color: white;
        text-decoration: none;
        font-size: 18px;
        padding: 10px 20px;
        margin: 0 10px;
    }
    .navbar a:hover {
        background-color: #f4a261;
        border-radius: 5px;
    }""", unsafe_allow_html=True)


# Navigation bar HTML
st.markdown("""
    <div class="navbar">
        <a href='/home'>Home</a>
        <a href='/results'>Results</a>
        <a href='/recipes'>Recipes</a>
    </div>
""", unsafe_allow_html=True)
    
            

food_emojis = ["🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", 
               "🍒", "🍑", "🍍", "🥭", "🥥", "🥝", "🍅", "🥑", "🍆", "🥕", 
               "🌽", "🌶️", "🥔", "🥬", "🍞", "🥖", "🥯", "🥩", "🍗", "🍔", 
               "🍟", "🌭", "🍕", "🍣", "🍱", "🥗", "🍜", "🍲", "🍛", "🍥", 
               "🍦", "🍧", "🍨", "🍩", "🍪", "🎂", "🍰", "🧁", "🍭", "🍬"]

def show():
    st.title("Recipes")
    st.write("Check out some things you can make!")
    rain(
        emoji=random.choice(food_emojis),
        font_size=54,
        falling_speed=5,
        animation_length=100,
    )
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #d3f0d3;
        padding: 20px;
        border-radius: 10px;
    }
    .recipe-card {
        background-color: #e0f2e0;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .recipe-card img {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.button("Monday")

    # Main content layout
    col1, col2 = st.columns([1, 3])  # Create two columns for layout

    # Left column for the recipe categories (represents the sidebar structure)
    with col1:
        st.header("Categories")
        st.button("Recipe 1")
        st.button("Recipe 2")
        st.button("Recipe 3")

    # Right column for recipe details
    with col2:
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        
        st.image("https://c.pxhere.com/photos/78/b1/photo-1617970.jpg!d", width=300, caption="Recipe 1")
        st.markdown("<p><strong>Recipe 1</strong></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # You can replicate this layout for other recipe cards
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.image("https://www.devourdinner.com/wp-content/uploads/2018/04/Teriyaki-Noodles_Devour-Dinner-101.jpg", width=300, caption="Recipe 2")
        st.markdown("<p><strong>Recipe 2</strong></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.sidebar.title("results")
    if st.button("Go Back to Home"):
        st.session_state.page = "home"