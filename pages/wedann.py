import streamlit as st
import os
from streamlit_gsheets import GSheetsConnection
from fx import append_csv, is_exist

ARCHITECT = "Tcitrogg"
BIO_URL   = "https://bnierimi.vercel.app"
APPNAME   = "MakeDP"

LAKENAME  = ".wedann-biodata.csv"


st.write(f"""Wedding Anniversary""")

row_data = []

with st.container(border=True):
    name = st.text_input("Name")
    anniversary_date = st.date_input("Date")
    row_data = [name, anniversary_date.strftime("%d-%m")]

save_button = st.button("Save data")

if save_button:
    data_exist = is_exist(row_data=row_data, lakename=LAKENAME)
    if not data_exist:
        append_csv(row=row_data, lakename=LAKENAME)
        row_data = []
        with st.container(border=True):
        #     st.write(f"""- {name}
        # - {anniversary_date}
        # """)
            st.success(f"Saved")
    else:
        st.warning("Data Exists in Lake")

