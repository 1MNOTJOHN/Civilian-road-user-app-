import streamlit as st
import random

# Title
st.title("Civilian Road User Dashboard")

# Random incident generator
incidents = [
    ("Critical", "Crash nearby - emergency on route"),
    ("Warning", "Reckless driving or hard braking detected"),
    ("Caution", "Near miss, possible hazard ahead"),
    ("Cleared", "No recent incidents in this area"),
]

incident_level, incident_description = random.choice(incidents)

# Section: Recent Incident
st.subheader("Recent Incident")
st.markdown(f"**Severity:** {incident_level}")
st.markdown(f"**Description:** {incident_description}")

# Section: Incident Location / Area to Avoid
st.subheader("Incident Location / Area to Avoid")
# Dummy random coordinates
latitude = round(random.uniform(51.0, 51.7), 6)
longitude = round(random.uniform(-0.5, 0.3), 6)
st.map(data={"lat": [latitude], "lon": [longitude]})

# Section: Report Incident (Mock buttons)
st.subheader("Report an Incident")
st.radio(
    "Choose an option:",
    ("Report incident", "Report hazard (icy road, pothole)"),
    index=None,
)
