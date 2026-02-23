import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("Data/covid_dataset/covid_19_clean_complete.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

st.title("🌍 Country Analysis")

country = st.selectbox("Select Country", df["Country/Region"].unique())

country_df = df[df["Country/Region"] == country]

fig = px.line(
    country_df,
    x="Date",
    y=["Confirmed","Deaths","Recovered"],
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)