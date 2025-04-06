import streamlit as st

# ----- Theme Styling -----
def set_background(main_color_name, sidebar_color_name):
    # Define two color themes: White and Black
    themes = {
        "White": {"bg": "#ffffff", "text": "#000000"},
        "Black": {"bg": "#000000", "text": "#ffffff"},
    }

    # Select main and sidebar themes based on user choice
    selected_main = themes.get(main_color_name, themes["White"])
    selected_sidebar = themes.get(sidebar_color_name, themes["White"])

    # Extract background and text colors
    bg_color = selected_main["bg"]
    text_color = selected_main["text"]
    sidebar_bg_color = selected_sidebar["bg"]

    # Determine contrasting text color for the sidebar based on background color
    def get_contrasting_text_color(background_color):
        if background_color == "#ffffff":  # White background
            return "#000000"  # Black text for white background
        else:  # Black background
            return "#ffffff"  # White text for black background

    sidebar_text_color = get_contrasting_text_color(sidebar_bg_color)

    # Apply custom CSS for both main background and sidebar with dynamic text color
    st.markdown(
        f"""
        <style>
        html, body, .stApp {{
            background-color: {bg_color} !important;
            color: {text_color} !important;
        }}
        .stSidebar {{
            background-color: {sidebar_bg_color} !important;
        }}
        .stSidebar .sidebar .css-1d391kg {{
            color: {sidebar_text_color} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
