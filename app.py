import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    }
    return pd.DataFrame(data)

df = load_data()

# ----- Sidebar -----
page, theme = setup_sidebar()

# Apply selected theme for both main content and sidebar
set_background(theme)

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
