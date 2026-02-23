import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Global Animated COVID Map")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Data/covid_dataset/covid_19_clean_complete.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# -----------------------------
# METRIC SELECTOR
# -----------------------------
metric = st.selectbox(
    "Select Metric",
    ["Confirmed", "Deaths", "Recovered"]
)

# -----------------------------
# AGGREGATE DATA
# -----------------------------
df_grouped = (
    df.groupby(["Country/Region", "Date"])[
        ["Confirmed", "Deaths", "Recovered", "Lat", "Long"]
    ]
    .sum()
    .reset_index()
)

# -----------------------------
# COLOR LOGIC (Professional Look)
# -----------------------------
color_scales = {
    "Confirmed": "Reds",
    "Deaths": "Inferno",
    "Recovered": "Greens"
}

# -----------------------------
# CREATE ANIMATED MAP
# -----------------------------
fig = px.scatter_geo(
    df_grouped,
    lat="Lat",
    lon="Long",
    size=metric,
    color=metric,
    hover_name="Country/Region",
    animation_frame="Date",
    projection="natural earth",
    template="plotly_dark",
    color_continuous_scale=color_scales[metric]
)

# -----------------------------
# MAP STYLING
# -----------------------------
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    coloraxis_colorbar=dict(
        title=metric,
        thickness=15,
        len=0.6
    ),
    geo=dict(
        showland=True,
        landcolor="rgb(20,20,20)",
        showocean=True,
        oceancolor="rgb(5,10,25)",
        showcountries=True,
        countrycolor="gray"
    )
)

st.plotly_chart(fig, use_container_width=True)