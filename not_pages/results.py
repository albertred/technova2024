import random
import streamlit as st
from streamlit_extras.let_it_rain import rain 
from recipe_recommender import gen_rec

image_folder_path = "/Users/shuyuliu/Downloads/archive(1)/FoodImages/FoodImages/"

# URL of the background image
background_image_url = "https://media.discordapp.net/attachments/1155327631361835119/1289648145713856684/Untitled_design_37.png?ex=66f995ee&is=66f8446e&hm=0dc366d98bee629ae4de11661932e734a89c5c7a783d1e55ec5fdd278efee563&=&format=webp&quality=lossless&width=1100&height=618"

def bg_image(background_image_url):
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
        "Title": "Recipe 1",
        "Image_Name": "https://c.pxhere.com/photos/78/b1/photo-1617970.jpg!d",
        "description": "A delicious pasta dish with rich tomato sauce and basil.",
        "Instructions": "Ingredients: Tomato, Basil, Pasta. Steps: 1. Boil pasta. 2. Cook tomato sauce. 3. Combine and serve."
    },
    {
        "id": 2,
        "Title": "Recipe 2",
        "Image_Name": "https://www.devourdinner.com/wp-content/uploads/2018/04/Teriyaki-Noodles_Devour-Dinner-101.jpg",
        "description": "Teriyaki noodles with vegetables and a savory sauce.",
        "Instructions": "Ingredients: Noodles, Teriyaki Sauce, Vegetables. Steps: 1. Cook noodles. 2. Stir-fry vegetables. 3. Add sauce and serve."
    },
    {
        "id": 3,
        "Title": "Recipe 3",
        "Image_Name": "https://www.foodandwine.com/thmb/IuZPWAXBp4YaT9hn1YLHhuijT3k=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/FAW-recipes-big-italian-salad-hero-83e6ea846722478f8feb1eea33158b00.jpg",
        "description": "A refreshing salad with greens and a light vinaigrette.",
        "Instructions": "Ingredients: Greens, Vinaigrette. Steps: 1. Chop greens. 2. Prepare vinaigrette. 3. Mix and serve."
    }
]


def show_recipe_details(recipe):

    st.image(image_folder_path + recipe["Image_Name"] + ".jpg", width=300)
    st.markdown(f"### {recipe['Title']}")
    #st.markdown(f"**Description:** {recipe['description']}")
    st.markdown(f"**Recipe:** {recipe['Instructions']}")
    if st.button("Go Back"):
        st.session_state.viewing_recipe = False
        st.rerun()

# recipes = get_recipe(["brown bread", "bananas", "peanut butter", "milk", "strawberries", "soda", "cherries"])

def show(ingredients):

    bg_image(background_image_url)

    if st.button("Home", key="gohome"):
        st.session_state.page = 'home'
        st.session_state.viewing_recipe = False
        st.rerun()

    st.title("Recipes")
    st.write("Check out some things you can make!")
    rain(
        emoji=random.choice(food_emojis),
        font_size=40,
        falling_speed=4,
        animation_length=1,
    )

    # Initially set `viewing_recipe` to False if it does not exist yet
    if 'viewing_recipe' not in st.session_state:
        st.session_state.viewing_recipe = False

    # Display recipe cards or selected recipe details based on `viewing_recipe`
    if not st.session_state.viewing_recipe:
        recipes = st.session_state.rec_list
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
                if st.button(f"View {recipe['Title']}", key=f"view_{recipe['id']}"):
                    st.session_state.selected_recipe = recipe
                    st.session_state.viewing_recipe = True  # Set the flag to True
                    st.rerun()
                st.image(image_folder_path + recipe["Image_Name"] + ".jpg", use_column_width=True)
                st.markdown(f"**{recipe['Title']}**")
                #st.markdown(f"{recipe['description']}")
    else:
        # Show the selected recipe details
        show_recipe_details(st.session_state.selected_recipe)
        #show_recipe_details(get_recipe(["brown bread", "bananas", "peanut butter", "milk", "strawberries", "soda", "cherries"]))
