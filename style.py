import streamlit as st

# ----- Theme Styling -----
def set_background(main_color_name):
    # Define two color themes: White and Black
    themes = {
        "White": {"bg": "#ffffff", "text": "#000000"},
        "Black": {"bg": "#000000", "text": "#ffffff"},
    }

    # Select the main theme based on user choice
    selected_main = themes.get(main_color_name, themes["White"])

    # Extract background and text colors
    bg_color = selected_main["bg"]
    text_color = selected_main["text"]

    # Apply custom CSS for the main background and sidebar (same background as the main content)
    st.markdown(
        f"""
        <style>
        html, body, .stApp {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}
        .stSidebar {{
            background-color: {bg_color} !important;
        }}
        .stSidebar .sidebar .css-1d391kg {{
            color: {text_color} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
