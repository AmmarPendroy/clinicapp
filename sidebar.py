# sidebar.py
import streamlit as st

def setup_sidebar():
    st.sidebar.title("Navigation & Settings")

    # Theme selection
    theme = st.sidebar.radio("Choose Theme", ["White", "Black"])

    # Contact info
    st.sidebar.markdown("---")
    st.sidebar.subheader("📞 Contact")
    st.sidebar.markdown("📧 Email: ammar.muhammed@geg-construction.com")
    st.sidebar.markdown("📱 Phone: +964 750 389 8085")
    st.sidebar.markdown("📍 Location: Erbil, Kurdistan Region, Iraq")

    return theme
