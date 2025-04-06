import streamlit as st

def setup_sidebar():
    """
    Sets up the sidebar with navigation and theme selection.
    Returns the page and selected theme.
    """
    # Sidebar content
    st.sidebar.image("path_to_your_logo.png", width=150)  # Add your logo

    st.sidebar.title("🏥 Clinic Dashboard")
    st.sidebar.markdown("Welcome to the Clinic Management System")

    page = st.sidebar.radio("Go to", ["Dashboard", "Add New Client"])

    # Theme switcher
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎨 Theme Style")
    theme = st.sidebar.selectbox("Choose background style", ["White", "Black"])

    # Contact info
    st.sidebar.markdown("---")
    st.sidebar.subheader("📞 Contact")
    st.sidebar.markdown("📧 Email: ammar.muhammed@geg-construction.com")
    st.sidebar.markdown("📱 Phone: +964 750 389 8085")
    st.sidebar.markdown("📍 Location: Erbil, Kurdistan Region, Iraq")

    return page, theme
