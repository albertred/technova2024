import streamlit as st

def home():
    
    logo_path = "logo.webp"

    # CSS for background image and navbar styling
    st.markdown(f"""
        <style>
        
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

