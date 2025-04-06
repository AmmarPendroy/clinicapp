import streamlit as st
import pandas as pd
import plotly.express as px
from sidebar import setup_sidebar
from style import set_background

# Sample Data
@st.cache_data
def load_data():
    return pd.DataFrame({
        "Client ID": [101, 102, 103],
        "Name": ["Alice Smith", "John Doe", "Fatima Ahmed"],
        "Age": [34, 45, 29],
        "Gender": ["Female", "Male", "Female"],
        "Visit Date": ["2024-01-15", "2024-03-22", "2024-04-01"],
        "Diagnosis": ["Flu", "Check-up", "Diabetes"],
    })

# Load Data
df = load_data()

# Sidebar and Theme
theme = setup_sidebar()
set_background(theme)

# Navigation
st.title("🏥 Clinic Client Dashboard")
page = st.radio("Select View", ["Dashboard", "Add New Client"])

# Dashboard View
if page == "Dashboard":
    st.subheader("📋 Client List")
    st.dataframe(df)

    st.subheader("📊 Gender Distribution")
    gender_counts = df["Gender"].value_counts()
    fig_gender = px.pie(names=gender_counts.index, values=gender_counts.values, title="Gender")
    st.plotly_chart(fig_gender)

    st.subheader("📈 Age Distribution")
    fig_age = px.bar(df, x="Name", y="Age", title="Client Ages")
    st.plotly_chart(fig_age)

# Add Client Form
elif page == "Add New Client":
    st.subheader("➕ Add New Client")

    with st.form("add_client_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        visit_date = st.date_input("Visit Date")
        diagnosis = st.text_input("Diagnosis")
        submitted = st.form_submit_button("Add Client")

        if submitted:
            st.success(f"✅ Client '{name}' added! (Note: Not saved permanently in this demo)")
