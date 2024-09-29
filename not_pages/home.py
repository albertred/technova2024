import streamlit as st

def home():
    # URL of the background image
    background_image_url = "https://media.discordapp.net/attachments/1155327631361835119/1289648145713856684/Untitled_design_37.png?ex=66f995ee&is=66f8446e&hm=0dc366d98bee629ae4de11661932e734a89c5c7a783d1e55ec5fdd278efee563&=&format=webp&quality=lossless&width=1100&height=618"
    logo_path = "logo.webp"

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
        }}

        .centered-content {{
            display: flex;
            flex-direction: column;
            justify-content: center;  /* Center vertically */
            align-items: center;
            height: auto;  /* Let content define height */
            text-align: center;
        }}
        .title {{
            font-size: 65px;
            font-weight: bold;
            margin-top: 5px;  /* Adjusted to reduce space above */
            margin-bottom: 5px;  /* Reduced space below the title */
        }}
        .subtitle {{
            font-size: 24px;
            font-weight: normal;
            color: #f4a261;
            margin-bottom: 20px;  /* Reduced space before button */
        }}

        .orange-box {{
            background-color: #f4a261;
            color: white;
            padding: 30px;
            border-radius: 5px; /* Rounded corners */
            margin-top: 30px;
        }}
        .orange-box-text {{
            font-size: 18px;
            line-height: 1.6;
        }}
        .dark-orange-box {{
            background-color: #FF7F50;
            color: white;
            padding: 30px;
            border-radius: 5px; /* Rounded corners */
            margin-top: 50px;
        }}
        </style>
    """, unsafe_allow_html=True)
    st.image(logo_path, use_column_width=True)
    
    # HTML layout for the page content
    st.markdown(f"""
        <div class="centered-content">
            <div class="title">Never Waste Food Again</div>
            <div class="subtitle">Transform your leftovers into culinary masterpieces</div>    
        </div>
    """, unsafe_allow_html=True)

    # Columns for button alignment
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        # Add padding to the button to control spacing
        if st.button("Get Started", key="get_started"):
            st.session_state.page = 'upload'
            st.rerun()

    # Additional content boxes below
    st.markdown("""
        <div class="orange-box">
            <p class="orange-box-text">Say goodbye to uninspired meals! FridgeFood empowers you to unlock the potential of your fridge's bounty. Simply snap a photo of your leftovers, and let our intelligent AI suggest mouthwatering recipes tailored to your ingredients.</p>
        </div>
        <div class="dark-orange-box">
            <p class="orange-box-text">Using a vast food dataset, we generate personalized recipes just for you. You can also manually add any ingredients you may have missed.</p>
        </div>
    """, unsafe_allow_html=True)

