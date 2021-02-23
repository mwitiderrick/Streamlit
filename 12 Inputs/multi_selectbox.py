import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("../data/ted.csv")

unique_days = tuple(df["published_day"].unique())
days = st.multiselect("Select Days", unique_days)

if days is not None:
    dff = df[df["published_day"].isin(days)]
    chart = (
        alt.Chart(dff)
        .mark_bar()
        .encode(x="published_year:O", y="sum(views)", color="published_day")
        .interactive()
        .properties(width=700, height=500)
    )
    st.altair_chart(chart)