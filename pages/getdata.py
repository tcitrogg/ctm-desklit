import streamlit as st
import os
from streamlit_gsheets import GSheetsConnection
from fx import read_csv, mk_lake, write_to_csv

ARCHITECT = "Tcitrogg"
BIO_URL   = "https://bnierimi.vercel.app"
APPNAME   = "MakeDP"

# url
GENERAL_LAKENAME  = ".general-biodata.csv"
ANNIVERSARY_LAKENAME  = ".wedann-biodata.csv"

# GENERAL_LAKENAME  = ".general-biodata.csv"
# ANNIVERSARY_LAKENAME  = ".wedann-biodata.csv"

# st.write(f"""fetch data""")

mk_lake(GENERAL_LAKENAME)
mk_lake(ANNIVERSARY_LAKENAME)

general_content = read_csv(GENERAL_LAKENAME)
anniversary_content = read_csv(ANNIVERSARY_LAKENAME)

with st.container():
    st.subheader("General")
    general_content = st.data_editor(general_content[::-1], use_container_width=True)
    if general_content:
        write_to_csv(general_content[::-1], GENERAL_LAKENAME)

with st.container():
    st.subheader("Anniversary")
    anniversary_content = st.data_editor(anniversary_content[::-1], use_container_width=True)
    if anniversary_content:
        write_to_csv(anniversary_content[::-1], ANNIVERSARY_LAKENAME)