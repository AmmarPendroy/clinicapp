# style.py
import streamlit as st

def set_background(theme):
    themes = {
        "White": {"bg": "#ffffff", "text": "#000000"},
        "Black": {"bg": "#000000", "text": "#ffffff"}
    }

    selected = themes.get(theme, themes["White"])
    bg = selected["bg"]
    text = selected["text"]

    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {bg};
            color: {text};
        }}
        </style>
    """, unsafe_allow_html=True)
