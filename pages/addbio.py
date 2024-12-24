import streamlit as st
import os
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

# 
st.subheader("Management")
st.title("Bio Data")

# Connect with Lake
LAKE_CONN = st.connection("gsheets", type=GSheetsConnection)

# Fetch data
existing_data = LAKE_CONN.read(worksheet="BioData", ttl=5)

# list of units
UNIT_TYPES = [
    "Prayer & Evangelism",
    "Children",
    "Ushering",
    "Choir",
    "Media",
    "Library",
    "Technical",
    "Drama"
]

# data form
with st.form(key="bio_form"):
    name = st.text_input("Name*").title()
    phone_number = st.text_input("Phone number")
    email = st.text_input("Email")
    gender = st.radio("Gender", ["Male", "Female"])
    date_of_birth = st.date_input("Date of Birth")
    department = st.text_input("Department").title()
    is_student = st.radio("Is a Student", [True, False])
    address = st.text_input("Address")
    units = st.multiselect("Unit", UNIT_TYPES)

    st.write("***: Required fields**")

    submit_button = st.form_submit_button(label="Save")

    if submit_button:
        if not name:
            st.warning("Required field must be filled.")
            st.stop()
        elif existing_data["Name"].str.contains(name).any() and existing_data["Date of Birth"].str.contains(str(date_of_birth)).any():
            st.warning("Person already exists.")
            st.stop()
        else:
            # Create a new row of data
            newbio_data = pd.DataFrame([
                {
                    "Name": name,
                    "Phone number": phone_number,
                    "Email": email,
                    "Gender": gender,
                    "Date of Birth": date_of_birth.strftime("%d-%m"),
                    "Department": department,
                    "Is a Student": is_student,
                    "Address": address,
                    "Unit": units,
                    "Timestamp": datetime.now().timestamp()
                }
            ])

            # Add new data to existing dat
            updated_df = pd.concat([existing_data, newbio_data], ignore_index=True)

            # Update SheetLake with new data
            LAKE_CONN.update(worksheet="BioData", data=updated_df)
            
            st.success("Saved data")
            name = ""
            phone_number = ""
            email = ""
            gender = ""
            date_of_birth = ""
            department = ""
            is_student = ""
            address = ""
            units = ""