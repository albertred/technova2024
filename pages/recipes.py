import streamlit as st

# CSS to customize the look of the sidebar and the recipe cards
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

# Sidebar content
st.sidebar.title("Recipes")
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
