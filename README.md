# covid-19-data-cleanup-visualizationn
# 🦠 COVID-19 Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen?style=for-the-badge)

An advanced multi-page interactive dashboard built using **Python, Pandas, and Streamlit** to analyze and visualize global COVID-19 data.

---

## 📌 Project Overview

This project transforms raw COVID-19 dataset into a structured and interactive analytics dashboard.

It includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Global & Country-wise Insights
- Time-Series Trend Analysis
- Interactive World Map Visualization
- Multi-page Streamlit Web App Deployment

---

## 🎯 Objectives

- Convert messy dataset into clean analytical format  
- Perform real-world time series analysis  
- Build interactive dashboards  
- Deploy as a web application  
- Practice scalable project structure  

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core Programming |
| Pandas | Data Cleaning & Aggregation |
| Matplotlib / Seaborn | Static Visualization |
| Plotly | Interactive Charts |
| Streamlit | Web App Framework |

---

## 📂 Project Structure
covid-19-analytics-dashboard/
│
├── app.py # Main entry point
├── covid_analysis.py # Backend data processing
│
├── Pages/
│ ├── 1_Overview.py
│ ├── 2_Country_Analysis.py
│ ├── 3_Trends_Deep_Dive.py
│ ├── 4_Advanced_Insights.py
│ └── 5_Global_Map.py
│
├── Data/
│ └── covid_dataset/
│ └── covid_19_clean_complete.csv
│
└── .streamlit/
└── config.toml

---

## 📊 Dashboard Features

### 📌 1. Overview
- Global total cases
- Death & recovery statistics
- Time-series visualization

### 🌍 2. Country Analysis
- Country filter
- Individual country trends
- Comparative insights

### 📈 3. Trends Deep Dive
- Growth rate analysis
- Case progression over time
- Trend interpretation

### 🔥 4. Advanced Insights
- Top 10 affected countries
- Death rate comparison
- Aggregated metrics

### 🗺 5. Global Map
- Interactive world visualization
- Geographic impact analysis

---

## 🧹 Data Cleaning Process

- Removed duplicates  
- Handled missing values  
- Converted Date column to datetime  
- Renamed inconsistent columns  
- Used groupby() for aggregations  

---

## 🚀 How to Run Locally

### 1️⃣ Install dependencies

```bash
pip install pandas streamlit matplotlib seaborn plotly

2️⃣ Run the application
streamlit run app.py
The app will automatically open in your browser.

🌐 Deployment

This project can be deployed using:

Streamlit Community Cloud

GitHub integration

Local server hosting

📚 Key Learnings

Real-world dataset handling

Time-series analytics

Interactive dashboard building

Clean project architecture

Deployment workflow

👩‍💻 Author

Garima Srivastava
Data Analytics | AI | Dashboard Development

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
