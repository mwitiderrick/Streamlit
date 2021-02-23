import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("../data/ted.csv")

day = st.text_input("Day of the Week", "Sunday")

if day is not None:
    dff = df[df["published_day"] == day]
    chart = (
        alt.Chart(dff)
        .mark_bar()
        .encode(
            x="published_year:O",
            y="sum(views)",
            color="published_day",
            tooltip=["sum(views)"],
        )
        .interactive()
        .properties(width=700, height=500)
    )
    st.altair_chart(chart)