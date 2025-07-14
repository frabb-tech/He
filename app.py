
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="HEWRI Dashboard", layout="wide")

st.title("HEWRI - Humanitarian Early Warning & Response Intelligence")

st.markdown("""
This is a basic placeholder dashboard for the HEWRI MVP.
Future versions will include:
- Live data feeds (conflict, displacement, disease, disasters)
- Risk score modeling
- Interactive maps
- Email alert triggers
""")

st.subheader("🧪 MVP Test Data Preview")

# Generate mock risk scores
regions = ["Lebanon", "Ukraine", "Syria", "Türkiye", "Georgia"]
data = {
    "Country": regions,
    "Conflict Risk": np.random.rand(len(regions)) * 100,
    "Displacement Risk": np.random.rand(len(regions)) * 100,
    "Disease Risk": np.random.rand(len(regions)) * 100,
    "Disaster Risk": np.random.rand(len(regions)) * 100,
    "Last Updated": [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] * len(regions)
}
df = pd.DataFrame(data)
st.dataframe(df)

st.success("✅ This MVP is ready to be deployed via Streamlit Cloud or VPS.")
