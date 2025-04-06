def set_background(theme):
    """
    Sets the background color and text color based on the selected theme.
    """
    themes = {
        "White": {"bg": "#ffffff", "text": "#000000"},
        "Black": {"bg": "#000000", "text": "#ffffff"},
    }

    selected = themes.get(theme, themes["White"])
    bg_color = selected["bg"]
    text_color = selected["text"]

    # Apply background to both the app content and sidebar
    st.markdown(
        f"""
        <style>
            html, body, [class*="css"] {{
                background-color: {bg_color} !important;
                color: {text_color} !important;
            }}
            .stApp {{
                background-color: {bg_color} !important;
                color: {text_color} !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
