import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("../data/ted.csv")

left_column, right_column = st.beta_columns(2)

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="published_year:O",
        y="sum(views)",
        color="published_day",
        tooltip=["sum(views)"],
    )
    .interactive()
    .properties(width=500, height=500)
)

with left_column:
    st.altair_chart(chart)

with right_column:
    st.altair_chart(chart)

with st.beta_container():
    st.altair_chart(chart)

with st.beta_expander("Some Explanation"):
    st.write("Some explanation")