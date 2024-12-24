import streamlit as st
import os
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

st.set_page_config("CTM Desk - Lit")

# 
st.title("Management")

st.page_link("pages/addbio.py", label="Add Bio Data")
st.page_link("pages/getdata.py", label="View Data Table")