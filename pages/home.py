import streamlit as st

# hide nav bar, and make own nav bar
# nav bar styling

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
    }
    
   
    /* Set the body and main container to have the same background color */
    .centered-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        text-align: center;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
    }
    .subtitle {
        font-size: 24px;
        font-weight: normal;
        color: #f4a261;
    }
    .upload-button {
        margin-top: 30px;
        padding: 15px 30px;
        background-color: #f4a261;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        cursor: pointer;
    }
    .upload-button:hover {
        background-color: #e07a5f;
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

# HTML layout for the page content
st.markdown("""
    <div class="centered-content">
        <div class="title">Never Waste Food Again</div>
        <div class="subtitle">Transform your leftovers into culinary masterpieces.</div>
        <form action="/">
            <button class="upload-button" onclick="window.location.href='/app.py'">Get Started</button>
        </form>
    </div>
""", unsafe_allow_html=True)