import random, app
import streamlit as st
from streamlit_extras.let_it_rain import rain 


# URL of the background image
background_image_url = "https://media.discordapp.net/attachments/1155327631361835119/1289648145713856684/Untitled_design_37.png?ex=66f995ee&is=66f8446e&hm=0dc366d98bee629ae4de11661932e734a89c5c7a783d1e55ec5fdd278efee563&=&format=webp&quality=lossless&width=1100&height=618"

# CSS for background image and navbar styling
app.bg_img(background_image_url)

# Styling the navigation bar
st.markdown("""
    <style>
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
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar HTML
st.markdown("""
    <div class="navbar">
        <a href='/home'>Home</a>
        <a href='/app'>Take Photo</a>
        <a href='/results'>Recipes</a>
    </div>
""", unsafe_allow_html=True)

# Food emojis for the rain effect
food_emojis = ["🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", 
               "🍒", "🍑", "🍍", "🥭", "🥥", "🥝", "🍅", "🥑", "🍆", "🥕", 
               "🌽", "🌶️", "🥔", "🥬", "🍞", "🥖", "🥯", "🥩", "🍗", "🍔", 
               "🍟", "🌭", "🍕", "🍣", "🍱", "🥗", "🍜", "🍲", "🍛", "🍥", 
               "🍦", "🍧", "🍨", "🍩", "🍪", "🎂", "🍰", "🧁", "🍭", "🍬"]

# Example array of recipes
recipes = [
    {
        "id": 1,
        "title": "Recipe 1",
        "image": "https://c.pxhere.com/photos/78/b1/photo-1617970.jpg!d",
        "description": "A delicious pasta dish with rich tomato sauce and basil.",
        "full_recipe": "Ingredients: Tomato, Basil, Pasta. Steps: 1. Boil pasta. 2. Cook tomato sauce. 3. Combine and serve."
    },
    {
        "id": 2,
        "title": "Recipe 2",
        "image": "https://www.devourdinner.com/wp-content/uploads/2018/04/Teriyaki-Noodles_Devour-Dinner-101.jpg",
        "description": "Teriyaki noodles with vegetables and a savory sauce.",
        "full_recipe": "Ingredients: Noodles, Teriyaki Sauce, Vegetables. Steps: 1. Cook noodles. 2. Stir-fry vegetables. 3. Add sauce and serve."
    },
    {
        "id": 3,
        "title": "Recipe 3",
        "image": "https://www.foodandwine.com/thmb/IuZPWAXBp4YaT9hn1YLHhuijT3k=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/FAW-recipes-big-italian-salad-hero-83e6ea846722478f8feb1eea33158b00.jpg",
        "description": "A refreshing salad with greens and a light vinaigrette.",
        "full_recipe": "Ingredients: Greens, Vinaigrette. Steps: 1. Chop greens. 2. Prepare vinaigrette. 3. Mix and serve."
    }
]

def show_recipe_details(recipe):
    st.image(recipe["image"], width=300)
    st.markdown(f"### {recipe['title']}")
    st.markdown(f"**Description:** {recipe['description']}")
    st.markdown(f"**Recipe:** {recipe['full_recipe']}")
    if st.button("Go Back"):
        st.session_state.viewing_recipe = False

def show(ingredients):
    st.title("Recipes")
    st.write("Check out some things you can make!")
    st.write(", ".join(ingredients))  # Temporary ingredient display
    rain(
        emoji=random.choice(food_emojis),
        font_size=54,
        falling_speed=5,
        animation_length=100,
    )

    # Initially set `viewing_recipe` to False if it does not exist yet
    if 'viewing_recipe' not in st.session_state:
        st.session_state.viewing_recipe = False

    # Display recipe cards or selected recipe details based on `viewing_recipe`
    if not st.session_state.viewing_recipe:
        st.markdown("""
        <style>
        .recipe-card {
            background-color: #e0f2e0;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }
        .recipe-card img {
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

        # Display recipe cards in a grid layout
        col1, col2, col3 = st.columns(3)  # Create 3 columns for layout
        columns = [col1, col2, col3]

        for i, recipe in enumerate(recipes):
            with columns[i % 3]:
                if st.button(f"View {recipe['title']}", key=f"view_{recipe['id']}"):
                    st.session_state.selected_recipe = recipe
                    st.session_state.viewing_recipe = True  # Set the flag to True
                st.image(recipe["image"], use_column_width=True)
                st.markdown(f"**{recipe['title']}**")
                st.markdown(f"{recipe['description']}")
    else:
        # Show the selected recipe details
        show_recipe_details(st.session_state.selected_recipe)
