import streamlit as st
import os
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 
st.title("Management")

# Connect with Lake
LAKE_CONN = st.connection("gsheets", type=GSheetsConnection)

# Fetch data
existing_data = LAKE_CONN.read(worksheet="responses_one", ttl=5)
# existing_data = existing_data.dropna(how="all")

st.dataframe(existing_data)

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
    name = st.text_input("Name*")
    phone_number = st.text_input("Phone number")
    email = st.text_input("Email")
    gender = st.radio("Gender", ["Male", "Female"])
    date_of_birth = st.date_input("Date of Birth")
    department = st.text_input("Department")
    is_student = st.radio("Are you a:", ["Student", "Non-student"])
    address = st.text_input("Address")
    units = st.multiselect("Unit", UNIT_TYPES)

    st.write("***: Required fields**")

    submit_button = st.form_submit_button(label="Save")

    if submit_button:
        if not name:
            st.warning("Required field must be filled.")
            st.stop()
        elif existing_data["Name"].str.contains(name).any() and existing_data["Date of Birth"].str.contains(date_of_birth).any():
            st.warning("Person already exists.")
            st.stop()
        else:
            # Create a new row of data
            newbio_data = pd.Dataframe([
                {
                    "Name": name,
                    "Phone number": phone_number,
                    "Email": email,
                    "Gender": gender,
                    "Date of Birth": date_of_birth.strftime("%d-%m"),
                    "Department": department,
                    "Are you a:": is_student,
                    "Address": address,
                    "Unit": units,
                }
            ])

            # Add new data to existing dat
            updated_df = pd.concat([existing_data, newbio_data], ignore_index=True)

            # Update SheetLake with new data
            LAKE_CONN.update(worksheet="responses_one", data=updated_df)
            
            st.success("Saved data")