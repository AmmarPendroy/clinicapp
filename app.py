import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----- Sample Data -----
@st.cache_data
def load_data():
    data = {
        "Client ID": [101, 102, 103],
        "Name": ["Alice Smith", "John Doe", "Fatima Ahmed"],
        "Age": [34, 45, 29],
        "Gender": ["Female", "Male", "Female"],
        "Visit Date": ["2024-01-15", "2024-03-22", "2024-04-01"],
        "Diagnosis": ["Flu", "Check-up", "Diabetes"],
    }
    return pd.DataFrame(data)

df = load_data()

# ----- Sidebar -----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Add New Client"])

# Theme switcher
st.sidebar.markdown("---")
st.sidebar.subheader("🎨 Theme Style")
theme = st.sidebar.selectbox("Choose background style", [
    "Classic White", "Soft Blue", "Dark Mode", "Light Green", "Peach"
])

# Sidebar background switcher
st.sidebar.markdown("---")
st.sidebar.subheader("🌈 Sidebar Background Style")
sidebar_theme = st.sidebar.selectbox("Choose sidebar background style", [
    "Classic White", "Soft Blue", "Dark Mode", "Light Green", "Peach"
])

# Contact info
st.sidebar.markdown("---")
st.sidebar.subheader("📞 Contact")
st.sidebar.markdown("📧 Email: ammar.muhammed@geg-construction.com")
st.sidebar.markdown("📱 Phone: +964 750 389 8085")

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

# Apply selected theme and sidebar theme
set_background(theme, sidebar_theme)

# ----- Main Content -----
st.title("🏥 Clinic Client Dashboard")

if page == "Dashboard":
    st.subheader("📊 Client Overview")
    st.dataframe(df)

    st.markdown("### Gender Distribution")
    gender_counts = df["Gender"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    st.pyplot(fig)

    st.markdown("### Age Distribution")
    st.bar_chart(df["Age"])

elif page == "Add New Client":
    st.subheader("➕ Add New Client")
    
    with st.form("client_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        visit_date = st.date_input("Visit Date")
        diagnosis = st.text_input("Diagnosis")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success(f"New client '{name}' added (Note: Not saved permanently in this demo).")
