import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


@st.cache
def load_data():
    df = pd.read_csv("../data/airbnb.csv")
    return df


df = load_data()


def main():
    plot = st.selectbox(
        "Select a Plot",
        [
            "Pie Chart",
            "Donut Chart",
            "Scatter Plot",
            "Scatter with Columns",
            "Line Plot",
            "Bar",
            "Stacked Bar",
            "Animation",
            "Subplots",
        ],
    )
    if plot == "Pie Chart":
        piechart()
    elif plot == "Donut Chart":
        st.header("Donut Chart")
        donut()
    elif plot == "Scatter Plot":
        st.header("Scatter Plot")
        scatter()
    elif plot == "Scatter with Columns":
        st.header("Scatter with Columns")
        scatter_columns()
    elif plot == "Line Plot":
        st.header("Line Plot")
        line()
    elif plot == "Bar":
        st.header("Bar")
        bar()
    elif plot == "Stacked Bar":
        st.header("Stacked Bar")
        stacked_bar()
    elif plot == "Animation":
        st.header("Animation")
        animate()
    elif plot == "Subplots":
        st.header("Subplots")
        subplot()


def piechart():
    dff = df.groupby("signup_method")["secs_elapsed"].sum().reset_index()
    labels = dff["signup_method"]
    values = dff["secs_elapsed"]
    colors = ["maroon", "black", "orange"]
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hoverinfo="label+percent",
                textinfo="value",
            )
        ]
    )
    fig.update_traces(marker=dict(colors=colors))
    st.plotly_chart(fig)


def donut():
    dff = df.groupby("device_type")["secs_elapsed"].sum().reset_index()
    fig = px.pie(
        dff,
        hole=0.2,
        values="secs_elapsed",
        names="device_type",
        color_discrete_sequence=px.colors.sequential.Aggrnyl,
    )
    st.plotly_chart(fig)


def scatter():
    fig = px.scatter(
        df,
        x="age",
        y="secs_elapsed",
        color="month_name_account_created",
        size="secs_elapsed",
        hover_data=["day_account_created"],
        width=900,
        height=600,
        color_discrete_sequence=px.colors.sequential.Agsunset,
        category_orders={
            "month_name_account_created": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
            ]
        },
    )
    st.plotly_chart(fig)


def scatter_columns():
    fig = px.scatter(
        df,
        x="age",
        y="secs_elapsed",
        color="month_name_account_created",
        size="secs_elapsed",
        hover_data=["day_account_created"],
        facet_col="signup_method",
        width=900,
        height=600,
        color_discrete_sequence=px.colors.sequential.algae,
        category_orders={
            "month_name_account_created": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
            ]
        },
    )
    st.plotly_chart(fig)


def line():
    dff = df.groupby("dayofyear_account_created")["user_id"].count().reset_index()
    dff.columns = ["Day of Year", "Number of Accounts"]
    fig = px.line(dff, x="Day of Year", y="Number of Accounts", width=1000)
    fig.update_traces(line_color="maroon")
    st.plotly_chart(fig)


def bar():
    dff = df.groupby("device_type")["secs_elapsed"].sum().reset_index()
    fig = px.bar(
        dff,
        x="device_type",
        y="secs_elapsed",
        title="Seconds Vs Device Type",
        width=900,
        height=700,
        color="device_type",
        color_discrete_sequence=px.colors.qualitative.G10,
    )
    st.plotly_chart(fig)


def stacked_bar():
    dff = (
        df.groupby(["device_type", "signup_method"])["secs_elapsed"].sum().reset_index()
    )
    fig = px.bar(
        dff,
        x="device_type",
        y="secs_elapsed",
        title="Seconds vs Device Type",
        color="signup_method",
        color_discrete_sequence=px.colors.qualitative.D3,
        width=900,
        height=700,
    )
    st.plotly_chart(fig)


def animate():
    fig = px.scatter(
        df,
        x="age",
        y="secs_elapsed",
        color="signup_method",
        animation_frame="month_name_account_created",
        size="secs_elapsed",
        size_max=40,
        hover_data=["day_account_created"],
        width=900,
        height=600,
        color_discrete_sequence=px.colors.sequential.Agsunset,
        category_orders={
            "month_name_account_created": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
            ]
        },
    )
    st.plotly_chart(fig)


def subplot():
    dff = df.groupby("signup_method")["secs_elapsed"].sum().reset_index()
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(
        go.Bar(
            x=dff["signup_method"], y=dff["secs_elapsed"], marker=dict(color="SkyBlue")
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Bar(x=dff["signup_method"], y=dff["secs_elapsed"], marker=dict(color="red")),
        row=1,
        col=2,
    )
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()