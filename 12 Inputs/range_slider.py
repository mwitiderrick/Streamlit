import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("../data/ted.csv")

df["published_date"] = pd.to_datetime(df["published_date"])

unique_years = df["published_year"].unique()
max_year = df["published_year"].max()
min_year = df["published_year"].min()

start_year, end_year = st.select_slider(
    "Select Years", options=list(unique_years), value=(min_year, max_year)
)

if (start_year is not None) & (end_year is not None):
    start_year = pd.to_datetime(start_year, format="%Y")
    end_year = pd.to_datetime(end_year, format="%Y")
    dff = df[df["published_date"].isin(pd.date_range(start_year, end_year))]
    chart = (
        alt.Chart(dff)
        .mark_bar()
        .encode(x="published_year:O", y="sum(views)", color="published_day")
        .interactive()
        .properties(height=500, width=700)
    )
    st.altair_chart(chart)
