import streamlit as st
import pandas as pd
import plotly.express as px

# Import necessary functions
from sidebar import setup_sidebar
from style import set_background

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
        "Phone Number": ["7501234567", "7509876543", "7505555555"]
    }
    return pd.DataFrame(data)

df = load_data()

# ----- Sidebar -----
page, theme = setup_sidebar()

# Apply selected theme for both main content and sidebar
set_background(theme)

# ----- Main Content -----
st.title("🏥 Clinic Client Dashboard")

# Client overview
if page == "Dashboard":
    st.subheader("📊 Client Overview")
    st.dataframe(df.style.highlight_max(axis=0))  # Styled dataframe

    st.markdown("### Gender Distribution")
    gender_counts = df["Gender"].value_counts()
    gender_pie = px.pie(names=gender_counts.index, values=gender_counts.values, title="Gender Distribution")
    st.plotly_chart(gender_pie)

    st.markdown("### Age Distribution")
    age_dist = px.histogram(df, x="Age", title="Age Distribution")
    st.plotly_chart(age_dist)

# Add New Client
elif page == "Add New Client":
    st.subheader("➕ Add New Client")
    
    with st.form("client_form"):
        name = st.text_input("Name")
        phone = st.text_input("Phone Number", max_chars=10)
        age = st.number_input("Age", min_value=0,
