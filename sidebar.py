import streamlit as st

# Function to set up sidebar navigation and theme selection
def setup_sidebar():
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Add New Client"])

    # Theme switcher (only White and Black available)
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎨 Theme Style")
    theme = st.sidebar.selectbox("Choose background style", [
        "White", "Black"
    ])

    # Sidebar background switcher (only White and Black available)
    st.sidebar.markdown("---")
    st.sidebar.subheader("🌈 Sidebar Background Style")
    sidebar_theme = st.sidebar.selectbox("Choose sidebar background style", [
        "White", "Black"
    ])

    # Contact info
    st.sidebar.markdown("---")
    st.sidebar.subheader("📞 Contact")
    st.sidebar.markdown("📧 Email: ammar.muhammed@geg-construction.com")
    st.sidebar.markdown("📱 Phone: +964 750 389 8085")

    return page, theme, sidebar_theme
