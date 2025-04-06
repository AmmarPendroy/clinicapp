import streamlit as st

# ----- Theme Styling -----
def set_background(main_color_name, sidebar_color_name):
    themes = {
        "Classic White": {"bg": "#ffffff", "text": "#000000"},
        "Soft Blue": {"bg": "#d0e6f7", "text": "#000000"},
        "Dark Mode": {"bg": "#1e1e1e", "text": "#ffffff"},
        "Light Green": {"bg": "#d4f7d4", "text": "#000000"},
        "Peach": {"bg": "#ffe5b4", "text": "#000000"}
    }

    # Define main theme colors (background and text)
    selected_main = themes.get(main_color_name, themes["Classic White"])
    selected_sidebar = themes.get(sidebar_color_name, themes["Classic White"])

    bg_color = selected_main["bg"]
    text_color = selected_main["text"]
    sidebar_bg_color = selected_sidebar["bg"]

    # Determine contrasting text color for the sidebar based on background color
    def get_contrasting_text_color(background_color):
        # If the background color is white or close to white, make the text black
        if background_color in ["#ffffff", "#ffe5b4", "#d0e6f7", "#d4f7d4"]:
            return "#000000"  # Black text for light backgrounds
        else:
            return "#ffffff"  # White text for dark backgrounds

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
