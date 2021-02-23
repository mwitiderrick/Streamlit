import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


@st.cache
def load_data():
    df = pd.read_csv("../data/ted.csv")
    return df


df = load_data()


def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage",
            "Bar Plot",
            "Horizontal Bar Plot",
            "Scatter Plot",
            "Histogram",
            "Pie Chart",
            "Two Subplots",
            "Four Subplots",
            "Two Axes",
            "Four Axes",
        ],
    )

    if page == "Homepage":
        # st.header("Data Application")
        """
        # Building apps with Streamlit
        Please select a page on the left
        """
        st.balloons()
        st.write(df)
    elif page == "Bar Plot":
        bar_chart()

    elif page == "Horizontal Bar Plot":
        horizontal_bar()

    elif page == "Scatter Plot":
        visualize_scatter()

    elif page == "Histogram":
        st.header("Languages Histogram")
        histogram()

    elif page == "Pie Chart":
        st.header("Views and Day Pie Chart")
        pie_chart()

    elif page == "Two Subplots":
        st.header("Two Subplots")
        two_subplots()
    elif page == "Four Subplots":
        st.header("Four Subplots")
        four_subplots()

    elif page == "Two Axes":
        st.header("Two Axes")
        two_axes()

    elif page == "Four Axes":
        st.header("Four Axes")
        four_axes()


def bar_chart():
    fig = plt.figure(figsize=(12, 5))
    plt.xticks(rotation=80)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    plt.ticklabel_format(style="plain")
    plt.bar(bar_data["event"], bar_data["views"])
    plt.xlabel("Event")
    plt.ylabel("Views")
    plt.title("Event and Views Plot")
    st.pyplot(fig)


def horizontal_bar():
    fig = plt.figure(figsize=(12, 5))
    plt.xticks(rotation=80)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    plt.ticklabel_format(style="plain")
    plt.barh(bar_data["event"], bar_data["views"])
    plt.xlabel("Event")
    plt.ylabel("Views")
    plt.title("Event and Views Plot")
    st.pyplot(fig)


def visualize_scatter():
    fig = plt.figure(figsize=(10, 8))
    plt.scatter(
        x=df["comments"],
        y=df["views"],
        marker="*",
        s=df["languages"],
        c=df["languages"],
        alpha=0.5,
    )
    st.pyplot(fig)


def histogram():
    fig = plt.figure(figsize=(12, 5))
    plt.hist(df["languages"], color="y", bins=50)
    st.pyplot(fig)


def pie_chart():
    days_data = (
        df.groupby("published_day")["views"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig = plt.figure(figsize=(10, 8))
    explode = (0.1, 0, 0, 0, 0, 0, 0)
    plt.pie(
        days_data["views"],
        labels=days_data["published_day"],
        shadow=True,
        explode=explode,
        autopct="%1.1f%%",
    )
    st.pyplot(fig)


def two_subplots():
    fig = plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    plt.barh(bar_data["event"], bar_data["views"])

    plt.subplot(1, 2, 2)
    plt.scatter(df["views"], df["comments"], c=df["languages"], marker="*")
    st.pyplot(fig)


def four_subplots():
    days_data = (
        df.groupby("published_day")["views"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    months_data = (
        df.groupby("published_month")["views"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig = plt.figure(figsize=(12, 10))
    plt.subplot(2, 2, 1)
    plt.title("Views & Published Day")
    plt.pie(
        days_data["views"],
        labels=days_data["published_day"],
        shadow=True,
        autopct="%1.1f%%",
    )
    plt.subplot(2, 2, 2)
    plt.title("Views & Published Month")
    plt.pie(
        months_data["views"],
        labels=months_data["published_month"],
        shadow=True,
        autopct="%1.1f%%",
    )
    plt.subplot(2, 2, 3)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    plt.xticks(rotation=80)
    plt.bar(bar_data["event"], bar_data["views"])

    plt.subplot(2, 2, 4)
    views = df.groupby("published_year")["views"].sum().reset_index()
    plt.plot(views["published_year"], views["views"])

    st.pyplot(fig)


def two_axes():
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    ax[0].barh(bar_data["event"], bar_data["views"])
    ax[1].scatter(df["views"], df["comments"], c=df["languages"], marker="*")
    st.pyplot(fig)


def four_axes():
    days_data = (
        df.groupby("published_day")["views"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    months_data = (
        df.groupby("published_month")["views"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig, ax = plt.subplots(2, 2, figsize=(12, 10))

    ax[0, 0].pie(
        days_data["views"],
        labels=days_data["published_day"],
        shadow=True,
        autopct="%1.1f%%",
    )
    ax[0, 1].pie(
        months_data["views"],
        labels=months_data["published_month"],
        shadow=True,
        autopct="%1.1f%%",
    )

    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    ax[1, 0].bar(bar_data["event"], bar_data["views"])

    views = df.groupby("published_year")["views"].sum().reset_index()
    ax[1, 1].plot(views["published_year"], views["views"])

    st.pyplot(fig)


if __name__ == "__main__":
    main()