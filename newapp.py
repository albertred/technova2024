
from pages import results, home
import streamlit as st
import cv2
import numpy as np
import torch
from recipe_recommender import gen_rec

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



def upload():

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

    # Initialize ingredients and new_ingredient in session state if not already there
    if 'ingredients' not in st.session_state:
        st.session_state.ingredients = []
    if 'new_ingredients' not in st.session_state:
        st.session_state.new_ingredients = []  # Initialize a list for new ingredients

    if 'rec_list' not in st.session_state:
        st.session_state.rec_list = []

    ingredients = st.session_state.ingredients  # Use session state for ingredients list
    
    def get_recipe(ingredients):
        arr = [
            {**row, 'id': index}
            for index, row in (gen_rec(ingredients)).iterrows()
        ]
        return arr

    def detect_food(image):
        model = torch.hub.load('yolov5', 'yolov5s', source='local')  # Update with your local path
        results = model(image)
        return results

    def visualize_detections(image, results):
        df = results.pandas().xyxy[0]
        detected_items = []
        for _, row in df.iterrows():
            if row['confidence'] > 0.5:
                xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                label = row['name']
                confidence = row['confidence']
                detected_items.append((label, confidence))
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
                cv2.putText(image, f'{label}: {confidence:.2f}', (xmin, ymin - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        return image, detected_items
    
    st.title("Food Detection App")
    uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        num_detected = 0  # Initialize number of detected items

        for index, uploaded_file in enumerate(uploaded_files):
            image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            st.image(image_rgb, caption=uploaded_file.name, use_column_width=True)
            uploaded_files[index].name = uploaded_files[index].name + "_" + str(index)

            results = detect_food(image)
            result_image, detected_items = visualize_detections(image_rgb.copy(), results)

            if detected_items:
                st.image(result_image, caption='Detected Food Items', use_column_width=True)
                st.write("Edit detected ingredients:")

                for item in detected_items:
                    label, confidence = item
                    num_detected += 1  # Increment the detected item count, used as the index

                    # If the current number of detected ingredients exceeds the list length, append placeholders
                    if num_detected > len(ingredients):
                        ingredients.append(label)

                    # Show a text input for each detected ingredient, allowing the user to edit the label
                    edited_name = st.text_input(f"Ingredient {num_detected} (Confidence: {confidence:.2f})", 
                                                value=ingredients[num_detected - 1], key=f"ingredient_{num_detected}")

                    # Update the corresponding ingredient at the correct index (num_detected - 1)
                    ingredients[num_detected - 1] = edited_name

            else:
                st.write("No food items detected.")

        # Add a button to create new ingredient input fields
        if 'new_ingredient_fields' not in st.session_state:
            st.session_state.new_ingredient_fields = 1  # Start with one additional input field

        # Show all current input fields for new ingredients
        for i in range(st.session_state.new_ingredient_fields):
            # Check if the new ingredients list has enough entries; if not, add placeholders
            if i >= len(st.session_state.new_ingredients):
                st.session_state.new_ingredients.append("")  # Placeholder for the new ingredient

            # Display the input field for editing new ingredients
            new_ingredient = st.text_input(f"New Ingredient {i + 1}", 
                                            value=st.session_state.new_ingredients[i], 
                                            key=f"new_ingredient_{i}")

            # Update the new ingredient list
            if new_ingredient != st.session_state.new_ingredients[i]:  # Check if it's been edited
                st.session_state.new_ingredients[i] = new_ingredient

        # Button to add another ingredient input field
        if st.button("Add Ingredient"):
            st.session_state.new_ingredient_fields += 1  # Increment the count of new ingredient fields
            st.session_state.new_ingredients.append("")  # Add a placeholder for the new ingredient
            st.rerun()

        # Combine detected ingredients with new ingredients
        ingredients = ingredients + [ing for ing in st.session_state.new_ingredients if ing]

        # Display current ingredients list
        st.write("Ingredients: " + ", ".join(ingredients))
        if st.button("Get my recipe!"):
        #    st.session_state.rec_list = get_recipe(ingredients)
        #    st.session_state.page = "results"
            with st.spinner('Fetching recipes for you...'):
                st.session_state.rec_list = get_recipe(ingredients)
                st.session_state.page = "results"
            st.rerun()

    return ingredients

# Initialize session state for page
if 'page' not in st.session_state:
    st.session_state.page = 'home'
# Navigation logic
if st.session_state.page == 'upload':
    ingredients = upload()
    with open("ingredients.txt", "w") as file:
        for item in ingredients:
            file.write(f"{item}\n")
elif st.session_state.page == 'home':
    home.home()
elif st.session_state.page == 'results':
    with open("ingredients.txt", "r") as file:
        ingredients = [line.strip() for line in file.readlines()]  # Remove newline characters
    results.show(ingredients)