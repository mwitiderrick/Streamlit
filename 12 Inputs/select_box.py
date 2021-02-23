import pandas as pd
import streamlit as st
import altair as alt
import datetime

df = pd.read_csv("../data/ted.csv")
unique_days = tuple(df["published_day"].unique())
day = st.selectbox("Select Day of Week", unique_days)

if day is not None:
    dff = df[df["published_day"] == day]
    chart = (
        alt.Chart(dff)
        .mark_bar()
        .encode(
            y="sum(views)",
            x="published_year:O",
            color="published_day",
            tooltip=["sum(views)"],
        )
        .interactive()
        .properties(height=500, width=700)
    )

    st.altair_chart(chart)
