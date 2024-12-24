import streamlit as st
import os
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

# 
st.subheader("Management")
st.title("Wedding Anniversary")

# Connect with Lake
LAKE_CONN = st.connection("gsheets", type=GSheetsConnection)

# Fetch data
existing_data = LAKE_CONN.read(worksheet="WeddingAnniversary", ttl=5)

st.dataframe(existing_data)