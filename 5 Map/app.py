import pandas as pd
import streamlit as st

df = pd.read_csv("../data/uber.csv")
map_data = df[["lat", "lon"]]
st.map(map_data)