import pandas as pd
import streamlit as st
import altair as alt
import datetime

df = pd.read_csv("../data/ted.csv")

start_date = st.date_input("Start Date - Publishing", datetime.date(2006, 1, 1))
end_date = st.date_input("Start Date - Publishing", datetime.date(2017, 12, 12))

df["published_date"] = pd.to_datetime(df["published_date"])
if (start_date is not None) & (end_date is not None):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    dff = df[df["published_date"].isin(pd.date_range(start_date, end_date))]

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
        .properties(height=500, width=700)
    )
    st.altair_chart(chart)
