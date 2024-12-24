import streamlit as st
import os
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

ARCHITECT = "Tcitrogg"
BIO_URL   = "https://bnierimi.vercel.app"
APPNAME   = "MakeDP"

st.title("Management")

# Connect with Lake
LAKE_CONN = st.connection("gsheets", type=GSheetsConnection)

# Fetch data
existing_data = LAKE_CONN.read(worksheet="BioData", ttl=5)
# existing_data = existing_data.dropna(how="all")


with st.container():
    st.subheader("General")
    st.dataframe(existing_data)