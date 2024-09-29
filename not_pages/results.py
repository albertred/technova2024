import random
import streamlit as st
from streamlit_extras.let_it_rain import rain 
from recipe_recommender import gen_rec
import pymongo

image_folder_path = "/Users/michellelu/Documents/archive1/FoodImages/FoodImages/"

# URL of the background image
background_image_url = "https://media.discordapp.net/attachments/1155327631361835119/1289648145713856684/Untitled_design_37.png?ex=66f995ee&is=66f8446e&hm=0dc366d98bee629ae4de11661932e734a89c5c7a783d1e55ec5fdd278efee563&=&format=webp&quality=lossless&width=1100&height=618"

client = pymongo.MongoClient("mongodb+srv://michellelu187:ItGErHWxYlRgflWx@cluster0.xg18n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tls=true&tlsAllowInvalidCertificates=true")
db = client.recipe_db
collection = db.recipes

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

# def save_recipe(user_email, recipe):
#     # Extract relevant recipe data for storage
#     recipe_data = {
#         "id": recipe["id"],
#         "Title": recipe["Title"],
#         "Image_Name": recipe["Image_Name"],
#         "Description": recipe.get("description", ""),  # Optional field, defaults to empty string
#         "Instructions": recipe["Instructions"]
#     }
    
#     # Check if the user already exists in the database
#     user = collection.find_one({"email": user_email})
    
#     if user:
#         # If the user exists, append the new recipe to their list of saved recipes
#         collection.update_one({"email": user_email}, {"$push": {"recipes": recipe_data}})
#     else:
#         # If the user doesn't exist, create a new document with the email and recipe
#         collection.insert_one({"email": user_email, "recipes": [recipe_data]})
        
def save_recipe(user_email, recipe):
    # Extract relevant recipe data for storage
    recipe_data = {
        "id": recipe["id"],
        "Title": recipe["Title"],
        "Image_Name": recipe["Image_Name"],
        "Description": recipe.get("description", ""),  # Optional field, defaults to empty string
        "Instructions": recipe["Instructions"]
    }
    
    # Check if the user already exists in the database
    user = collection.find_one({"email": user_email})
    
    if user:
        # Check if the recipe is already in the user's saved recipes by title
        saved_recipes = user.get("recipes", [])
        recipe_titles = [r["id"] for r in saved_recipes]
        
        if recipe_data["id"] in recipe_titles:
            st.warning("Recipe is already saved!")
        else:
            # If the recipe is not already saved, append it to their saved recipes
            collection.update_one({"email": user_email}, {"$push": {"recipes": recipe_data}})
            st.success("Recipe saved successfully!")
    else:
        # If the user doesn't exist, create a new document with the email and recipe
        collection.insert_one({"email": user_email, "recipes": [recipe_data]})
        st.success("Recipe saved successfully!")


def show_recipe_details(recipe, user_email):
    st.image(image_folder_path + recipe["Image_Name"] + ".jpg", width=300)

    # Create two columns for the title and save button alignment
    col1, col2, col3 = st.columns([4, 2, 1])  # Adjust the ratio to make the title larger than the button

    # Display the recipe title in the first column
    with col1:
        st.markdown(f"### {recipe['Title']}")

    # Display the save button in the second column (right-aligned)
    with col2:
        saved = False
        if st.button("Save Recipe"):
            # Logic to save the recipe for the user (save to database or session state)
            saved = True
            save_recipe(user_email, recipe)


    #st.markdown(f"**Description:** {recipe['description']}")
    st.markdown(f"**Recipe:** {recipe['Instructions']}")
    if st.button("Go Back"):
        st.session_state.viewing_recipe = False
        st.rerun()

# recipes = get_recipe(["brown bread", "bananas", "peanut butter", "milk", "strawberries", "soda", "cherries"])

def show(user_email):

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
        show_recipe_details(st.session_state.selected_recipe, user_email)
        #show_recipe_details(get_recipe(["brown bread", "bananas", "peanut butter", "milk", "strawberries", "soda", "cherries"]))
