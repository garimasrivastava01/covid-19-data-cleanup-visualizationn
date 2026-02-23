import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Executive Overview")

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Data/covid_dataset/covid_19_clean_complete.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# -------------------------
# GLASS STYLE
# -------------------------
st.markdown("""
<style>
[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.05);
    padding: 15px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# KPI SECTION
# -------------------------
latest_date = df["Date"].max()
previous_date = df["Date"].sort_values().unique()[-2]

latest = df[df["Date"] == latest_date]
previous = df[df["Date"] == previous_date]

total_cases = latest["Confirmed"].sum()
previous_cases = previous["Confirmed"].sum()

growth = ((total_cases - previous_cases) / previous_cases) * 100

col1, col2, col3 = st.columns(3)

col1.metric("🌍 Total Cases", f"{total_cases:,}", delta=f"{growth:.2f}%")
col2.metric("💀 Total Deaths", f"{latest['Deaths'].sum():,}")
col3.metric("💚 Total Recovered", f"{latest['Recovered'].sum():,}")

# -------------------------
# AREA CHART
# -------------------------
trend = df.groupby("Date")[["Confirmed","Deaths","Recovered"]].sum().reset_index()

fig = px.area(
    trend,
    x="Date",
    y=["Confirmed","Deaths","Recovered"],
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# DOWNLOAD SECTION
# -------------------------
st.markdown("---")
st.subheader("📥 Export Latest Snapshot")

st.download_button(
    label="Download Latest Data",
    data=latest.to_csv(index=False),
    file_name="covid_latest_data.csv",
    mime="text/csv"
)