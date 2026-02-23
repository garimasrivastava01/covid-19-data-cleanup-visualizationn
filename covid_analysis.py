import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\prasa\Desktop\Module_4 Project\covid_project\Data\covid dataset\covid_19_clean_complete.csv")

df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

df.rename(columns={
    'Country/Region': 'Country',
    'Province/State': 'State'
}, inplace=True)

print(df.head())



# Global Trend (Date wise total cases)
global_trend = df.groupby("Date")[["Confirmed", "Deaths", "Recovered", "Active"]].sum().reset_index()

print(global_trend.head())



plt.figure(figsize=(12,6))

plt.plot(global_trend["Date"], global_trend["Confirmed"], label="Confirmed")
plt.plot(global_trend["Date"], global_trend["Deaths"], label="Deaths")
plt.plot(global_trend["Date"], global_trend["Recovered"], label="Recovered")

plt.title("Global COVID-19 Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


country_summary = df.groupby("Country")[["Confirmed", "Deaths", "Recovered"]].max().reset_index()

top10 = country_summary.sort_values("Confirmed", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top10, x="Confirmed", y="Country")

plt.title("Top 10 Countries by Confirmed Cases")
plt.tight_layout()
plt.show()


country_summary["Mortality_Rate"] = (country_summary["Deaths"] / country_summary["Confirmed"]) * 100
country_summary["Recovery_Rate"] = (country_summary["Recovered"] / country_summary["Confirmed"]) * 100

print(country_summary.sort_values("Mortality_Rate", ascending=False).head())



global_trend["7_day_avg"] = global_trend["Confirmed"].rolling(7).mean()

plt.figure(figsize=(12,6))
plt.plot(global_trend["Date"], global_trend["Confirmed"], alpha=0.5, label="Daily Confirmed")
plt.plot(global_trend["Date"], global_trend["7_day_avg"], linewidth=3, label="7 Day Moving Avg")

plt.legend()
plt.title("Confirmed Cases with 7-Day Moving Average")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Get latest date data
latest_date = df["Date"].max()
latest_data = df[df["Date"] == latest_date]

# Pivot table for heatmap
heatmap_data = latest_data.groupby("Country")["Confirmed"].sum().reset_index()

top20 = heatmap_data.sort_values("Confirmed", ascending=False).head(20)

# Set index for heatmap
top20.set_index("Country", inplace=True)

plt.figure(figsize=(10,8))
sns.heatmap(top20, cmap="Reds", annot=True, fmt=".0f")

plt.title("Top 20 Countries - Confirmed Cases Heatmap")
plt.tight_layout()
plt.show()