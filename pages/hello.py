import streamlit as st
from PIL import Image, ImageOps

# Session state to keep track of which page the user is on
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # Default to 'home' page

# Function to change pages
def navigate_to(page):
    st.session_state.page = page

# Home Page
if st.session_state.page == 'home':
    st.title("Image Uploader and Viewer")
    
    # File uploader for images
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Open and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Save the image in session state to pass to the next page
        st.session_state.image = image
        
        # Button to go to the next page (simulates routing)
        if st.button("Submit"):
            navigate_to('result')

# Result Page
elif st.session_state.page == 'result':
    st.title("Image Processing Result")
    
    # Display the uploaded image (retrieved from session state)
    if 'image' in st.session_state:
        st.image(st.session_state.image, caption="Uploaded Image", use_column_width=True)
        
        # Convert to grayscale and display
        gray_image = ImageOps.grayscale(st.session_state.image)
        st.image(gray_image, caption="Grayscale Image", use_column_width=True)
        
        # Button to return to the home page
        if st.button("Go Back"):
            navigate_to('home')


