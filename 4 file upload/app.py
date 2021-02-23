import pandas as pd
import streamlit as st
import time

uploaded_file = st.file_uploader("Choose File", type=["csv"])

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    # progress_bar = st.progress(0)
    # for percentage_complete in range(100):
    #     time.sleep(0.1)
    #     progress_bar.progress(percentage_complete+1)
    # st.write(dataframe)
    with st.spinner("Writing to DF.."):
        time.sleep(5)
        st.write(dataframe)