
import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta

# Config
st.set_page_config(page_title="HEWRI - Conflict Dashboard", layout="wide", page_icon="🛡️")
st.image("assets/logo.png", width=300)
st.title("HEWRI - Humanitarian Early Warning & Response Intelligence")

st.markdown("""
<style>
body {
    background-color: #F1FAEE;
}
h1, h2, h3 {
    color: #003049;
}
.stButton>button {
    background-color: #D62828;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.subheader("📡 Live Conflict Risk Data (Powered by ACLED API)")

# Parameters
api_key = "GgksApEs2Pz6B8wBnzaM"
headers = {"Authorization": f"Bearer {api_key}"}
base_url = "https://api.acleddata.com/acled/read"
countries = [
    "Lebanon", "Ukraine", "Syria", "Türkiye", "Georgia", "Armenia",
    "Bosnia and Herzegovina", "Palestine", "Afghanistan", "Jordan"
]
start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

# Fetch and process data
summary = []
for country in countries:
    params = {
        "event_date_start": start_date,
        "event_date_end": end_date,
        "country": country,
        "limit": 500
    }
    try:
        r = requests.get(base_url, headers=headers, params=params)
        if r.status_code == 200:
            data = r.json().get("data", [])
            events = len(data)
            fatalities = sum(int(e["fatalities"]) for e in data if e["fatalities"].isdigit())
            score = round(events * 1.5 + fatalities * 3, 1)
            summary.append({
                "Country": country,
                "Conflict Events": events,
                "Fatalities": fatalities,
                "Conflict Score": score
            })
        else:
            summary.append({
                "Country": country,
                "Conflict Events": "API Error",
                "Fatalities": "API Error",
                "Conflict Score": "API Error"
            })
    except:
        summary.append({
            "Country": country,
            "Conflict Events": "Error",
            "Fatalities": "Error",
            "Conflict Score": "Error"
        })

df = pd.DataFrame(summary)
df["Last Updated"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.dataframe(df)

# Alert zone
high_risk = df[df["Conflict Score"].apply(lambda x: isinstance(x, (int, float)) and x > 75)]
if not high_risk.empty:
    st.error("🚨 Alert: High conflict risk detected in the following countries:")
    st.dataframe(high_risk[["Country", "Conflict Score"]])
else:
    st.success("✅ No high conflict risk detected based on current data.")
