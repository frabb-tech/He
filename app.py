
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="HEWRI Dashboard", layout="wide", page_icon="🛡️")

# Logo and Title
# st.image("assets/logo.png", width=300)
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

st.subheader("🧪 Live Conflict Risk Data (Mock)")

regions = ["Lebanon", "Ukraine", "Syria", "Türkiye", "Georgia", "Armenia", "Bosnia", "Palestine", "Afghanistan", "Jordan"]
data = {
    "Country": regions,
    "Conflict Events": np.random.randint(5, 80, len(regions)),
    "Fatalities": np.random.randint(0, 50, len(regions)),
}

df = pd.DataFrame(data)
df["Conflict Score"] = (df["Conflict Events"] * 1.5 + df["Fatalities"] * 3).round(1)
df["Last Updated"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

st.dataframe(df)

alert_df = df[df["Conflict Score"] > 75]
if not alert_df.empty:
    st.error("🚨 Alert: High conflict risk detected in the following countries:")
    st.dataframe(alert_df[["Country", "Conflict Score"]])
else:
    st.success("✅ No high conflict risk detected based on current data.")
