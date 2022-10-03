import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np
from st_aggrid import AgGrid

st.set_page_config(page_title="SDA Dashboard",
                    page_icon=":bar_chart:",
                    layout="wide")

df = pd.read_csv('matchedPeoplePPV.csv',
                #  skiprows= 1,
                 nrows=10000,
                 index_col=0,
                 )
# print(df)\
st.title("SDA Dashboard")
st.text("Created by Waiee Zainol")
st.dataframe(df)

# ----- SIDEBAR -----
