import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Advanced Trend Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("Data/covid_dataset/covid_19_clean_complete.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Sidebar Controls
country = st.selectbox("Select Country", df["Country/Region"].unique())
metric = st.radio("Select Metric", ["Confirmed", "Deaths", "Recovered"])

country_df = df[df["Country/Region"] == country].sort_values("Date")

# Daily New Cases
country_df["Daily"] = country_df[metric].diff()

# 7-Day Moving Average
country_df["7-Day MA"] = country_df["Daily"].rolling(7).mean()

view_option = st.radio("View Mode", ["Cumulative", "Daily + Moving Avg"])

if view_option == "Cumulative":
    fig = px.line(
        country_df,
        x="Date",
        y=metric,
        template="plotly_dark",
        title=f"{metric} Cases - {country}"
    )
else:
    fig = px.line(
        country_df,
        x="Date",
        y=["Daily", "7-Day MA"],
        template="plotly_dark",
        title=f"Daily {metric} + 7-Day MA - {country}"
    )

st.plotly_chart(fig, use_container_width=True)