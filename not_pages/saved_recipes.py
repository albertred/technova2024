import streamlit as st
import pymongo


image_folder_path = "/Users/shuyuliu/Downloads/archive(1)/FoodImages/FoodImages/"

client = pymongo.MongoClient("mongodb+srv://michellelu187:ItGErHWxYlRgflWx@cluster0.xg18n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tls=true&tlsAllowInvalidCertificates=true")
db = client.recipe_db
collection = db.recipes

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

def delete_recipe(user_email, recipe_title):
    # Update the user's saved recipes in the database by removing the specified recipe
    collection.update_one(
        {"email": user_email},
        {"$pull": {"recipes": {"Title": recipe_title}}}
    )
    st.rerun()
    
def show_recipe_details(recipe, user_email):
    st.image(image_folder_path + recipe["Image_Name"] + ".jpg", width=300)

    # Create two columns for the title and save button alignment
    col1, col2, col3 = st.columns([4, 2, 1])  # Adjust the ratio to make the title larger than the button

    # Display the recipe title in the first column
    with col1:
        st.markdown(f"### {recipe['Title']}")


    #st.markdown(f"**Description:** {recipe['description']}")
    st.markdown(f"**Recipe:** {recipe['Instructions']}")
    
    if st.button("Go Back"):
        st.session_state.viewing_recipe = False
        st.rerun()

# recipes = get_recipe(["brown bread", "bananas", "peanut butter", "milk", "strawberries", "soda", "cherries"])

def show(user_email):
    if st.button("Home", key="gohome"):
        st.session_state.page = 'home'
        st.session_state.viewing_recipe = False
        st.rerun()
        
	        
    st.title("Saved Recipes")

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

        saved_recipes = collection.find_one({"email": user_email})

        if saved_recipes and "recipes" in saved_recipes:
            # Loop through the saved recipes and display them in a grid
            for i, recipe in enumerate(saved_recipes["recipes"]):
                with columns[i % 3]:
                    if st.button(f"View {recipe['Title']}", key=f"view_{recipe['id']}"):
                        st.session_state.selected_recipe = recipe
                        st.session_state.viewing_recipe = True  # Set the flag to True
                        st.rerun()

                    st.image(image_folder_path + recipe["Image_Name"] + ".jpg", use_column_width=True)
                    st.markdown(f"**{recipe['Title']}**")
                    st.markdown(f"{recipe.get('Description', 'No Description')}")
        else:
            st.write("No saved recipes found.")
          
    else:
        # Show the selected recipe details
        show_recipe_details(st.session_state.selected_recipe, user_email)
