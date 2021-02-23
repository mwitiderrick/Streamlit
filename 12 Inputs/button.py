import streamlit as st

if st.button("Show Slider"):
    start_year, end_year = st.select_slider(
        "Select Years", options=[2012, 2013, 2014, 2015, 2017], value=(2012, 2017)
    )
else:
    st.write("Click to show slider")