import streamlit as st
import os
from streamlit_gsheets import GSheetsConnection
from fx import append_csv, is_exist

ARCHITECT = "Tcitrogg"
BIO_URL   = "https://bnierimi.vercel.app"
APPNAME   = "Biovault"

LAKENAME  = ".general-biodata.csv"

# DATA_SCHEMA = {
#     "name": "",
#     "date_of_birth": "",
#     "gender": "",
#     "department": "",
#     "email": "",
#     "phone_number": "",
# }

st.set_page_config(page_title=APPNAME, menu_items={
# 'About': "# This is a header. This is an *extremely* cool app!"
'Get help': 'mailto:tcitrogg@gmail.com',
})

# side bar
# sidebar = st.sidebar
# sidebar.page_link("addbio.py", label="Biodata", icon="🏠")
# sidebar.page_link("pages/wedann.py", label="Wedding Annivesary", icon="1️⃣")
# sidebar.page_link("pages/getdata.py", label="Fetch Data", icon="2️⃣")


row_data = []

# -------- Home
# main board
with st.container(border=True):
    name = st.text_input("Name")
    phone_number = st.text_input("Phone number")
    email = st.text_input("Email")
    date_of_birth = st.date_input("Date of Birth")
    gender = st.radio("Gender", ["Male", "Female"])
    department = st.text_input("Department")
    is_student = st.radio("Are you a:", ["Student", "Non-student"])
    address = st.text_input("Address")
    row_data = [name, phone_number, email, date_of_birth.strftime("%d-%m"), gender, department, is_student, address]

save_button = st.button("Save data")

if save_button:
    data_exist = is_exist(row_data=row_data, lakename=LAKENAME)
    if not data_exist:
        append_csv(row=row_data, lakename=LAKENAME)
        row_data = []
        with st.container(border=True):
        #     st.write(f"""- {name}
        # - {date_of_birth}
        # - {gender}
        # - {department}
        # - {phone_number}
        # """)
            st.success(f"Saved")
    else:
        st.warning("Data Exists in Lake")

