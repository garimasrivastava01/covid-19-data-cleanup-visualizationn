import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔥 Global Intensity Heatmap")

@st.cache_data
def load_data():
    df = pd.read_csv("Data/covid_dataset/covid_19_clean_complete.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

metric = st.selectbox("Select Metric", ["Confirmed", "Deaths", "Recovered"])

# Take latest date snapshot
latest_date = df["Date"].max()
latest_df = df[df["Date"] == latest_date]

top_countries = latest_df.sort_values(metric, ascending=False).head(20)

fig = px.density_heatmap(
    top_countries,
    x="Country/Region",
    y=metric,
    color_continuous_scale="Turbo",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)